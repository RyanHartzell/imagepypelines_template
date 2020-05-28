# If you need the filenames of data from your data directory, modify the code
# below for your specific filename(s)
import pkg_resources
DATA_DIRECTORY = pkg_resources.resource_filename(__name__, 'data')
"""data directory - the full path to the directory where data shipped with this
package is located"""
del pkg_resources

# if you want fetch specific filenames, uncomment and modify the following line:
# DATA_PATH = pkg_resources.resource_filename(__name__, 'data/<your_filename_here>')

# replace these lines with your own imports
from .blocks import ExampleBlock
from .pipelines import ExamplePipeline

# import the global variables (unused as of 04/06/20)
from .globals import *
