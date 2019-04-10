import os

MODULE = os.environ['MODULE']
HOSTNAME = os.environ['MFCOM_HOSTNAME']
MODULE_VERSION = os.environ.get('MODULE_VERSION', 'unknown')
PLUGIN_NAME_ENV_VAR = "%s_CURRENT_PLUGIN_NAME" % MODULE
PLUGIN = os.environ.get(PLUGIN_NAME_ENV_VAR, "#core#")


def transform_func(dict_object):
    if "name" in dict_object:
        # FIXME: don't hardcode elasticsearch here
        # But it's difficult to block elasticsearch logger where it's used only
        # in jsonlog2elasticsearch
        if dict_object['name'] in ("elasticsearch", "jsonlog2elasticsearch"):
            return None
    dict_object["module"] = MODULE
    dict_object["hostname"] = HOSTNAME
    dict_object["module_version"] = MODULE_VERSION
    dict_object["plugin"] = PLUGIN
    return dict_object
