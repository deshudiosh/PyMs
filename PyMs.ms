fn run = (
	startpath = "D:\\GitHub\\PyMs\\"
	app = "PyMs.exe"
	cmd = "assets/VrayZdepthCalculator_RGBA.exr"
	xxx = app + " " + cmd
	print xxx
		
	str = "pause"
-- 	hiddendoscommand xxx startpath:startpath exitCode:&exitcode
	print ((getINISetting (startpath+"PyMs.ini") "VRAY_DEPTH_CALC" "min") as number)
)

clearlistener()
run()