install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
		pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

lint:
	pylint --disable=R,C,W1203,W0702 app.py

test:
	python -m pytest -vv --cov=app test_*.py

format:
	black *.py

run:
	python app.py

all: install lint test format