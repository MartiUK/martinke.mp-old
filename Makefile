clean-pyc:
	$(shell find * -name "*.pyc" | xargs rm -rf)

clean: clean-pyc

test: clean
	coverage run -m py.test tests -s
	coverage report -m
