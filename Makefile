.PHONY: run test format

run:
		FLASK_ENV=development flask run

test:
		PYTHONPATH=. pytest

format:
		isort . ; ruff check --fix ; ruff format ; black .