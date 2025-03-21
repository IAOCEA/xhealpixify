import datetime as dt

project = "xhealpixify"
author = f"{project} developers"
initial_year = "2023"
year = dt.datetime.now().year
copyright = f"{initial_year}-{year}, {author}"

extensions = [
    "sphinx.ext.autosummary",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    # "sphinx.ext.doctest",
    # "autoapi.extension",
    "sphinx_copybutton",
    "myst_parser",
    "nbsphinx",
    "sphinx.ext.intersphinx",
    "nbsphinx_link",
    "sphinx_remove_toctrees",
]

napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_use_param = False
napoleon_use_rtype = False
napoleon_preprocess_types = True
napoleon_type_aliases = {
    # general terms
    "sequence": ":term:`sequence`",
    "iterable": ":term:`iterable`",
    "callable": ":term:`callable`",
    "dict_like": ":term:`dict-like <mapping>`",
    "dict-like": ":term:`dict-like <mapping>`",
    "path-like": ":term:`path-like <path-like object>`",
    "mapping": ":term:`mapping`",
    "file-like": ":term:`file-like <file-like object>`",
    "any": ":py:class:`any <object>`",
    # numpy terms
    "array_like": ":term:`array_like`",
    "array-like": ":term:`array-like <array_like>`",
    "scalar": ":term:`scalar`",
    "array": ":term:`array`",
    "hashable": ":term:`hashable <name>`",
}

autosummary_generate = True
autosummary_imported_members = False
nbsphinx_execute = "never"

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", ".ipynb_checkpoints"]
remove_from_toctrees = ["generated/*"]
suppress_warnings = ["config.cache"]

html_theme = "sphinx_book_theme"
pygments_style = "sphinx"

html_static_path = []

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "xarray": ("https://docs.xarray.dev/en/latest", None),
    "pandas": ("https://pandas.pydata.org/docs/", None),
}
