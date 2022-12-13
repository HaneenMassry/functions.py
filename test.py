# Python3 program to
# demonstrate instantiating
# a class

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db, storage


class Dog:

	# A simple class
	# attribute
	attr1 = "mammal"
	attr2 = "dog"

	# A sample method
	def fun(self):
		print("I'm a", self.attr1)
		print("I'm a", self.attr2)


# Driver code
# Object instantiation
Rodger = Dog()

Rodger.attr1="koko"
Rodger.attr2="hi"

# Accessing class attributes
# and method through objects
print(Rodger.attr1)
Rodger.fun()

#cred = credentials.Certificate('firebase-sdk.json')
#firebase_admin.initialize_app(cred, {

  #  'storageBucket': 'uploadtest-2e678.appspot.com',

 #   'databaseURL': 'https://uploadtest-2e678-default-rtdb.firebaseio.com/'
#})

#ref=firebase_admin.db.reference().child("lesssons")
#ref.push(Rodger.__dict__)
#ret=ref.child("-NDgMaAbK2d6fAs2VAFa").get()
#print("retrieved")
#print(ret)
