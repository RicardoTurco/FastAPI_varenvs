# Environments Variables - Test

Example about how to read environments variables from .env file

## Installing

To install and execution the 'example' In your local machine, you will need to:

```
a) Clone this project in your machine:


b) Create and activate one "virtualenv" (SO Linux):

python3 -m venv venv
source venv/bin/activate

** This steps are OPTIONAL, but HIGH recommended !!!

python -m pip install --upgrade pip
(Update 'pip')

pip install -U setuptools
(Update 'setuptools')

pip install wheel 


c) Install the dependences of project:

pip install -r requirements.txt


d) Create your '.env' file based on template 'env.example', filling in all the informatons.
(If this is not done, it will cause an error in execution)


e) Run the project:

uvicorn main:app --host 0.0.0.0 --port 8000 --reload


f) To access documentation/swagger of this 'example':

localhost:8000/docs (on your browser)
```

## Project Structure

Project structure (considering folder start in `FastAPI_varenvs`):

```

├── FastAPI_varenvs
│   ├── app
│   │   ├── __init__.py
│   │   ├── controller
│   │   │    ├── __init__.py 
│   │   │    ├── group.py
│   │   │    ├── user.py
│   │   ├── extension
│   │   │    ├── __init__.py 
│   │   │    ├── general_constants.py
├── .env
├── .gitignore
├── config.py
├── env.example
├── main.py
├── README.md
├── requirements.txt
├── urls.py

```

### Folders

* `FastAPI_varenvs` - "Main" folder of project.
* `app` - All the RESTfull API implementation is here.
* `app/controller` - "Controller" module of project (endpoints).
* `app/extension` - "Extension" module of project (Constants).

### Files

* `.env` - Environments variables of the project (based in env.example file).
* `.gitignore` - Lists files and directories which should not be added to git repository.
* `config.py` - Import the environments variables from '.env' file.
* `env.example` - Template to create '.env' file.
* `main.py` - The Application entrypoint. 
* `README.md` - Instructions and information to run this project locally.
* `requirements.txt` - All project dependencies.
* `urls.py` - Declare all resource routes of project.
* `app/extension/general_constants.py` - Import ALL variables from 'config.py' to pass on to classes of constants

## Environments Variables

The environments variables of project are in '.env' file (based in 'env.example') - [FastAPI documentaton](https://fastapi.tiangolo.com/advanced/settings/#reading-a-env-file).
