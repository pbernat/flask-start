#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import logging
from google.appengine.api import users
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():

    ### A ignorer en première lecture
    user        = users.get_current_user()
    login_url   = users.create_login_url('/')
    logout_url  = users.create_logout_url('/')
    ###

    ma_variable_integer = 4
    ma_variable_string  = "bonjour"

    return render_template('index.html', toto_int = ma_variable_integer, tata_str = ma_variable_string, **locals())


@app.route('/admin/dashboard', methods=['GET'])
def admin_dashboard():

    return "Page réservée à l'administrateur"