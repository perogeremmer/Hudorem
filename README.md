# Hudorem Migration Library

Hudorem Migration Library is a Python library inspired by Laravel Migration. Hudorem allows developers to create and run database migrations similar to Laravel's migration system. With this library, developers can create migrations based on dates and use schema objects to define database schema changes.

## Features

- Create database migrations based on dates.
- Define database schema changes using schema objects.
- Run migrations to apply changes to the database.

## Installation

You can install Hudorem Migration Library using pip:

```bash
pip install hudorem
```

## How to use


### Create migration

```python
python cli.py migration:create migration_name
```

The migration does not supported space, if you want to use more than 1 word, use quotes as example "create user table".

### Run migration

```python
python cli.py migrate
```

The migration does not supported space, if you want to use more than 1 word, use quotes as example "create user table".


## Development

1. Clone project
2. Create virtualenv and activate
3. Install poetry

```bash
pip install poetry
```

4. Run poetry install

```bash
poetry install --no-root
```
