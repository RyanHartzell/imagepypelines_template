========================
imagepypelines_template
========================

How to make an ImagePypelines Plugin
====================================

1. clone this project
    '''git clone <ryan insert clone link>'''

2. rename the 'imagepypelines_template' directories to the name of your project

3. edit the DIRECTORY_NAME and NAMESPACE variables in setup.py

4. Put a license in the LICENSE file.
    - see https://choosealicense.com/licenses/ for help

5. Add the names of dependencies you need (e.g. numpy or scipy) in requirements.txt
    - each dependency should be it's own line
    - you can optionally specify the version you need as well
    - e.g. `numpy>=1.14`

5. If you need to ship data with your project (for examples or tests):
    - Put your files in the data directory. It will be automatically included
    - see `__init.__.py` to see how to fetch the filenames at runtime

6. Start coding!

7. import your code in `__init__.py`

8. open a terminal and run `python setup.py install` to install!

9. test an import with imagepypelines!
    - ```python -c "import imagepypelines as ip; ip.require('your_plugin_namespace')"```


How to upload your plugin pypi so other people can install it with pip
----------------------------------------------------------------------
*Note*: This is a super quick guide, for more help see `https://packaging.python.org/tutorials/packaging-projects/`_

1. install some quick dependencies
```pip install twine wheel```

2. create the necessary dists using setup.py
```python setup.py sdist bdist_wheel```


6. if everything worked, then upload it to pypi!
```twine upload dist/*```


Other information
=================
If you need help working with rst files, please see this helpful guide
`<https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html>`_
