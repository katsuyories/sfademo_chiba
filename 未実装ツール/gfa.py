import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import pandas as pd

# 下のファイルは先程ダウンロードした秘密鍵のパスを入れてください
cred = credentials.Certificate("inspired-terra-323815-firebase-adminsdk-c3ned-89ba579fd5.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

#読み込み
db_ref_r = db.collection('千葉市')
"""
#読み込み(document)
doc_ref = db_ref_r.document('JA支部').get()
if doc_ref.exists:
    print(doc_ref.to_dict())
else:
    print("no document")
"""
#読み込み(collection)
docs = db_ref_r.stream()
vl = [doc.to_dict() for doc in docs]
vl_df = pd.DataFrame(vl)
df_gm = 'http://maps.google.co.jp/maps?q=' + vl_df['正式名称']
vl_df['GMaps'] = df_gm
print(vl_df)
"""
for doc in docs:
    print(doc.to_dict())
"""
target_list = {
                '正式名称':'千葉みらい農業協同組合',
                '住所':'〒260-0026　千葉市中央区千葉港5-25（千葉みらい地域本部住所）',
                'URL':'http://www.ja-chibamirai.or.jp/'
}
"""
#書き込み
db_ref_w1 = db.collection('千葉市')
db_ref_w2 = db.collection('市川市')
#書き込み先1
doc_ref = doc_ref_w1.document('JA支部')
doc_ref.set(target_list)
#書き込み先2
doc_ref = doc_ref_w2.document('JA支部')
doc_ref.set(target_list)
"""
