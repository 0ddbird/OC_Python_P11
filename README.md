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
- After cloning, change into the directory and type 
```bash
python -m venv venv
```  
This will then set up a a virtual python environment within that directory.

### Activating the virtual environment
```bash
source venv/bin/activate
```

### Dectivating the virtual environment
```bash
deactivate
```

### Installing the requirements

```bash
pip install -r requirements/requirements.txt
```

### (Optional) Installing the development requirements
```bash
pip install -r requirements/dev-requirements.txt
```

### Creating a .env file
```bash
cat > .env
```    
then type:  
```bash
FLASK_SECRET_KEY=<a_secret_key_of_your_choice>
```  
then press CTRL+D to save and exit.  


## 4. Usage

### Run the server

```bash
make run
```
then navigate to http://127.0.0.1:5000

### Run the test suite (dev dependencies must be installed)

```bash
make test
```

### Generate coverage report (dev dependencies must be installed)

```bash
make cov
```
then you can find the generated report at `~/reports/coverage/index.html`

### Run Locust (dev dependencies must be installed)

```bash
make locust
```
then navigate to http://0.0.0.0:8089