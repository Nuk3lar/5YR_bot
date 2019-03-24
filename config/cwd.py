# Modules

import os
import sys

# Determines the system type when posting Images and Videos

if sys.platform == "linux": cwdmain = os.getenv('PWD')
elif sys.platform == "win32": cwdmain = os.getcwd()
    