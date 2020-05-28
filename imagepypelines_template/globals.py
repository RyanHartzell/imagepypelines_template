# ==============================================================================
# these are optional to replace, but good practice
# ==============================================================================

# update this if you add more variables to this file
__all__ = ['__version__',
            '__author__',
            '__email__',
            '__description__',
            '__version__']

################################ DIST Variables ################################
# replace this with your version number (optional)
__version__ = "0.0.0"

# your name(s) and email(s)
__author__ = ""
__email__ = ""

# one line description of your plugin
__description__ = ""

# the type of license you use e.g. "MIT"
__license__ = ""


################# Variables to modify ImagePypelines behavior ##################
# Modify this variable if you want Pipelines to do shape checking on custom
# this should be a dictionary with your new type as the key, and a function that
# returns a tuple of its shape as the value
SHAPE_FUNCS = {}
# by default, numpy.ndarray, int, float, list, tuple, str, dict are all supported

# Modify this variable to add support for homogenus containers.
# this should be a list or tuple of container types
# Homogenus containers are data containers where every datum is the same
# shape and type. For example, every row of a numpy array has the same shape, so
# there is no reason to perform shape checking on every datum - only the first
# row. A numpy array is homogenus.
# A list, where every element can be a different shape/type, is inhomogenus.
HOMOGENUS_CONTAINERS = []
