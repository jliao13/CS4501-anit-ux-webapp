# CS4501-anit-ux-webapp

Shouldn't have to edit anything except for the html files in templates folder. 

## How to run Heroku app locally:

```
source venv/bin/activate
heroku local
```

## How to push Heroku app
```
git add .
git commit -m <commit-message>
git push heroku <branch-name>
git push 
```

Make sure to verify that all your commits got pushed with 'git push' at the end. 

Edit static files make sure to run the following to update:
```
python manage.py collectstatic
```

Run local django:
```
python manage.py runserver
```