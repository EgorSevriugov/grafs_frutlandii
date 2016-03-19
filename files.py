import sys
param = sys.argv
if len(param) > 1:
	param[:] = param[1:]
	for name in param:
		files = open(name,"r")
		txt = files.read()
		print(txt)
		files.close()
else:
	print("Too small numbers")
