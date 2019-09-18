===============
MFUTIL API
===============

.. automodule:: mfutil

.. The :skip: directive is used here  to avoid substantial warning on classes and functions
which are note in current modules, during documentation build.

.. autosummary::
    mfutil
    mfutil.net
    mfutil.plugins
    mfutil.cli

.. automodapi:: mfutil
   :include-all-objects:
   :inherited-members:
   :skip: flags, get_bash_output_or_die, get_bash_output_or_warning
   :no-inheritance-diagram:

.. automodapi:: mfutil.net
   :include-all-objects:
   :no-inheritance-diagram:

.. automodapi:: mfutil.plugins
   :include-all-objects:
   :skip: BashWrapper, BashWrapperException, BashWrapperOrRaise, ExtendedConfigParser, LayerApi2Wrapper
   :skip: get_unique_hexa_identifier, mkdir_p_or_die, PluginsBaseDir, MFEXT_HOME, MFMODULE, MFMODULE_LOWERCASE, PLUGIN_NAME_REGEXP, RUNTIME_HOME, SPEC_TEMPLATE
   :no-inheritance-diagram:

.. automodapi:: mfutil.cli
   :include-all-objects:
   :skip:MFUTIL_INSTANCE, print_function
