# Installation 

1. Install uv

2. Install Python packages

```
uv sync
```

3. Run database migrations

```
uv run python manage.py migrate
```

4. Add some Todos to the database so we have something to look at

```
uv run python manage.py add_todos
```

5. Run the server 

```
uv run python manage.py runserver
```


## Tutorial tags

We are using git tags to move through the different versions of this tutorial. 

To list available tags: 

```
git tag
```

To checkout a specific tag:

```
git checkout {tag_name}
```