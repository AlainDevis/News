from flask import render_template, request, redirect, url_for
from  .request import get_sources,get_articles
from .models import Source, Articles
from . import models

@main.route('/')
def index():
    business = get_sources('business')
    general = get_sources('general')
    entertainment = get_sources('entertainment')
    sports = get_sources('sports')

    return render_template('index.html', business=business, 
    entertainment=entertainment,general=general,sports=sports)

@main.route('/sources/<id>')
def articles(id):

    article = get_articles(id)

    return render_template('article.html', article= article)