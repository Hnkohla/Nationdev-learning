# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'Nationdev Learning'
copyright = '2025, Hnkohla'
author = 'Hnkohla'

# -- General configuration ---------------------------------------------------
import os
import sys
import django
from django.conf import settings

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath('../..'))

# Configure Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'nationdev.settings'
django.setup()

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