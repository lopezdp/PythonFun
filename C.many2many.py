import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# create new tables
cur.executescript('''
	DROP TABLE IF EXISTS User;
	DROP TABLE IF EXISTS Course;
	DROP TABLE IF EXISTS Member;

	CREATE TABLE User(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	name TEXT UNIQUE
	);

	CREATE TABLE Course(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	title TEXT UNIQUE
	);

	CREATE TABLE Member(
	user_id INTEGER, 
	course_id INTEGER,
	role INTEGER,

	PRIMARY KEY (user_id, course_id)
	)
	''')

# create a file handler var that will take in the raw json data
fileName = raw_input('Enter file name: ')
if(len(fileName) < 1): fileName = 'roster_data.json'

# Data Structure modeled in JSON
# [ "Charley", "si110", 1 ],
# [ "Mea", "si110", 0 ],


# open file handler and read data into a var
strData = open(fileName).read() 

# load strData with json and create list of data inside of jsonData variable
jsonData = json.loads(strData)

# loop through list of json data first index of list is user name & 2nd index is the course title & 3rd index is role data
# store data in variables, then insert into DB, then SELECT id and store in variable
# commit data to DB

for entry in jsonData:
	name = entry[0]
	title = entry[1]
	role = entry[2]

	# print the data to ensure it has been collected
	print name, title

	# insert the name into the DB if it already exists then ignore it
	cur.execute('''INSERT OR IGNORE INTO User(name) VALUES(?)''', (name, ))

	# get the user_id from the entry that previously executed & store into a variable
	cur.execute('SELECT id FROM User WHERE name = ?', (name, ))
	user_id = cur.fetchone()[0]

	# insert the course into the DB if it already exists then ignore it
	cur.execute('''INSERT OR IGNORE INTO Course(title) VALUES(?)''',(title, ))

	# get the course_id from the entry that previously executed & store into a variable
	cur.execute('SELECT id FROM Course WHERE title = ?', (title, ))
	course_id = cur.fetchone()[0]

	cur.execute('''INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES(?,?,?)''', (user_id, course_id, role))

	conn.commit()













