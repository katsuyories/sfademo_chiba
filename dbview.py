#firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import pandas as pd

cred = credentials.Certificate("inspired-terra-323815-firebase-adminsdk-c3ned-89ba579fd5.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

class Visits():
    db_ref_r = db.collection('千葉市')
    docs = db_ref_r.stream()
    view_list = [doc.to_dict() for doc in docs]
    df_vl = pd.DataFrame(view_list)
    #view_list_sample
    #[{'住所': '〒260-0026 千葉市中央区千葉港5-25（千葉みらい地域本部住所）', '正式名称': '千葉みらい農業協同組合', 'URL': 'http://www.ja-chibamirai.or.jp/'}, {'正式名称': 'しょいか～ご千葉店', '住所': '千葉市若葉区小倉町871', 'URL': 'http://www.syoicargo.jp/'}, {'URL': 'https://www.pref.chiba.lg.jp/ap-chiba/index.html', '正式名称': '千葉農業事務所_企画振興課', '住所': '〒266-0014 千葉市緑区大金沢町473-2'}, {'URL': 'https://www.pref.chiba.lg.jp/ap-chiba/index.html', '正式名称': ' 千葉農業事務所_総務課', '住所': '〒290-0056 市原市五井5500-4'}]

    name = df_vl['正式名称']
    address = df_vl['住所']
    url = df_vl['URL']
    gmap = "http://maps.google.co.jp/maps?q=" + str(name)
