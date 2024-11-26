# Makefile
DOCKER_ID_USER ?= jenniferli6
IMAGE_NAME ?= de_demo
VERSION ?= latest

# Default target - runs when you just type 'make'
.PHONY: all
all: clean install test build push

# Docker commands
build:
	docker build -t $(DOCKER_ID_USER)/$(IMAGE_NAME):$(VERSION) .

push:
	docker push $(DOCKER_ID_USER)/$(IMAGE_NAME):$(VERSION)

run:
	docker run -p 5001:5000 $(DOCKER_ID_USER)/$(IMAGE_NAME):$(VERSION)

# Development commands
install:
	pip install -r requirements.txt

test:
	python -m pytest

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete

.PHONY: build push run install test clean