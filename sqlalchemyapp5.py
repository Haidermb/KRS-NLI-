from flask import Flask , render_template, request
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///college1.db', echo = True)
meta = MetaData()
conn = engine.connect()

app= Flask(__name__)


students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String),
)
#meta.create_all(engine)

# insert data into db
conn.execute(students.insert(), [
   {'name':'Komal','lastname' : 'Bhandari'},
   {'name':'Abdul','lastname' : 'Sattar'},
   {'name':'Priya','lastname' : 'Rajhans'},  
])

#to print data from db
s = students.select()
conn = engine.connect()
result = conn.execute(s)
for row in result:
   print (row)


if __name__=="__main__":
    app.run(debug=True)
