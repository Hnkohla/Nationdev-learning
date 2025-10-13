# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'Nationdev Learning'
copyright = '2025, Hnkohla'
author = 'Hnkohla'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon'
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']