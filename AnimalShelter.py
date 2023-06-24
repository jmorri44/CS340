from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime
from datetime import datetime

class AnimalShelter(object):

	#Initialization method
	def __init__(self, USER = 'aacuser', PASS = 'userpass', HOST = 'nv-desktop-services.apporto.com', PORT = 32330, DB = 'AAC', COL = 'animals'):		
		
		
		self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
		self.database = self.client['%s' % (DB)]
		self.collection = self.database['%s' % (COL)]
		
		
	#Create a document: Returns true if successful, False if no success	
	def createDocument(self, data):		
		
		if data is not None:
			if type(data) is dict:
				inserted = self.collection.insert_one(data)
				if inserted.inserted_id:
					return True
			else:
				raise Exception ('Data must be of type Dictionary')
				return False
		else:
			raise Exception('Cannot insert blank document')
			return False
		
	
	#Returns a single document	
	def findDocument(self, query):
		mydocument = self.collection.find_one(query)
		
		return mydocument
	
	#Returns a list of documents	
	def findDocuments(self, query):
		mydocuments = self.collection.find(query)
		
		return mydocuments
		
	#Removes all documents matching a single query; returns number deleted	
	def removeDocuments(self, query):
		removeddocuments = self.collection.delete_many(query)
		return removeddocuments.deleted_count
	
	#Returns a count of how many documents match a specific query
	def countDocuments(self, query):
	
		mycount = self.collection.count_documents(query)
		return mycount
		
	#Updates all documents with the given values. Returns a count of updated documents
	def updateDocuments(self, query, values):
	
		updateddocuments = self.collection.update_many(query, values)
		return updateddocuments.modified_count
		
	
		

		
		
		
	def verifyme(self):
	
		#Check client connection
		#Any error will result in a return of false
		#Successful execution will return true
		try:				
			self.client.server_info()
	
		except ConnectionFailure as thiserror:
			
			return False
	
		except:
			
			return False
		
			
		#Check database access
		try:			
			print(self.collection.find_one())
			
		except Exception as e:
			return False
		
			
		
		#If the program reaches this line, all tests passed.
		return True
		
			


		
		
		
