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

    SchoolName = (str)(input("Write school name"))

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
        docs = db.collection('Teacher').where(u'Teachername', u'==', teacher).stream()
        count=0
        for doc in docs:
            count=count+1

        if count==0:
            creatTeacher(Schools)

        else:
            docs = db.collection('Teacher').where(u'Teachername', u'==', teacher).stream()
            for doc in docs:
                bal = doc.to_dict()[u'Schools']
                #bal = u'{}'.format(get_bal.to_dict())
                check = False
                for j in bal:
                    if j != SchoolName:
                        check = True

                if check:
                   bal.append(SchoolName)
                   doc.reference.update({u'Schools': bal})
                   print(doc.to_dict())


    st = ""
    while st != "Done":
        st = (str)(input("wtite the subject name, if done type #Done#"))
        if st != "Done":
         subjects.append(st)

    db.collection('School').add({'Schoolname': SchoolName, 'Teachers': teachers, ' Subjects': subjects, 'Classes': Classes})




def addTeacher(teachers,Schools):
    newTeacher = (str)(input("write the name of the new teacher"))
    WhichSchool = (str)(input(" To ehich school do you want to add this teacher?"))

    #print(teachers)
    docs = db.collection('School').where(u'Schoolname', u'==', WhichSchool).stream()
    for doc in docs:
        teachers=doc.to_dict()[u'Teachers']
        teachers.append(newTeacher)
        doc.reference.update({u'Teachers': teachers})
        print(doc.to_dict())


    #Schools.append(WhichSchool)
    docs = db.collection('Teacher').where(u'Teachername', u'==', newTeacher).stream()
    for doc in docs:
        bal=doc.to_dict()[u'Schools']
        bal.append(WhichSchool)
        doc.reference.update({u'Schools': bal})
        print(doc.to_dict())


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


st=(str)(input("what do you want to do? upload new school/ upload new teacher/ add teacher to school/ add subject to school"))
if st=="upload school":
    creatSchool(teachers, subjects, Classes)

if st=="upload teacher":
    creatTeacher(Schools)

if st=="add teacher":
    addTeacher(teachers, Schools)

if st == "add subject":
    addSubject(subjects)



