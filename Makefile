.PHONY: install run

install:
	@echo "Installing dependencies..."
	pip3 install -r requirements.txt

run:
	@echo "Running the application..."
	python3 main.py