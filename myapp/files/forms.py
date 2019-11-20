from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from flask_ckeditor import CKEditorField
import bleach
from flask_wtf.file import FileField, FileAllowed
from flask import request


class FileForm(FlaskForm):
    title=StringField('Title/Titre', validators=[DataRequired(), Length(2, 40)])
    description=TextAreaField('About the doc', validators=[DataRequired(), Length(10, 500)])
    filedata = FileField('Upload the doc', validators=[FileAllowed(['pdf'])])
    submit=SubmitField('Add/Ajouter')
    

class EbookForm(FlaskForm):
    title=StringField('Title / Titre', validators=[DataRequired(), Length(min=2, max=40)])  
    author=StringField('Author / Auteur', validators=[DataRequired(), Length(min=2, max=40)])
    submit=SubmitField('Command/Commander')  


class SearchForm(FlaskForm):
    search = StringField('', validators=[DataRequired()])
    submit=SubmitField('Search/Rechercher')