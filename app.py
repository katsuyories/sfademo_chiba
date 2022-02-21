from flask import Flask, render_template, request, logging, Response, redirect, flash

#firestore
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import pandas as pd


cred = credentials.Certificate("inspired-terra-323815-firebase-adminsdk-c3ned-89ba579fd5.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def index():
    return render_template('index.html')

@app.route('/list_view')
def list_view_index():
    db_ref_r = db.collection('千葉市')
    docs = db_ref_r.stream()
    vl = [doc.to_dict() for doc in docs]
    vl_df = pd.DataFrame(vl)
    df_gm = 'http://maps.google.co.jp/maps?q=' + vl_df['正式名称']
    vl_df['グーグルマップ'] = df_gm
    header = vl_df.columns
    record = vl_df.values.tolist()

    return render_template('list_view.html', header=header, record=record)

@app.route('/route_view')
def route_view():
    return render_template('route_view.html')

if __name__ == '__main__':
    app.run(debug=true)
