Sunsurfers
==========

We are the Sunsurfers community. We do live in the present moment - everyday and anytime. This application helps us to explore the world and connect to each other, to be kind and do good deeds.

What is it about? It’s about traveling, adventures, inspiration and self-realization.

This app will help you to find amazing places and broad-minded open people in your proximity as well as around the world. It will help you to become a Sunsurfer.

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

```bash
./manage.py migrate
./manage.py loaddata initial_data
```

Set some environment variables:

```bash
export SECRET_KEY=secret
export TGAUTH_DOMAIN=127.0.0.1
export TGAUTH_TOKEN=
# it would be available on the website anyway
export MAPBOX_TOKEN=pk.eyJ1IjoiZWktZ3JhZCIsImEiOiJjaWhnNW5qd3YwMDd1dHhtNHd1a2FuZ3k4In0.zkrRQneYHOJhLNAbsRuttw
export DEBUG=1
```

And then you should be able to run the development server:

```bash
./manage.py runserver
```

Which would be accessible on [http://127.0.0.1:8000/](http://127.0.0.1:8000).

Admin interface: [/admin/](http://127.0.0.1:8000/admin/) (admin password: admin)

REST API: [/api/v1/](http://127.0.0.1:8000/api/v1/)
