import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('teachcom_v2.py', base=base, icon="logo_teachccom.ico")
]

setup(name= 'TCE App V2',
    version= '0.1',
    description= 'TCE Launcher',
    executables=executables
)