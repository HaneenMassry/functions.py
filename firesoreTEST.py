import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db=firestore.client()

#teacheres = ["aa","bbb","www"] #בניית מערך
#teacheres.append("zzz") #הוספה למערך
#print (teacheres)

#Class=(str)(input("writewhichclass"))
#Subject=(str)(input("writethesubjectname"))
#Teacher=(str)(input("teachername"))
#teacheres.append(Teacher)
#SchoolName=(str)(input("Writeschoolname"))
#db.collection('School').add({'Schoolname':SchoolName,'Teachers':teacheres,'Subject':Subject,'Classes':Class})


#where() to query for all of the documents that meet a certain condition
#docs = db.collection('School').where(u'Subject', u'==', u'Math').stream()
#for doc in docs:
 #   print(doc.to_dict())


#result = db.collection('School').document('zdupZyxO34u6aS7gP2Bf').get()
#if result.exists:
#    print(result.to_dict())
#else :
#    print("false")
subjects=[]
teachers = []  # בניית מערך
def creatSchool(teachers,subjects):

    teacherNum= (int)(input(" how many teachers in the school?"))
    for x in range(teacherNum):
        teacher=(str)(input("write the teacher name"))
        teachers.append(teacher)

    st=""
    while st!="Done" :
        st=(str)(input("wtite the subject name, if done type #Done#"))
        if st!="Done":
         subjects.append(st)

    SchoolName = (str)(input("Writeschoolname"))
    db.collection('School').add({'Schoolname': SchoolName, 'Teachers': teachers,'Subjects':subjects})




def addTeacher(teachers):
    newTeacher=(str)(input("write the name of the new teacher"))
    WhichSchool=(str)(input(" To ehich school do you want to add this teacher?"))
    teachers.append(newTeacher)
    print(teachers)
    docs = db.collection('School').where(u'Schoolname', u'==', WhichSchool).stream()
    for doc in docs:
     doc.reference.update({u'Teachers': teachers})
     print(doc.to_dict())


#sss
def addSubject(subjects):
    newSubject = (str)(input("write the name of the new Subject"))
    WhichSchool = (str)(input("To which school do you want to add this teacher?"))
    subjects.append(newSubject)
   # print(teachers)
    docs = db.collection('School').where(u'Schoolname', u'==', WhichSchool).stream()
    for doc in docs:
        doc.reference.update({u'Subjects': subjects})
       # print(doc.to_dict())




creatSchool(teachers,subjects)
addTeacher(teachers)
addSubject(subjects)




