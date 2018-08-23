fn run = (
	startpath = "D:\\GitHub\\PyMs\\"
	app = "PyMs.exe"
	file = "assets/VrayZdepthCalculator_RGBA.exr"
	command = app + " " + file
		
	hiddendoscommand command startpath:startpath exitCode:&exitcode
	print ((getINISetting (startpath+"PyMs.ini") "VRAY_DEPTH_CALC" "min") as number)
)

clearlistener()
run()