call "./venv/Scripts/activate"
pyinstaller pyms_debug.spec --onefile --log-level=DEBUG --clean --debug
pause