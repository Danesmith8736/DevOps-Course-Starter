# DevOps Apprenticeship: Project Exercise

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```


The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.


Update the three trello vars in the .env file to include the correct board id, API key and API token you can get these by clicking the following link https://trello.com/app-key


## Testing the code works as expected

To test the app is working as expected there are two sets of tests.
Unit tests are to check the code with a static data set, the data file is created to run against 3 tests
Intergratio tests are to check the pages are running correctly with stub data

to run these tests: 
*Press control shift P in VSCode and find Python:Configure tests
*Select Pytest then select the todo_app folder
*Select the test window (dispalyed as a science beaker)
*Run all tests under the test explorer
*Also you can run these via the command line by typing "Poetry run Pytest"  


## Running in docker 

To build the to-do app in Docker run the following two commands depending on env you wish to run
docker build --target development --tag todo-app:dev .
docker build --target production --tag todo-app:prod .

To run the APP in Docker run either of the two commands depending on env you wish to run
docker run --env-file ./.env -p 3500:80 --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app todo-app:dev
docker run --env-file ./.env -p 3500:80 --mount type=bind,source="$(pwd)"/todo_app,target=/app/todo_app todo-app:prod

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.



