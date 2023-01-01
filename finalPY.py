from functions import *
from firesoreTEST import *


Classes = []
subjects = []
teachers = []


print('create school:1\nadd teacher to school:2\nupload lesson:3')

st = (int)(input("what do you want to do?"))
if st==1:
    creatSchool()

if st==2:
    addTeacher()

if st==3:
    uploadfinal()