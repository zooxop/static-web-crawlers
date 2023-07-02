import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import parsers.parsing_companies as ps

categories = ps.getCategories()
companies = ps.getCompanies()

#Firebase database 인증 및 앱 초기화
cred = credentials.Certificate('practice/path/to/cpoint-serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'projectId':'cpoint-map',
})
db = firestore.client()

# category 정보 update
for index, category in enumerate(categories):
    doc_name = u'category' + '{:02}'.format(index)
    doc_ref = db.collection(u'category').document(doc_name)
    doc_ref.set({
        u'name': category
    })
    print(category)

# company 정보 upadte
for index, companies in enumerate(companies):
    doc_name = u'company' + '{:02}'.format(index)
    doc_ref = db.collection(u'company').document(doc_name)
    doc_ref.set({
        u'name': companies[0],
        u'text': companies[1]
    })
    print(companies[0], companies[1])