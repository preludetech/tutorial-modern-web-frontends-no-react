# Installation 

Follow these steps to get the project set up:

## 1. Install UV

We'll be using uv to manage our dependencies. You can see how to install it [here](https://docs.astral.sh/uv/getting-started/installation/)

## 2. Install python packages

Run this to download all the Python dependencies and set up a virtual env:

```
uv sync
```

## 3. Install playwright

We'll be using Playwright towards the end of the tutorial. It's a browser automation testing tool

```
playwright install
```

There is a chance that it will say your system is missing dependencies, but it will tell you how to install them.


Check that it was installed properly by running 

```
uv run pytest
```

You should see 1 test passed.

## 4. Database setup

We're using sqlite for our database. First, run the migrations to set up all the tables:

```
uv run python manage.py migrate
```

Now run this to put some data in the database:

```
uv run python manage.py add_todos
```

## Run the development server

```
uv run python manage.py runserver
```

You will now be able to see the application running at http://127.0.0.1:8000/

# What to expect 

As it stands, the web app looks nice enough. But it is not fully implemented. 