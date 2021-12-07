from flask import Flask, render_template, request, redirect,flash
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
import logging
from flaskwebgui import FlaskUI


# initlizing the flask app
app= Flask(__name__)
ui= FlaskUI(app,width=2000,height=5000)
app.secret_key="secert_key"

app.config['SQLALCHEMY_DATABASE_URI']="mariadb+mariadbconnector://root:admin@127.0.0.1:3306/flask_crud"

app.config['SQLALCHEMY_TRACK_MODITIFICATIONS']=False

db =SQLAlchemy(app)

#Creating the table for database
class Todo(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    task_name= db.Column(db.String(100))
    task_status= db.Column(db.String(100))

    def __init__(self,task_name,task_status) -> None:
        self.task_name = task_name
        self.task_status = task_status
#Table creation ends here

#default routing for the app
@app.route("/")
def home():
    #getting all data
    all_data = Todo.query.all()
    return render_template("index.html", Tasks =all_data)

# creating a route for inserting todo list
@app.route("/addtodo", methods=['POST'])
def addTodo():
    if request.method == 'POST':

        task_name =request.form['task']
        task_status = "notstarted"

        todo_data = Todo(task_name,task_status)
        db.session.add(todo_data)
        db.session.commit()

        flash("Task added successfully !!")

        return redirect(url_for('home'))

# Insertion routes ends

# Creating an Update route
@app.route("/update/<task_id>",methods=['GET','POST'])
def updateTask(task_id):
    if request.method == 'POST':
        new_data = Todo.query.filter_by(task_id =task_id).first()
        app.logger.info(new_data)
        new_data.task_name =request.form['taskName']
        new_data.task_status =request.form['taskStatus']

        db.session.commit()

        flash("Task updated successfully !!")

        return redirect(url_for('home'))
#update routes ends here

#writing delete routes
@app.route("/delete/<task_id>/", methods=['GET','POST'])
def deleteTask(task_id):
    taskData=Todo.query.get(task_id)
    db.session.delete(taskData)
    db.session.commit()

    flash("Task has been deleted successfully!!")
    
    return redirect(url_for('home'))
#delete routes ends here

#main function
if __name__ == "__main__":
    #app.run(debug=True,host='0.0.0.0') #for debugging purpose
    #app.run()
    ui.run()
