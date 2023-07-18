import sys
from cx_Freeze import setup, Executable

target_script = "GUI.py"

# Create an instance of the Executable class
executable = Executable(
    script=target_script,
    base="Win32GUI",  # "Win32GUI" for a GUI application on Windows
    icon=None
)

# Define additional options for the setup
options = {
    "build_exe": {
        "includes": ["tkinter", "serial"],
    }
}

# Function to create the executable
setup(
    name="Shuttling GUI",
    version="1.0",
    description="Controls segmented electrode voltage through an Arduino",
    executables=[executable],
    options=options
)
