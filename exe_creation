from cx_Freeze import setup, Executable

base = None    

executables = [Executable("main.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "LooLi",
    options = options,
    version = "PRE-ALPHA",
    description = '<any description>',
    executables = executables
)
