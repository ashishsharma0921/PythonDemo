'''
Created on Oct 14, 2016
 
@author: ashish.sharma2
'''
# import os
# from google.appengine.ext import vendor

"""This file is loaded when starting a new application instance."""
import sys
import os.path

# add `lib` subdirectory to `sys.path`, so our `main` module can load
# third-party libraries.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))
from gcloud import datastore
 
# Add any libraries installed in the "lib" folder.
# vendor.add(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib'))


 
 


