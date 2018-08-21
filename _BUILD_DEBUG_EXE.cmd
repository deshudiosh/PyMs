call "./venv/Scripts/activate"
pyinstaller ^
	--onefile ^
	--log-level INFO ^
	--clean ^
	--debug ^
	pyms_debug.spec
pause