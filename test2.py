import firebase_admin
from firebase_admin import credentials
from firebase_admin import db, storage

class Lesson:
    # Class Variable
    lesson = 'LClass'

    # The init method or constructor
    def __init__(self, Subject,Teacher,Class,Video,Srt_File,VideoLink,SRT_Link):
        # Instance Variable
        self.Subject=Subject
        self.Teacher=Teacher
        self.Class=Class
        self.Video=Video
        self.Srt_File=Srt_File
        self.VideoLink=VideoLink
        self.SRT_Link=SRT_Link



    # Retrieves instance variable
    def getSubject(self):
        return self.Subject

    def getTeacher(self):
        return self.Teacher

    def getClass(self):
        return self.Class

    def getVideo(self):
        return self.Video

    def getSrtFile(self):
        return self.Srt_File


# Driver Code
Class = (str)(input("write which class"))
Subject = (str)(input("write the subject name"))
Teacher = (str)(input("teacher name"))
lessonName = (str)(input("Write lesson name"))
Video=lessonName+".mp4"
Srt_File = lessonName+".txt"

VideoLink="ללללל"
SRT_Link="ליייייי"

Lesson1= Lesson(Subject,Teacher,Class,Video,Srt_File,VideoLink,SRT_Link)
#print(Lesson1.getSubject())
#print(Lesson1.getTeacher())
#print(Lesson1.getClass())
#print(Lesson1.getVideo())
#print(Lesson1.getSrtFile())


cred = credentials.Certificate('firebase-sdk.json')
firebase_admin.initialize_app(cred, {

    'storageBucket': 'uploadtest-2e678.appspot.com',

    'databaseURL': 'https://uploadtest-2e678-default-rtdb.firebaseio.com/'
})

ref=firebase_admin.db.reference().child("lesssons")
ref.push(Lesson1.__dict__)
ret=ref.child("-NDgMaAbK2d6fAs2VAFa").get()
print("retrieved")
#print(ret)




def uploadLesson(lesson):
    ref = firebase_admin.db.reference().child("lesssons")
    ref.push(lesson.__dict__)
    ret = ref.child("-NDgMaAbK2d6fAs2VAFa").get()
    print("retrieved")
