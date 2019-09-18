MFMODULE=MFCOM
MFMODULE_LOWERCASE=mfcom

-include adm/root.mk
-include $(MFEXT_HOME)/share/main_root.mk

all:: directories
	cd adm && $(MAKE)
	cd config && $(MAKE)
	_layer_dhash root@mfcom >$(MFCOM_HOME)/.dhash
	cd layers && $(MAKE)

clean::
	cd config && $(MAKE) clean
	cd adm && $(MAKE) clean
	cd layers && $(MAKE) clean

test::
	cd layers/layer1_python3/0100_mfutil && make test
	cd layers/layer1_python2/0100_mfutil && make test
	cd layers/layer1_python3/0300_conf_monitor && make test
	cd layers/layer1_python3/0500_mflog_addon && make test
	cd layers/layer1_python2/0500_mflog_addon && make test

directories:
	@for DIR in tmp opt/python2/lib/python$(PYTHON2_SHORT_VERSION)/site-packages opt/python3/lib/python$(PYTHON3_SHORT_VERSION)/site-packages; do mkdir -p $(MFCOM_HOME)/$${DIR}; done
