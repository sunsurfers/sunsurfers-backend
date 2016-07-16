Sunsurfers
==========

We are the Sunsurfers, we live in the current moment - everyday, anytime. This
application helps us to explore the world, to connect to each other, to be kind,
to make a good deeds.

What's that about? It is about travelling, adventures, inspiration and
self-realization.

This app will help you to find interesting places and open people near you and
around the world. It will try to make you the Sunsurfer.

Run for Development
-------------------

Clone the repo, create virtualenv and install requirements:
```
git clone git@github.com:ei-grad/sunsurfers.git
cd sunsurfers
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

You will need a PostgreSQL server with PostGIS extension to run Sunsurfers, if
you don't have it yet, just follow the
[GeoDjango guide](https://docs.djangoproject.com/en/1.9/ref/contrib/gis/install/#mac-os-x).

If you have PostgreSQL up and running, then create a sunsurfers database with
PostGIS extension enabled:

```
createdb sunsurfers
psql sunsurfers <<< "create extension postgis"
```

Create the database structure and load some initial users and quests for development:

```
./manage.py migrate
./manage.py loaddata initial_data
```

And then you should be able to run the development server:

```
./manage.py runserver
```

Which would be accessible on [http://localhost:8000/](http://localhost:8000).

Admin interface: [/admin/](http://localhost:8000/admin/) (admin password: admin)

REST API: [/api/v1/](http://localhost:8000/api/v1/)
