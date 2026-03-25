from flask import app, render_template

@app.route('/todo') 
def todo(): 
    return render_template('todo.html')