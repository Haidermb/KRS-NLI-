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

conn.execute(students.insert(), [
   {'name':'Komal','lastname' : 'Bhandari'},
   {'name':'Abdul','lastname' : 'Sattar'},
   {'name':'Priya','lastname' : 'Rajhans'},
])


if __name__=="__main__":
    app.run(debug=True)
