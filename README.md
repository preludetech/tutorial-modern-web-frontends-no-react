# Installation 

1. Install uv

2. Install Python packages

```
uv sync
```

3. Install playwright

```
playwright install
```

There is a chance that it will say your system is missing dependencies, but it will tell you how to install them.


Check that it was installed properly by running 

```
uv run pytest
```



4. Run database migrations

```
uv run python manage.py migrate
```

5. Add some Todos to the database so we have something to look at

```
uv run python manage.py add_todos
```

6. Run the server 

```
uv run python manage.py runserver
```

