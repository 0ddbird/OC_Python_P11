# gudlift-registration

## 1. Introduction

This is a proof of concept (POC) project to show a light-weight version of our competition booking platform.  
The aim is the keep things as light as possible, and use feedback from the users to iterate.

## 2. Getting Started

This project uses the following technologies:
- Python v3.x+
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Virtual environment](https://virtualenv.pypa.io/en/stable/installation.html)


## 3. Installation

### Creating a virtual environment
- After cloning, change into the directory and type `python -m venv venv`.  
This will then set up a a virtual python environment within that directory.

### Activating the virtual environment
`source venv/bin/activate`.  

### Dectivating the virtual environment
`deactivate`

### Installing the requirements

`pip install -r requirements/requirements.txt`

### (Optional) Installing the development requirements
`pip install -r requirements/dev-requirements.txt`

### Creating a .env file
`cat > test`    
then type:  
`FLASK_SECRET_KEY=<a_secret_key_of_your_choice>`  
then press CTRL+D to save and exit.  


## 4. Usage

### Run the server
`make run`
then navigate to http://127.0.0.1:5000
### Run the test suite (dev dependencies must be installed)
`make test`

### Generate coverage report (dev dependencies must be installed)
`make cov`, then you can find the generated report at `~/reports/coverage/index.html`

### Run Locust (dev dependencies must be installed)
`make locust` then navigate to http://0.0.0.0:8089