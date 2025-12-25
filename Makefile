run: # Run development docker build
	. dev.sh

install: # Set up python venv, install pip and npm dependencies
	python3 -m venv .venv
	. .venv/bin/activate
	pip install -r app/server/requirements.txt
	npm install --prefix ./app/client

	mkdir certs
	mkcert -key-file certs/localhost-key.pem \
       -cert-file certs/localhost.pem \
       localhost 127.0.0.1 ::1
	
build: # Run production docker build
	docker build .