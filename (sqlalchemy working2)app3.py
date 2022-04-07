from flask import Flask , render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///krtest2.sqlite'
 
# creating object of class SQLAlchemy with app as parameter 

db = SQLAlchemy(app)
class students(db.Model):
   room= db.Column('Room_No',db.Integer, primary_key = True )
   date = db.Column('Date',db.Date, default=db.func.now())
   bname = db.Column('Borrower_Name',db.String(200))
   btime = db.Column(db.DateTime(timezone=True), server_default=func.now())
   rname = db.Column('Returner_Name',db.String(200))
   rtime = db.Column(db.DateTime(timezone=True), server_default=func.now())
def __init__(self, room, bname, rname):
   self.room = room
   self.bname = bname
   self.rname = rname

@app.route("/h" , methods = ['POST', 'GET'])
def add():
   if request.method == "POST":
        b=students(room=request.form['roomno'],bname=request.form['bname'],rname=request.form['rname'])    
        db.session.add(b)
        db.session.commit()
        return render_template('home.html')

@app.route('/')
def form():
    return render_template('home.html')
 
if __name__=="__main__":
    app.run(debug=True)

