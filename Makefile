hello:
	echo "I'm here justto say HELLO"

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_operations.py
	python -m pytest -vv test_main.py

lint:
	pylint --disable=R,C operations.py

all: install lint test
