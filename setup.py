from http.server import executable
import cx_Freeze
import sys
import os
import os.path
import main

#Dependencies
import re

base = None
if sys.platform == "win32":
    base = "Win32GUI"

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

executables = [cx_Freeze.Executables(main.py)]

cx_Freeze.Setup(
    name = "main.py",
    version = "3.10.0",
    executables = executables,
    options = {"build_exe":{"packages":["tkinter", "re"],
    'include_files':[
        os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
        os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
    ]

}}
)
