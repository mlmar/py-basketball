run: # Run development docker build
	. dev.sh

install: # Set up python venv, install pip and npm dependencies
	python3 -m venv .venv
	. .venv/bin/activate
	pip install -r app/server/requirements.txt
	npm install --prefix ./app/client
	
build: # Run production docker build
	docker build .