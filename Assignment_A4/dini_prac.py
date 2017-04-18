import sys
from pymongo import MongoClient
import threading
from threading import Thread
import time

class Philosophers(Thread):
	connection = MongoClient("localhost",27017)

	def read_mongo(self,indexx):
		db = Philosophers.connection.test.diniraw7  #Philosophers.connection.DB.coll_name
		cursor = db.find({"ph_no":indexx})
 		sys.stdout.write(str(cursor[0]) + "\n")



	def __init__(self,indexx,name,leftFork,rightFork):
		Thread.__init__(self)
		self.name = name
		self.indexx = indexx
		self.leftFork = leftFork
		self.rightFork = rightFork




	def run(self):
		while(self.running==True):  #note:  self.running !
			sys.stdout.write('Philosopher ' + self.name + ' is hungry\n')
			self.get_fork()

	def get_fork(self):
		fork1 = self.leftFork
		fork2 = self.rightFork

		while(self.running == True):
			fork1.acquire(True)
			val = fork2.acquire(False)
			if val: break

			fork1.release()   #if not got 2nd fork,release first fork

			sys.stdout.write(self.name + " swaps the forks\n")
			fork1, fork2 = fork2, fork1  #swap
		else:
			return

		self.dine()
		fork1.release()
		fork2.release()


	def dine(self):
		sys.stdout.write("Philosopher " + self.name + " is finally eating\n")
		self.read_mongo(self.indexx)
		time.sleep(3)
		sys.stdout.write("Philosopher " + self.name + " is finally finished eating\n")

def Dining():
	fork=[]
	
	for i in range (5):
 		fork.append(threading.Lock())
	
	names = ("Animesh","Giraffe","Colha","donkey","Erlich")
	
	phils = []
	for i in range(5):
		phils.append(Philosophers(i,names[i],fork[i%5],fork[(i+1)%5]))

	Philosophers.running = True   #note:  Philosophers.running !
	for p in phils:
		p.start()
 
	time.sleep(30)
	Philosophers.running = False
	sys.stdout.write("Finishing!\n")

Dining()
