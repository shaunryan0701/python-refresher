# -- importing --

from mymodule import divide

print(divide(10, 2))

# -- __name__ --

# will print __main__ only from the file being run

print(__name__)

# -- importing with names --

import mymodule

print("code.py: ", __name__)

# How does Python know where `mymodule` is?
# Answer, it looks at the paths in sys.path in order:

import sys

print(sys.path)

# The first path is the folder containing the file that you ran.
# The second path is the environment variable PYTHONPATH, if it is set.
# We won't cover environment variables in depth here, but they are variables you can set in your operating system. It can help Python find things to import when the folder structure is ambiguous.

# -- circular imports --
# Make mymodule.py import code.py as well.

# -- importing from a folder --

import mymodule

print("code.py: ", __name__)

import sys

# Using the sys module to see what modules are currently loaded
# This is a dictionary where the keys are the module names and the values are the modules themselves.
# This is how Python keeps track of what has been imported.
# This is useful for debugging, but it's also useful for understanding how Python handles imports.
# It's a good way to see what is going on under the hood.
# It's also a good way to see if a module has already been imported, so you don't import it again.
# This is important because importing a module can be a slow operation.
# If you import a module multiple times, it can slow down your program.
# This is especially true if the module does a lot of work when it is imported.

print(sys.modules)
