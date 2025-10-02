.PHONY: all lint test install dev clean distclean

PYTHON ?= python

all: ;

lint:
	q2lint
	flake8

test: all
	py.test

build-matryoshka: all distclean
	npm install --prefix reports/matryoshka
	npm run build --prefix reports/matryoshka
	mkdir -p q2templates/reports/built_assets/matryoshka
	cp -r reports/matryoshka/build/* q2templates/reports/built_assets/matryoshka

build-reports: build-matryoshka ;

install: all build-reports
	$(PYTHON) -m pip install -v .

dev: all build-reports
	pip install -e .

clean: distclean

distclean: ;
	rm -rf q2templates/reports/built_assets/*
