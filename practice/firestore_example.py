# Firestore Database 연동

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

#Firebase database 인증 및 앱 초기화
cred = credentials.Certificate('practice/path/to/cpoint-serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'projectId':'cpoint-map',
})
db = firestore.client()

doc_ref = db.collection(u'users').document(u'user01')
doc_ref.set({
    u'level': 20,
    u'money': 700,
    u'job': "knight"
})

users_ref = db.collection(u'users')
docs = users_ref.stream()

for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))