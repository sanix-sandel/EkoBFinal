import os
import secrets
from PIL import Image
from flask import url_for, current_app, render_template, Flask, flash
from flask_mail import Message
from myapp.factory import mail
from myapp.tasks import send_email



def save_picture(form_picture):
    random_hex=secrets.token_hex(8)#we gave the image file a randomized name
    _, f_ext=os.path.splitext(form_picture.filename)
    picture_fn=random_hex + f_ext
    picture_path=os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

 
def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='techyintelo@gmail.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
    {url_for('users.reset_token', token=token, _external=True)}
    If you didn't make this request then simply ignore this email and no changes will be made.
    '''
    mail.send(msg)



def msg_to_dict(to, subject, template, **kwargs):
    msg=Message(subject, sender='techyintelo@gmail.com', recipients=[to])
    msg.body=render_template(template+'.html', **kwargs)
    msg.html=render_template(template+'.txt', **kwargs)
    return msg.__dict__ 

def send_mail(to, subject, template, **kwargs):
    send_email.delay(msg_to_dict(to, subject, template, **kwargs))
   