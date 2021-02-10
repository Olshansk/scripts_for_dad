import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["pandas", "numpy", "glob", "openpyxl"],
    "excludes": ["xz", "liblzma", "pyliblzma"]
    # "packages": ["glob"],
    # "includes": []
}

base = 'Win32GUI' if sys.platform=='win32' else None

setup(  name = "ProgramGUI",
        version = "0.1",
        description = "Script for dad!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("dir_to_sheets.py", base=base)])
