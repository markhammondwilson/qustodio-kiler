import os, replit, psutil
replit.clear()
while True:
	for proc in psutil. process_iter(['name']):
		name = proc.info['name']
		if 'q' in name.lower():
			_ = os.system('sudo kill -9 ' + str(proc.pid))
