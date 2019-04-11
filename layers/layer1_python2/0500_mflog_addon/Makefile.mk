include ../../../adm/root.mk
include $(MFEXT_HOME)/share/subdir_root.mk

EGG_P2=mflog_metwork_addon-0.0.0-py$(PYTHON2_SHORT_VERSION).egg

clean:: pythonclean

all:: dist/$(EGG_P2)

dist/$(EGG_P2):
	python setup.py install --prefix=$(MFCOM_HOME)/opt/python2

test:
	@echo "***** PYTHON2 TESTS *****"
	flake8.sh --exclude=build .
	find . -name "*.py" ! -path './build/*' -print0 |xargs -0 layer_wrapper --layers=python2@mfext -- pylint.sh --errors-only
