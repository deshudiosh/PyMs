fn run = (
	app = "D:\GitHub\PyMs.exe"
	cmd = ""
	xxx = DOSCommand (app + cmd)
	print xxx
	dir = "D:\\GitHub\PyMs\\kutas\\"
	makeDir dir
	
	str = "pause"
	hiddendoscommand str startpath:"$max" exitCode:&exitcode
)

clearlistener()
run()