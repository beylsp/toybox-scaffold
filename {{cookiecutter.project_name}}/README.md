# {{cookiecutter.project_title}}

{{cookiecutter.project_description}}

## Local Development

First, prepare the project:

``` bash
$ make setup                                # Prepare the project
```

{%- if cookiecutter.use_db == "yes" %}
The simplest way to run the site makes use of SQLite, which is not the same as production where it will use PostgreSQL:

``` bash
$ make init                                 # Provision the database
```
{%- endif %}

Build the CSS sources and run the site with:

``` bash
$ yarn build                                 # Build CSS sources
$ pipenv run flask run                       # Run the development server
```

Or use the shorthand command:

``` bash
$ make develop
```

{%- if cookiecutter.use_db == "yes" %}
Whenever you make any changes to the database scheme, don't forget to run the migrations script:

``` bash
$ pipenv run flask deploy
```
{%- endif %}

If you prefer not to use the `pipenv` wrapper, you need to activate the virtual environment:

``` bash
$ pipenv shell                               # Activate virtual environment
$ flask run                                  # Run the development server
```

Type `deactivate` to exit the virtual environment:

``` bash
$ deactivate
```
