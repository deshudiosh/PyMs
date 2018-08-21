call "./venv/Scripts/activate"
pyinstaller pyms_debug.spec ^
	--onedir ^
	--log-level INFO ^
	--clean ^
	--debug
pause