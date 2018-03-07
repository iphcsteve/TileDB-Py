#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

# -- Imports configuration -------------------------------------------------

import os
import sys
from os.path import abspath, join, dirname

sys.path.insert(0, abspath(join(dirname(__file__))))

# -- ReadTheDocs configuration ---------------------------------------------

# Special handling on ReadTheDocs builds.
# Some of this code is from https://github.com/robotpy/robotpy-docs/blob/master/conf.py
readthedocs = os.environ.get('READTHEDOCS', None) == 'True'
rtd_version = os.environ.get('READTHEDOCS_VERSION', 'latest')
rtd_version = rtd_version if rtd_version in ['stable', 'latest'] else 'stable'

# -- Project information -----------------------------------------------------

project = 'TileDB-Py'
copyright = '2018, TileDB, Inc.'
author = 'TileDB, Inc.'

# The short X.Y version
version = '0.1'
# The full version, including alpha/beta/rc tags
release = '0.1.0'


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
]

# Mapping for linking between RTD subprojects.
if readthedocs:
    intersphinx_mapping = {
        'tiledb': ('https://tiledb-inc-tiledb.readthedocs-hosted.com/en/%s/' % rtd_version, None),
        'tiledb-py': ('https://tiledb-inc-tiledb.readthedocs-hosted.com/projects/python-api/en/%s/' % rtd_version, None),
        'python': ('https://docs.python.org/', None)
    }

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'friendly'


# -- Options for HTML output -------------------------------------------------

html_static_path = ['_static']
html_logo = '_static/tileDB_uppercase_600_112.png'
html_favicon = '_static/favicon.ico'

if readthedocs:
    html_theme = 'default'
else:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'TileDB-Pydoc'


# -- Options for LaTeX output ------------------------------------------------

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
    (master_doc, 'TileDB-Py.tex', 'TileDB-Py Documentation',
     'TileDB, Inc.', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'tiledb-py', 'TileDB-Py Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'TileDB-Py', 'TileDB-Py Documentation',
     author, 'TileDB-Py', 'One line description of project.',
     'Miscellaneous'),
]

# -- Custom Document processing ----------------------------------------------

# Generate the sidebar automatically so that it is identical across all subprojects.
# This (and gensidebar.py) from https://github.com/robotpy/robotpy-docs
import gensidebar
gensidebar.generate_sidebar({'on_rtd': readthedocs, 'rtd_version': rtd_version}, 'tiledb-py')

# -- Custom setup -----------------------------------------------------------

def setup(app):
    app.add_stylesheet('custom.css')