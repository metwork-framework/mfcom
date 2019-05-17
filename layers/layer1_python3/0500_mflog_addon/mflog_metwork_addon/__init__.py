import os

MODULE = os.environ['MODULE']
CURRENT_PLUGIN_ENV_VAR = "%s_CURRENT_PLUGIN_NAME" % MODULE
if CURRENT_PLUGIN_ENV_VAR in os.environ:
    PLUGIN = os.environ[CURRENT_PLUGIN_ENV_VAR]
else:
    PLUGIN = "#core#"
REQUEST_ID_ENV_VAR = "%s_CURRENT_REQUEST_ID" % MODULE


def extra_context():
    extra_context = {
        "plugin": PLUGIN
    }
    if "REQUEST_ID_ENV_VAR" in os.environ:
        extra_context["request_id"] = os.environ["REQUEST_ID_ENV_VAR"]
    return extra_context
