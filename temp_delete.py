import os,getpass, subprocess, win32api, shutil

username = getpass.getuser()
npath = r"C:\Users\{}\AppData\Local\Temp".format(username)
# subprocess.call('explorer "{}'.format(npath))

for content in os.listdir(npath):
	# print(content)
	try:
		os.remove((os.path.join(npath,content)))
	except:
		pass

	try:
		os.rmdir((os.path.join(npath,content)))
	except:
		pass

	try:
		shutil.rmtree((os.path.join(npath,content)))
	except:
		pass
		
win32api.MessageBox(0,"Unnecessary temp files deleted.","Success!")