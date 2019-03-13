import os

MODULE = os.environ['MODULE']
HOSTNAME = os.environ['MFCOM_HOSTNAME']
MODULE_VERSION = os.environ.get('MODULE_VERSION', 'unknown')


def transform_func(dict_object):
    if "module" not in dict_object:
        dict_object["module"] = MODULE
    if "hostname" not in dict_object:
        dict_object["hostname"] = HOSTNAME
    if "module_version" not in dict_object:
        dict_object["module_version"] = MODULE_VERSION
    return dict_object
