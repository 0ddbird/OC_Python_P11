.PHONY: run test format cov locust

run:
		FLASK_ENV=development flask run --debug

test:
		PYTHONPATH=. pytest

format:
		isort . ; ruff check --fix ; ruff format ; black .

cov:
		PYTHONPATH=. pytest --cov=. --cov-report html:reports/coverage --cov-config=.coveragerc

locust: 
		locust -f locustfile.py