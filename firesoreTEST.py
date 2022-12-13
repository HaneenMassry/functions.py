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

teachers = ['']  # בניית מערך
def creatSchool(teachers):

    teacherNum= (int)(input(" how many teachers in the school?"))
    for x in range(teacherNum):
        teacher=(str)(input("write the teacher name"))
        teachers.append(teacher)

    SchoolName = (str)(input("Writeschoolname"))
    db.collection('School').add({'Schoolname': SchoolName, 'Teachers': teachers})




def addTeacher(teachers):
    newTeacher=(str)(input("write the name of the new teacher"))
    WhichSchool=(str)(input(" To ehich school do you want to add this teacher?"))
    newTeachers=teachers.append(newTeacher)
    print(newTeachers)
    #docs = db.collection('School').where(u'Schoolname', u'==', WhichSchool).stream()
    #for doc in docs:
     #  key = doc.id
      #doc.reference.update({u'Teachers': newTeachers})
      # db.collection('School').document(key).update({"Teachers":newTeachers})
      # print(doc.to_dict())


#sss
#def addSubject:


#creatSchool(teachers)
addTeacher(teachers)





