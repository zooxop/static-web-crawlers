# Realtime Database 연동

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#Firebase database 인증 및 앱 초기화
cred = credentials.Certificate('practice/path/to/cpoint-serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://cpoint-map-default-rtdb.firebaseio.com'
})

dir = db.reference()
dir.update({'자동차':['기아', '현대', '벤츠']})

dir = db.reference('이동수단/기차')
dir.update({'1번':'KTX'})
dir.update({'2번':'무궁화'})

dir = db.reference()
print(dir.get())

dir = db.reference('이동수단/기차/1번')
print(dir.get())
