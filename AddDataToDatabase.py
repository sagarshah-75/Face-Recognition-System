import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':"https://faceattendancerealtime-fdc5b-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {

"122":
        {
            "name": "PM Modi",
            "major": "Political Science",
            "starting_year": 2022,
            "total_attendance": 20,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2023-10-19 00:54:34"
        },
    "123":
        {
            "name": "Elon Musk",
            "major": "Innovation",
            "starting_year": 2022,
            "total_attendance": 12,
            "standing": "B",
            "year": 2,
            "last_attendance_time": "2023-10-11 00:54:34"
        },
    "1233":
        {
            "name": "Sagar Shah",
            "major": "B.Tech(CSE)",
            "starting_year": 2020,
            "total_attendance": 15,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-10-15 10:54:34"
        },
    "111":
        {
            "name": "Prajwol Giri",
            "major": "B.Tech(CSE)",
            "starting_year": 2020,
            "total_attendance": 3,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-11-15 01:54:34"
        }
}


for key, value in data.items():
    ref.child(key).set(value)
