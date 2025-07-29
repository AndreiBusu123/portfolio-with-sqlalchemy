**Portfolio with SQLALchemy**

This project is a portfolio application built using Flask and SQLAlchemy. 

To run the app locally head to the project directory:
1. run 'pip install -r requirements.txt'
2. run 'python app.py'
3. Open your browser and go to http://localhost:5000 (check the console logs for the exact address as it could be different)
4. Enjoy the app!



What I have learned:



Flask-SQLAlchemy Model and Database Connection
Create a model class for adding and editing project information. Connect to the database.

NOTE: When run, the database should already contain at least the 4 previous projects of the Techdegree.

Routes for the Application
Create each of the following routes for your application

/ - Known as the root page, homepage, or landing page.

/projects/new - The Create route

/projects/<id> - The Detail route

/projects/<id>/edit - The Edit or Update route

/projects/<id>/delete - Delete route

NOTE: Each route is of course prefixed with the running server address

Example: The route /project would be mapped to: http://<address>:<port>/project

Create the Homepage route/view
Route: /

This view should render a page of all of the projects, where each project displays the following fields:

Title - should be a linked title, clicking it routes the user to the detail page for the clicked project.
Short description - Each project should have a short description of what the project is about.
Skills practiced - a list of the skills practiced in the project
GitHub link - A link to the project on GitHub
Create the Detail route/view
Route: /project/<id>

This view should render a detail page of a project, it should display the following fields on the page:

Title
Date
Description
Skills practiced
Link to the project’s GitHub repo
NOTE: This page should contain a link/button that takes the user to the Edit route for the project with this <id>.

Create the Add route/view
Create an add view with the route /project/new that allows the user to add a project with the following fields:

Title - string
Date - date
Description - text
Skills - text
GitHub repo link - text
The page should present a new blank project form that allows the user to Create a new project that will be stored in the database.

Create the Edit route/view
Route: /project/<id>/edit

Create an edit view with the route /project/<id>/edit that allows the user to edit the project with an id of the <id> passed in:

Title
Date
Description
Skills practiced
GitHub repo link
Ideally, you should pre-populate each form field with the existing data on load. So the form is filled out with the existing data so the User can easily see what the value is and make edits to the form to make the update.

NOTE: Updating a project should not result in a new project being created, this behavior would not be seen as editing this would be adding a new project. To check this, you can simply make an edit and then reload the listing page to see if a duplicate record was created.

Create the Delete route
Create a delete route to delete the project from the database. When the delete button is clicked by the user, the project will be removed from the database and they will be redirected to the homepage.

Use the supplied HTML/CSS
Use the supplied HTML/CSS to build and style your pages. Use CSS to style headings, font colors, project container colors, and body colors.

You will want to create two folders in your project root for these files:

Create a templates folder that will hold your HTML template files to be used for rendering pages.

Create a static folder that should hold your .css files that you can reference from your HTML templates to style your pages.

Python Coding Style
Coding style or PEP 8 are guidelines for writing clean, readable code, to keep yourself in the best practices of writing Python you should get into a strong habit of checking out the most common PEP guidelines for writing Python code so your code looks similar to professionals in the industry.

Make sure your code complies with the most common PEP 8 Guidelines

Review the following sections of the link above:

Code Layout
Indentation
Tabs or Spaces?
Maximum Line Length
Blank Lines
Imports
Include dependencies file
Anytime you have a project that you build that required you to pip install <some package> so that you could use that package as an import into your own project, such as pip install Flask or pip install flask-sqlalchemy these become what are known as dependencies. These dependencies are required to be able to run your project because of this you will always need to ensure you provide a dependencies file in the root of your project folder.

A common convention is to have one of the following files, but NOT both:

Pipfile -- used commonly with Pipenv
requirements.txt -- used commonly with Virtualenv
Either is acceptable to use and depends on which method you use to install your third-party packages into your Python virtual environment.

You can generate a requirements.txt file with the command listed below, but first, you will want to ensure that you are inside an activated python virtual environment. Check out the Additional Resources for a related video about Virtual Environments.

Command to generate dependencies file:

pip freeze > requirements.txt

NOTE: Ensure you are inside an activated Python Virtual Environment.

Before submitting the project
Before you submit your project, check off each item in the project submissions checklist below.

 I have read all of the project instructions, including the “How you’ll be graded” section for this project.

 I understand what is needed to receive a Meets or Exceeds Expectations grade, and asked for clarification about grading requirements on Slack if necessary.

 My GitHub repo for this project contains only this project, only files needed to make this project run, and a README.md file providing details about my project.

 I wrote all of my own code for this project. Any code included in my project that I did not write myself is appropriately attributed to its source.

 I have completed all of the project requirements and believe the project is ready to receive a meets or exceeds expectation grade.

 I have received a preliminary review of my project in Slack to catch anything I might have missed.

 I understand that in order to receive an Exceeds Expectations grade, I must complete all extra credit items.

 I understand that what I submit is what will get reviewed and that when I submit my project, any changes I make after the submission won't be seen by my reviewer.

Extra Credit
To get an "exceeds" rating, complete all of the steps below:

 3 steps
Create a layout.html file
The layout.html file should include any repeated content in each HTML file. IE: Add the footer to the layout.html file, and replace the footer in the rest of the template pages with the notation for displaying the footer.

Create an About page
Create an about page route and fill out the HTML template.

404 Route
Create a 404 route and HTML template. The 404 route should be triggered whenever an error occurs - ie: incorrect URL, wrong project id, etc.

NOTE: Getting an "Exceed Expectations" grade.

See the rubric in the "How You'll Be Graded" tab above for details on what you need to receive an "Exceed Expectations" grade.
Passing grades are final. If you try for the "Exceeds Expectations" grade, but miss an item and receive a “Meets Expectations” grade, you won’t get a second chance. Exceptions can be made for items that have been misgraded in review.
Always mention in the comments of your submission or any resubmission, what grade you are going for. Some students want their project to be rejected if they do not meet all Exceeds Expectations Requirements, others will try for all the "exceeds" requirement but do not mind if they pass with a Meets Expectations grade. Leaving a comment in your submission will help the reviewer understand which grade you are specifically going for