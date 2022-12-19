import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

Classes = []
subjects = []
teachers = []  # בניית מערך


Schools=[]
TeSub=[]

def creatSchool(teachers,subjects,Classes):

    SchoolName = (str)(input("Writeschoolname"))

    st = (str)(input("what the type of the school? (Primary School,preparatory School,High school)"))
    if (st == "Primary"):
        for x in range(1, 7):
            Classes.append(x)

    else:
        if (st == "Preparatory"):
            for x in range(7, 10):
             Classes.append(x)

        else:
           for x in range(10, 13):
            Classes.append(x)

    teacherNum = (int)(input(" how many teachers in the school?"))
    for x in range(teacherNum):
        teacher = (str)(input("write the teacher name"))
        teachers.append(teacher)

    st = ""
    while st != "Done":
        st = (str)(input("wtite the subject name, if done type #Done#"))
        if st != "Done":
         subjects.append(st)

    db.collection('School').add({'Schoolname': SchoolName, 'Teachers': teachers, ' Subjects': subjects, 'Classes': Classes})




def addTeacher(teachers,Schools):
    newTeacher = (str)(input("write the name of the new teacher"))
    WhichSchool = (str)(input(" To ehich school do you want to add this teacher?"))
    teachers.append(newTeacher)
    print(teachers)
    docs = db.collection('School').where(u'Schoolname', u'==', WhichSchool).stream()
    for doc in docs:
      doc.reference.update({u'Teachers': teachers})
      print(doc.to_dict())


    Schools.append(WhichSchool)
    docs = db.collection('Teacher').where(u'Teachername', u'==', newTeacher).stream()
    for doc in docs:
        doc.reference.update({u'Schools': Schools})
        print(doc.to_dict())


#sss
def addSubject(subjects):
    newSubject = (str)(input("write the name of the new Subject"))
    WhichSchool = (str)(input("To which school do you want to add this teacher?"))
    subjects.append(newSubject)
    docs = db.collection('School').where(u'Schoolname', u'==', WhichSchool).stream()
    for doc in docs:
        doc.reference.update({u'Subjects': subjects})


def creatTeacher(Schools):
    teachername = (str)(input("write the teacher name"))
    st = ""
    while st != "Done":
        st = (str)(input("wtite the schools name that the teacher works at, if done type #Done#"))
        if st != "Done":
            Schools.append(st)

    db.collection('Teacher').add({'Teachername': teachername, 'Schools': Schools})




creatSchool(teachers,subjects,Classes)
creatTeacher(Schools)
addTeacher(teachers,Schools)
#addSubject(subjects)


