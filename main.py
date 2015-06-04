#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import logging
from google.appengine.api import users
from google.appengine.ext import ndb
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

app.jinja_env.line_statement_prefix = '#'

class Flat(ndb.Model):
    price = ndb.IntegerProperty()
    street = ndb.StringProperty()
    zip_code = IntegerProperty() 
    for_rent = ndb.BooleanProperty()
    city = ndb.StringProperty()
    owners = ndb.KeyProperty(repeated=True)

class Owner(ndb.Model):
    email = ndb.StringProperty()



@app.route('/', methods=['GET'])
def index():

    ### A ignorer en première lecture
    user        = users.get_current_user()
    login_url   = users.create_login_url('/')
    logout_url  = users.create_logout_url('/')
    ###

    ma_variable_integer = 4
    ma_variable_string  = "bonjour"
    a = "adieu"

    return render_template('index.html', toto = ma_variable_integer, tata = ma_variable_string, **locals())


@app.route('/profile', methods=['GET'])
def user_profile():
    # Remarque : Nous avons forçé l'utilisateur à se connecter avant d'accéder à cette fontion > cf. fichier app.yaml >> 'login: required'

    user        = users.get_current_user()
    is_admin    = users.is_current_user_admin()
    login_url   = users.create_login_url(request.path)
    logout_url  = users.create_logout_url(request.path)

    return render_template('profile.html', **locals())


@app.route('/admin/dashboard', methods=['GET'])
def admin_dashboard():

    return "Page réservée à l'administrateur"

@app.route('/search', methods=['POST'])
def search():
    search = request.form["recherche"]
    flat = Flat()
    flat.name = search
    flat.put()
    return render_template('index.html', marecherche = search)

