.PHONY: all lint test test-cov install dev clean distclean

all: ;

lint:
	q2lint
	flake8

test: all

test-cov: all

install: all
	python setup.py install

dev: all
	pip install -e .

clean: distclean

distclean: ;
