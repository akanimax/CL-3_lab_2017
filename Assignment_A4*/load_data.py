from pymongo import MongoClient

f = open('data.txt').read().strip().split("\n")

connection = MongoClient("localhost", 27017)
db = connection.test.diniraw7

for line in f:
	record=line.strip().split(",")
	post={"ph_no" : int(record[0]), "temp" : int(record[1])}
 	db.insert(post)
