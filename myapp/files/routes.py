from flask import (render_template, url_for, flash, make_response,
                   redirect, request, abort, Blueprint, request, send_file, Response, g, current_app)
from flask_login import current_user, login_required
from myapp.factory import db, mail
from myapp.models import File, Ebook, Cover, User, Notif, Genre
from myapp.files.forms import FileForm, EbookForm, SearchForm
from myapp.users.utils import save_picture, send_reset_email, send_mail, msg_to_dict
from flask import Markup
from flask_mail import Message
from sqlalchemy.orm.util import join
from datetime import datetime
import os
import secrets
from werkzeug.utils import secure_filename


files=Blueprint('files', __name__)


ALLOWED_EXTENSIONS=set(['pdf', 'epub', 'txt'])
EXTENSIONS_ALLOWED=set(['jpeg', 'png', 'jpg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def file_allowed(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in EXTENSIONS_ALLOWED


@login_required
@files.route("/files", methods=['GET', 'POST'])
def allfiles():
    page = request.args.get('page', 1, type=int)
    files = File.query.order_by(File.date_posted.desc()).paginate(page=page, per_page=12)
    genres=Genre.query.all()
    flash('More than '+str(files.total)+' for free downloads', 'success')
    return render_template('Files.html', files=files, genres=genres)


@files.route('/img/<int:img_id>', methods=['GET', 'POST'])
def serve_image(img_id):
    image=Cover.query.get_or_404(img_id)
    return image.data




def sav_picture(form_picture):
    random_hex=secrets.token_hex(8)#we gave the image file a randomized name
    _, f_ext=os.path.splitext(form_picture.filename)
    picture_fn=random_hex + f_ext
    picture_path=os.path.join(current_app.root_path, 'static/pdf_files', picture_fn)

    
    form_picture.save(picture_path)

    return picture_fn


def save_file(pdf_file):
    file_fn=secure_filename(pdf_file.filename)
    file_path=os.path.join(current_app.root_path, 'static/pdf_files', file_fn)
    pdf_file.save(file_path)
    return file_fn



@login_required
@files.route('/home/upload', methods=['GET', 'POST'])
def upload():
    form=FileForm()
    if request.method=='POST':
        fichier=request.files['file']
        cover=request.files['cover']
        if 'file' not in request.files:
            flash('No file part !')
        
        elif fichier.filename=='':
            flash('No file selected ', 'danger')
            return redirect(request.url)  

        elif not (allowed_file(fichier.filename) or file_allowed(cover.filename)):
            flash('Only PDF files, please for files', 'danger')
            flash('And Only png, jpeg, jpg files allowed for cover image', 'danger')
           
         
    #if form.is_submitted():
        else:
            try:

                flash('Your file has been successfully uploaded !', 'succes')
            
                category=form.genre.data
                data=sav_picture(fichier)
                fichier.seek(0, os.SEEK_END)
                file_length=fichier.tell()/1000000
                file_length=str(file_length)[:4]

                newfile=File(title=form.title.data.title(), data=data, description=form.description.data, uploader=current_user, downloaded=0, file_size=file_length, category=category.title, auteur=form.auteur.data)
                cover=Cover(file=newfile, data=cover.read())
                db.session.commit()
                newfile.img_id=cover.id
                db.session.add(cover)  
                db.session.add(newfile)
                db.session.commit()
                return redirect(url_for('files.allfiles'))
            except:
                flash("We're accounting a technical problem right now, try later please", 'danger')    
                return redirect(url_for('files.allfiles'))
    return render_template("File_upload.html", form=form)



@login_required
@files.route('/home/upload/<int:recommender_id>', methods=['GET', 'POST'])
def uploadv(recommender_id):
    form=FileForm()
    recommender=User.query.filter_by(id=recommender_id).first()
    if request.method=='POST':
        fichier=request.files['file']
        cover=request.files['cover']
        if 'file' not in request.files:
            flash('No file part !')
        
        elif fichier.filename=='':
            flash('No file selected ', 'danger')
            return redirect(request.url)  

        elif not (allowed_file(fichier.filename) or file_allowed(cover.filename)):
            flash('Only PDF files, please for files', 'danger')
            flash('And Only png, jpeg, jpg files allowed for cover image', 'danger')
    #if form.is_submitted():
        else:
            
            flash('Your file has been successfully uploaded !', 'succes')
            flash('thank You very much, Keep helping the biblio grow', 'succes')
            
            category=form.genre.data
            data=sav_picture(fichier)
            fichier.seek(0, os.SEEK_END)
            file_length=fichier.tell()/1000000
            file_length=str(file_length)[:4]
            
            newfile=File(title=form.title.data.title(), data=data, description=form.description.data, uploader=current_user, downloaded=0, file_size=file_length, category=category.title, auteur=form.auteur.data)
            cover=Cover(file=newfile, data=cover.read())
            db.session.commit()
            newfile.img_id=cover.id
            db.session.add(cover)  
            db.session.add(newfile)
            db.session.commit()
            msg = Message('E-Books Recommendation',
                  sender='techyintelo@gmail.com',
                  recipients=[recommender.email])
            msg.body = f'''Woopi ! the ebook you needed has been uploaded by a volunteer ! You can check it out 
            If you did not make this request then simply ignore this email and no changes will be made.
            TechyB Team.
                '''
           
            mail.send(msg)

              
    return render_template("File_upload2.html", form=form)




@login_required
@files.route("/file/<int:file_id>", methods=['GET', 'POST'])
def file(file_id):
    
    file = File.query.get_or_404(file_id)
    return render_template('file.html', title=file.title, file=file, cover=file.cover, file_size=file.file_size, img_id=file.img_id)

@login_required
@files.route('/file/<int:file_id>/download', methods=['POST', 'GET'])
def download(file_id):
    file_data=File.query.get_or_404(file_id)
    file_data.downloads()
    db.session.commit()
    try:
        file_path=  os.path.join(current_app.root_path, 'static/pdf_files', file_data.data)
        return send_file(file_path, attachment_filename=file_data.title+"."+file_data.data.split(".")[-1], as_attachment=True) 
    except:
        flash('Sorry, The file has been removed', 'danger')
        return redirect(url_for('files.allfiles'))
    
    

@login_required
@files.route("/home/recommend", methods=['GET', 'POST'])
def recommend():
    form=EbookForm()
    if form.validate_on_submit():
        flash("Your recommendation is received, we'll reply soon", 'success')
        ebook=Ebook(title=form.title.data.capitalize(), author=form.author.data, recommender=current_user)
        db.session.add(ebook)
        db.session.commit()
        send_mail(current_user.email,'Recommendation of an Ebook', 'ebookrecommendation', username=current_user.username, title=ebook.title)
        return redirect(url_for('main.home'))  
    return render_template('Recommend.html', form=form)


@login_required
@files.route('/home/ebooks', methods=['GET'])    
def ebooks():
    page = request.args.get('page', 1, type=int)
    ebooks = Ebook.query.order_by(Ebook.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('Ebooks.html', ebooks=ebooks)


@files.route('/home/files/<string:category>')
def files_bygenre(category):
    form=SearchForm()
    page = request.args.get('page', 1, type=int)
    genre=Genre.query.filter_by(title=category).first()
    genres=Genre.query.all()
    files=File.query.filter_by(category=genre.title)\
        .order_by(File.date_posted.desc())\
        .paginate(page=page, per_page=6)
    return render_template('files_bygenre.html', files=files, genre=genre, form=form, genres=genres)





