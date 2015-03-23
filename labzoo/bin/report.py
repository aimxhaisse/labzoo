# -*- coding: utf-8 -*-

import argparse

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    g,
)
from labzoo import (
    Database,
    SessionConfig,
    SessionModel,
)


app = Flask(__name__)
config_path = None
db_path = None


@app.before_request
def before_request():
    g.conf = SessionConfig.load_from_file(config_path)
    g.db_session = Database.load_db(db_path)


@app.route('/')
def home():
    sess = g.db_session()
    benchmarks = sess.query(SessionModel).all()
    return render_template('home.html', benchmarks=benchmarks)


def main():
    parser = argparse.ArgumentParser(
       description='offers a web interface of a LabZoo session')
    parser.add_argument('config', help='path to the YAML file describing the '
                        'check to run')
    parser.add_argument('database', help='path to the database file of the '
                        'session')
    args = parser.parse_args()

    # set global state
    global config_path, db_path
    config_path = args.config
    db_path = args.database

    app.run('0.0.0.0', debug=True)
