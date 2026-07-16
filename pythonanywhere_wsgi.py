# ============================================================
# PythonAnywhere WSGI configuration file
# ============================================================
# On PythonAnywhere, go to the "Web" tab -> click your WSGI
# configuration file link -> DELETE everything in it -> paste
# this in, editing the two values marked below.
# ============================================================

import sys

# 1. Set this to the path where you uploaded/cloned the project.
#    e.g. '/home/yourusername/portfolio_site'
project_home = '/home/yourusername/portfolio_site'

if project_home not in sys.path:
    sys.path.insert(0, project_home)

# 2. Import the Flask app object. This must be called "application"
#    for PythonAnywhere to find it.
from app import app as application
