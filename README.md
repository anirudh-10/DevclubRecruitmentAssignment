Drive Link for the Research and Brain Warm up Part
https://drive.google.com/file/d/1e_JCdZq1ZqLP7F2Dv9mlDDg-QVl9jGAD/view?usp=sharing
** How to run the application
Download all rateyourprofessor files in a folder and navigate to that folder in CMD
1. Install Pip
2. Then run  
	1. pip install virtual env
	2. virtualenv env
	3. cd env
	4. cd Scripts
	5. activate
	6. cd ..
	7. cd ..
	8. pip install django
	9. pip install pillow
	10. pip install py3DNS(for validation of email)
	11.pip install django-crispy-forms
	12.python manage.py migrate
	13.python manage.py runserver
And then run the website on http://127.0.0.1:8000/

** Features 

The database setup is the sqlite database(default for django)
I used the library validation_email for validation of the email address provided by the user but it was not working for the iitd domain.
As i have done that for registration domain should be "@iitd.ac.in" and not anything else so i am commenting out the validation part so 
if you want to register a new user you can. Only one account with one email has been setup.


I tried to make a basic page which containen all the reviws and then add search bar to search about any professor or course. 
But the search bar is not working so the basic idea of two entities if failing for now.

All the reviews are posted anonymously and are currently sorted according to the date posted.

Admin can ban any account permanently or upto till he wants.

Admin can see who has posted which review.

Only the admin has the cridibilty to add a course.

5 users with given username and passwords have been created. 


