fn run = (
	app = "D:\GitHub\PyMs\PyMs.exe"
	cmd = ""
	xxx = DOSCommand (app + cmd)
	print xxx
		
	str = "pause"
	hiddendoscommand str startpath:"$max" exitCode:&exitcode
)

clearlistener()
run()