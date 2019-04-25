===============
MFUTIL API
===============

.. The :skip: directive is used here  to avoid substantial warning on classes and functions
which are note in current modules, during documentation build.

.. autosummary::
    mfutil
    mfutil.net
    mfutil.plugins
    mfutil.cli
    mfutil.jinja2_extensions
    mfutil.layerapi2

.. automodapi:: mfutil
   :include-all-objects:
   :skip: flags, get_bash_output_or_die, get_bash_output_or_warning

.. automodapi:: mfutil.net
   :include-all-objects:

.. automodapi:: mfutil.plugins
   :include-all-objects:
   :skip: BashWrapper, BashWrapperException, BashWrapperOrRaise, ExtendedConfigParser, LayerApi2Wrapper
   :skip: get_unique_hexa_identifier, mkdir_p_or_die

.. automodapi:: mfutil.cli
   :include-all-objects:

.. todo:: Check if mfutil.jinja2_extensions is needed in documentation.
.. automodapi:: mfutil.jinja2_extensions
   :include-all-objects:
   :skip: Extension

.. todo:: Check if mfutil.layerapi2 is needed in documentation.
.. automodapi:: mfutil.layerapi2
   :include-all-objects:
   :skip: Glib2Wrapper, c_char, c_char_p, c_int



