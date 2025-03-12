from cx_Freeze import setup, Executable

setup(
    name="MATRIX CALCULATOR",
    version="1.0",
    description="My Program",
    executables=[Executable("MATRIX_CALCULATOR.py")]
)
