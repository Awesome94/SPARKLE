import datetime 
import sqlite3
conn = sqlite3.connect('calender.db')
c = conn.cursor()
c.execute("create table if not exists events(eventId INTEGER PRIMARY KEY ,name vachar, date text, event_type vachar)")
conn.row_factory = sqlite3.Row
class Event(object):
	"""docstring for ClassName"""

	def __init__(self,name,date,event_type):
		self.name = name
		self.event_type  = event_type
		self.date = date


	def add_event(self):	
		c.execute("insert into events(name,date,event_type) Values (?,?,?)",(self.name,self.event_type,self.date))
		conn.commit()


	def list_events(self):
		c.execute("select * from events")
		print(c.fetchall())

	def drop_event(self):
		c.execute("drop table events")
		conn.commit()

	def last_event(self):
		c.execute("select * from events order by eventId desc")
		print(c.fetchone())
				
event = Event("Bootcamp1","12.12.2012","Programming-python");
event.add_event()
# event.list_events()
event.last_event()

		


		
	



