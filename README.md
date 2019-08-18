Opt Out Public Api
==========


Add a short description here!


Description
===========

A longer description of your project goes here...

Development
===========
You will need to have `git lfs` installed

Run `poetry install`
and after that `pre-commit install`

You can test your commit checks by running
`pre-commit run`

You will also need to specify django configuration in .env file (which is not committed to repository)
Example
```
DB_NAME=database_name
DB_USER=db_user
PASSWORD=data_base_password
SECRET_KEY=super_secret_password
DEBUG=TRUE
```

Note
====

This project has been set up using PyScaffold 3.2.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.
