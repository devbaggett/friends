from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb_assignment')
@app.route('/')
def index():
	# friends = mysql.query_db("SELECT * FROM friends") OR as follows:
	query = "SELECT * FROM friends" 							# define query
	friends = mysql.query_db(query)								# run query with query_db()
	print friends								
	return render_template('index.html', all_friends=friends)  	# pass data to our template
@app.route('/friends', methods=['POST'])
def create():
	# add a friend to the database!
    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
	query = "INSERT INTO friends (name, age) VALUES (:name, :age)"
	# We'll then create a dictionary of data from the POST data received.
	data = {
    		'name': request.form['name'],
    		'age':  request.form['age']
   			}
   	# Run query, with dictionary values injected into the query.
   	mysql.query_db(query, data)    
	# test form in terminal
	# print request.form['first_name']
	# print request.form['last_name']
	# print request.form['occupation']
	return redirect('/')
app.run(debug=True)