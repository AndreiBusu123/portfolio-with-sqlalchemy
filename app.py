from flask import render_template, request, redirect, url_for 
from models import db, Project, app
from flask_sqlalchemy import SQLAlchemy
import datetime


def check_db_exists():
    if len(Project.query.all()) > 3:
        return
    # if not then add these 4
    # I could have done some kind of check to my github but I think that was beyond the scope of this project
    else :
        initialized_project = []

        if not Project.query.filter(Project.title == 'Guessing Game').first():
            initialized_project.append(Project(title='Guessing Game', date_created=datetime.datetime(2025, 1, 7), description='This is a game where you have to guess the number before your lives run out', 
                                    skills_learnt='For loops, If statements, Random module, Basic Python',
                                    github_link="https://github.com/AndreiBusu123/Guessing-Game.git"))
            
        if not Project.query.filter(Project.title == 'Basketball Stats Tool').first():
            initialized_project.append(Project(title='Basketball Stats Tool',date_created=datetime.datetime(2025, 3, 7), description='This is a tool that allows you to view the stats of your favorite basketball players', 
                                    skills_learnt='Data cleanup, even more data cleanup, and more data cleanup',
                                    github_link="https://github.com/AndreiBusu123/basketball-stats-tool-Andrei.git"))
            
        if not Project.query.filter(Project.title == 'Phrase Hunters').first():
            initialized_project.append(Project(title='Phrase Hunters',date_created=datetime.datetime(2025, 5, 7), description='This is a game where you have to guess the number before your lives run out', 
                                    skills_learnt='Multiple files, Classes, Methods, and more Python',
                                    github_link="https://github.com/AndreiBusu123/Phrase-Hunters.git"))
            
        if not Project.query.filter(Project.title == 'Store Inventory with SQLAlchemy').first():
            initialized_project.append(Project(title='Store Inventory with SQLAlchemy',date_created=datetime.datetime(2025, 7, 21), description='This is a game where you have to guess the number before your lives run out', 
                                    skills_learnt='SQLAlchemy, Databases, sessions, and a little parsaltongue (Python)',
                                    github_link="https://github.com/AndreiBusu123/Store-Inventory-With-SQLAlchemy.git"))
            
        
        db.session.add_all(initialized_project)
        db.session.commit()
        return

@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/project/new', methods=['GET', 'POST'])
def new_project():
    projects = Project.query.all()
    
    if request.method == 'POST':
        new_project = Project(
            title=request.form['title'],
            date_created=datetime.datetime.strptime(request.form['date_created'], '%Y-%m-%d') if request.form['date_created'] else None,
            description=request.form['description'],
            skills_learnt=request.form['skills_learnt'],
            github_link=request.form['github_link']
        )
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('add.html', projects=projects)


@app.route('/project/<id>')
def detail(id):
    project = Project.query.get_or_404(id)
    projects = Project.query.all()
    return render_template('detail.html', project=project, projects=projects)


@app.route('/project/<id>/edit', methods=['GET', 'POST'])
def edit(id):
    project = Project.query.get_or_404(id)
    projects = Project.query.all()
    
    if request.method == 'POST':
        project.title = request.form['title']
        project.description = request.form['description']
        project.skills_learnt = request.form['skills_learnt']
        project.github_link = request.form['github_link']
        
        # Handle date conversion
        if request.form['date_created']:
            project.date_created = datetime.datetime.strptime(request.form['date_created'], '%Y-%m-%d')
        
        db.session.commit()
        return redirect(url_for('detail', id=project.id))
    
    return render_template('edit.html', project=project, projects=projects)

@app.route('/project/<id>/delete', methods=['GET', 'POST'])
def delete(id):
    project = Project.query.get_or_404(id)
    projects = Project.query.all()
    
    if request.method == 'POST':
        db.session.delete(project)
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('delete.html', project=project, projects=projects)


@app.route('/about')
def about():
    projects = Project.query.all()
    return render_template('about.html', projects=projects)


@app.errorhandler(404)
def page_not_found(e):
    projects = Project.query.all()
    return render_template('404.html', projects=projects), 404


if __name__ == '__main__':

    with app.app_context():
        db.create_all()
        check_db_exists()
    app.run(debug=True, port=8000, host='0.0.0.0')

