from flask import (render_template, request, Blueprint, redirect, url_for, current_app, flash)
from myapp.models import Post, File, Genre, Tag
from myapp.files.forms import SearchForm
from myapp.factory import db

main=Blueprint('main', __name__)


@main.route("/",methods=['GET', 'POST'])
@main.route("/home", methods=['GET', 'POST'])
def home():
    
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    tags=Tag.query.all()
    genres=Genre.query.all()
    
    return render_template('Home.html', posts=posts, genres=genres, tags=tags)


@main.route('/home/searching', methods=['GET', 'POST'])
def search_results():  
    """Results=File.query.filter_by(title=searched).all()"""
    
    searched=request.form.get('searched')
    if searched=="":
        flash('Not an empty field', 'danger')
        return redirect(url_for('main.home'))
    else:
        searched=searched.title()
        flash("Searching results of "+searched, 'success')
           
        Results1=File.query.filter(File.title.like('%'+searched+'%'))
        Results2=Post.query.filter(Post.title.like('%'+searched+'%'))
        total1=Results1.count()
        total2=Results2.count()
        return render_template('search.html', results1=Results1, results2=Results2, total1=total1, total2=total2)
                           

@main.route("/about")
def about():
    return render_template('about.html', title='About')


@main.route('/admin')
def securityblock():
    return render_template('errors/404.html'), 404


@main.route("/home/trends")
def trend():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.reads.desc()).paginate(page=page, per_page=5)
    return render_template('trending.html', posts=posts)

"""
form=SearchForm()
    if form.validate_on_submit():
        searched=form.search.data
        searched=searched.capitalize()
        flash('Search results of the keyword '+searched, 'success')
        return search_results(searched) 
"""