# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Nonhermitian - Homepage'
copyright = '2021, Paul Nation'
author = 'Paul Nation'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "ablog",
    "myst_nb",
    "sphinx_panels",
    "sphinxcontrib.bibtex",
]

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_image",
]

jupyter_execute_notebooks = "off"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store',
                    "*import_posts*",
                    "**/pandoc_ipynb/inputs/*",
                    '**.ipynb_checkpoints']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

html_theme_options = {
  "github_url": "https://github.com/nonhermitian",
  "search_bar_text": "Search ...",
  "navbar_end": ["search-field.html", "navbar-icon-links"],
}

html_favicon = "_static/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_extra_path = ["feed.xml"]
html_sidebars = {
    "index": ["hello.html"],
    "about": ["hello.html"],
    "cv": ["hello.html"],
    "publications": ["hello.html"],
    "projects": ["hello.html"],
    "talks": ["hello.html"],
    "posts/**": ['ablog/postcard.html', 'download.html',
                 'ablog/recentposts.html', 'ablog/archives.html'],
    "blog": ["hello.html", "ablog/categories.html", 'ablog/tagcloud.html', 'ablog/archives.html'],

}
blog_baseurl = "nonhermitian.org"
blog_title = "Paul Nation's Blog"
blog_path = "blog"
fontawesome_included = True
blog_post_pattern = "posts/*/*"
post_redirect_refresh = 1
post_auto_image = 1
post_auto_excerpt = 2

# Panels config
panels_add_bootstrap_css = False


# Bibliography and citations
bibtex_bibfiles = ["_static/papers.bib"]

html_logo = "_static/logo.png"


def setup(app):
    app.add_css_file("custom.css")
