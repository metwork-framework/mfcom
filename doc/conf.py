# -*- coding: utf-8 -*-

import os
import sphinx_rtd_theme
# sys.path.insert(0, os.path.abspath('.'))


def get_version():
    """
    :return: # The short X.Y version.
    """
    return ".".join(os.environ.get('MODULE_VERSION',
                                   'unknown.unknown').split('.')[0:-1])


def get_release():
    """
    :return: the full version, including alpha/beta/rc tags
    """
    return os.environ.get('MODULE_VERSION', 'unknown')



# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.viewcode',
              'sphinx.ext.napoleon',
              'sphinx.ext.intersphinx',
              'sphinx.ext.autosectionlabel',
              'sphinx.ext.todo',
              'sphinx_automodapi.automodapi',
              'sphinx_automodapi.smart_resolver',
              ]

# A dictionary of values to pass into the template engine’s context for all pages
html_context = {
    # Enable the "Edit in GitHub link within the header of each page. See https://docs.readthedocs.io/en/stable/vcs.html
    'display_github': True,
    # Set the following variables to generate the resulting github URL for each page.
    'github_user': 'metwork-framework',
    'github_repo': 'mfcom',
    'github_version': 'integration',
    # Path in the checkout to the docs root
    'conf_py_path': '/doc/',
    # Changes how to view files when using display_github, display_gitlab, etc.
    # When using GitHub or GitLab this can be: blob (default), edit, or raw.
    # See https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html#confval-vcs_pageview_mode
    # Warning : the parameter is theme_vcs_pageview_mode and not vcs_pageview_mode as mentionned in the the documentation
    'theme_vcs_pageview_mode': 'edit'
}


# True to prefix each section label with the name of the document it is in,
# followed by a colon. For example, index:Introduction for a section called Introduction that appears in document index.rst.
# Useful for avoiding ambiguity when the same section heading appears in different documents.
autosectionlabel_prefix_document = True

# If set, autosectionlabel chooses the sections for labeling by its depth.
# For example, when set 1 to autosectionlabel_maxdepth, labels are generated only for top level sections,
# and deeper sections are not labeled. It defaults to None (disabled).
autosectionlabel_maxdepth = 3

# The output format for Graphviz when building HTML files. This must be either 'png' or 'svg'
graphviz_output_format = 'svg'

# This must be a string that specifies the name of the directory the automodsumm generated documentation ends up in.
# This directory path should be relative to the documentation root (e.g., same place as index.rst). Defaults to 'api'.
automodapi_toctreedirnm = 'api'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
#source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'mfcom'
copyright = u'2017-2019, MetWork'
author = u'MetWork'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = get_version()

# The full version, including alpha/beta/rc tags.
release = get_release()

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True
# Emits a warning or not for each TO DO entries. The default is False.
todo_emit_warnings = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_style = 'css/override_theme.css'
html_logo = '_images/logo-metwork.png'
html_favicon = '_images/metwork.ico'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'mfcomdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'mfcom.tex',
     u'mfcom Documentation',
     u'MetWork', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'mfcom', u'mfcom Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'mfcom', u'mfcom Documentation',
     author, 'mfcom', 'One line description of project.',
     'Miscellaneous'),
]

napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = True
napoleon_use_param = False
autoclass_content = 'both'


def build_intersphinx_mapping_url(current_module, module):
    """
    Guess and build the documentation url for a Metwork module
    :param current_module: the current Metwork module name
    :param module: the Metwork module name (e.g. mfext, mfdata, ...)
    :return: the documentation url oof the module
    """
    current_version = get_version()
    # By default, we choose the 'release' url
    url = "http://metwork-framework.org/pub/metwork/releases/docs/release_{}/{}".format(current_version, module)
    if current_version.startswith("integration"):
        url = "http://metwork-framework.org/pub/metwork/continuous_integration/docs/integration/{}".format(module)
    elif current_version.startswith("dev"):
        # CAUTION: here we assume the version (i.e. git branch) of documentation development starts with 'dev'
        url = "{}/_build/html".format(os.path.abspath(os.path.dirname(__file__))).replace(current_module, module)

    return url


intersphinx_mapping = {
    'mfext': (build_intersphinx_mapping_url(project, 'mfext'), None),
    'mfadmin': (build_intersphinx_mapping_url(project, 'mfadmin'), None),
    'mfbase': (build_intersphinx_mapping_url(project, 'mfbase'), None),
}
