# Resources

## Columbia research computing course

- https://github.com/rabernat/research_computing_2018.git

- formatted https://rabernat.github.io/research_computing_2018/

## Whirlwind tour of python

- https://github.com/jakevdp/WhirlwindTourOfPython

- formatted https://jakevdp.github.io/WhirlwindTourOfPython/index.html

## Python data science handbook

- https://jakevdp.github.io/PythonDataScienceHandbook/

- https://github.com/jakevdp/PythonDataScienceHandbook


# Installation

* `conda env create -f setup/environment.yml` to create environment

* copy Modis file from https://www.dropbox.com/sh/mfsmf2vpqenohg9/AADkmt_ijKDexoMUOKUeCbDpa?dl=0
  into datadir

* edit `~/.jupyter/jupyter_notebook_config.py` to add these lines:


```

# NotebookApp(JupyterApp) configuration
# ------------------------------------------------------------------------------

## Set the Access-Control-Allow-Credentials: true header
c.NotebookApp.allow_credentials = False
c.NotebookApp.browser = u"chrome"  # noqa
c.NotebookApp.contents_manager_class = "jupytext.TextFileContentsManager"  # noqa
c.ContentsManager.preferred_jupytext_formats_save = "py:percent" # noqa
c.ContentsManager.default_jupytext_formats = "ipynb,python//py" # noqa
c.ContentsManager.default_notebook_metadata_filter = "all,-language_info"
c.ContentsManager.default_cell_metadata_filter = "all"
```


* cd to notebooks/python and start jupyter:

  `jupyter notebook`

* the notebook modis_level1b_read.py should work

