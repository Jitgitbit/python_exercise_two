pip3 install django
django-admin

REMOVING from git locally
1) (first remove it from github)
2) rm -rf <python-exercise-two>/.git   NOPE -->  in directory:   rm -rf .git
3) (now remove the directory itself too)

START:
django-admin startproject python_exercise_two

git init
git add .
git commit -m 'first'
gst
and then the github stuff...
git remote add origin git@github.com:Jitgitbit/python_exercise_two.git
git push -u origin master
gst
DONE

python3 manage.py runserver    ------>  http://127.0.0.1:8000/   