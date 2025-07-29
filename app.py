from flask import render_template, request, redirect, url_for 
from models import db, Project, app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/projects/new')
def new_project():
    return render_template('create.html')


@app.route('/projects/<id>')
def detail(id):
    return render_template('detail.html')


@app.route('/edit.html')
def edit(id):
    return render_template('edit.html')


@app.route('/delete/<id>')
def delete(id):
    return render_template('delete.html')



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host='0.0.0.0')

