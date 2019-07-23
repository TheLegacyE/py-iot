import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin import db

cred = credentials.Certificate('./iot-demo-37925-firebase-adminsdk-3pjz8-66decf4d51.json')

default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://iot-demo-37925.firebaseio.com/'
})

ref = db.reference('/')
ref.set({
        'moving':
            {
                'car01': {
                    'moving': 'n0',
                    'message': "Wutang is the greates",
                    'degree':2
                }
            }
        })