# Imports
import os
import time
import shutil
import patoolib
import datetime
import tkinter as tk
from tkinter import filedialog

folder_names = ['Images/', 'Text/', 'Applications/', 'Audio/', 'Videos/', 'Compressed/']

root = tk.Tk()
root.withdraw()
path = filedialog.askdirectory()

# Sort function
def sort():
	# Variables
	names = os.listdir(path)
	dt=datetime.datetime.now()
	filesmoved = 0
	directoriescreated = 0
	directoriesremoved = 0
	for files in names:

		if '.jpg' in files or '.png' in files or '.gif' in files or '.ico' in files:
			if not os.path.exists(path+folder_names[0]):
				os.makedirs(path+folder_names[0])
				directoriescreated += 1
			if not os.path.exists(path+folder_names[0]+files):
				shutil.move(path+files, path+folder_names[0]+files)
				filesmoved += 1

		if '.txt' in files:
			if not os.path.exists(path+folder_names[1]):
				os.makedirs(path+folder_names[1])
				directoriescreated += 1
			if not os.path.exists(path+folder_names[1]+files):
				shutil.move(path+files, path+folder_names[1]+files)
				filesmoved += 1

		if '.exe' in files or '.msi' in files:
			if not os.path.exists(path+folder_names[2]):
				os.makedirs(path+folder_names[2])
				directoriescreated += 1
			if not os.path.exists(path+folder_names[2]+files):
				shutil.move(path+files, path+folder_names[2]+files)
				filesmoved += 1

		if '.mp3' in files or '.wav' in files or '.ogg' in files:
			if not os.path.exists(path+folder_names[3]):
				os.makedirs(path+folder_names[3])
				directoriescreated += 1
			if not os.path.exists(path+folder_names[3]+files):
				shutil.move(path+files, path+folder_names[3]+files)
				filesmoved += 1

		if '.mp4' in files or '.mov' in files or '.wmv' in files:
			if not os.path.exists(path+folder_names[4]):
				os.makedirs(path+folder_names[4])
				directoriescreated += 1
			if not os.path.exists(path+folder_names[4]+files):
				shutil.move(path+files, path+folder_names[4]+files)
				filesmoved += 1

		if '.zip' in files or '.rar' in files or '.7z' in files:
			filename = files
			if '.zip' in filename:
				filename=filename.replace('.zip', '')
			if '.rar' in filename:
				filename=filename.replace('.rar', '')
			if '.7z' in filename:
				filename=filename.replace('.7z', '')
			if not os.path.exists(path+folder_names[5]):
				os.makedirs(path+folder_names[5])
				directoriescreated += 1
			if not os.path.exists(path+folder_names[5]+files):
				shutil.move(path+files, path+folder_names[5]+files)
				if not os.path.exists(path+folder_names[5]+filename):
					os.makedirs(path+folder_names[5]+filename)
				patoolib.extract_archive(path+folder_names[5]+files, outdir=path+folder_names[5]+filename)
				if os.path.exists(path+folder_names[5]+files):
					os.remove(path+folder_names[5]+files)
				filesmoved += 1

	# Removing empty folders
	if os.path.exists(path+folder_names[0]):
		if not os.listdir(path+folder_names[0]):
			os.rmdir(path+folder_names[0])
			directoriesremoved += 1

	if os.path.exists(path+folder_names[1]):
		if not os.listdir(path+folder_names[1]):
			os.rmdir(path+folder_names[1])
			directoriesremoved += 1

	if os.path.exists(path+folder_names[2]):
		if not os.listdir(path+folder_names[2]):
			os.rmdir(path+folder_names[2])
			directoriesremoved += 1

	if os.path.exists(path+folder_names[3]):
		if not os.listdir(path+folder_names[3]):
			os.rmdir(path+folder_names[3])
			directoriesremoved += 1

	if os.path.exists(path+folder_names[4]):
		if not os.listdir(path+folder_names[4]):
			os.rmdir(path+folder_names[4])
			directoriesremoved += 1

	if os.path.exists(path+folder_names[5]):
		if not os.listdir(path+folder_names[5]):
			os.rmdir(path+folder_names[5])
			directoriesremoved += 1

	# Debug console
	# Remove quotes to use
	"""print('ran at '+dt.strftime("%Y_%m_%d %H:%M:%S"))
	if filesmoved == 1:
		print(str(filesmoved) + ' file moved')
	else:
		print(str(filesmoved) + ' files moved')
	if directoriescreated == 1:
		print(str(directoriescreated) + ' directory created')
	else:
		print(str(directoriescreated) + ' directories created')
	if filesmoved == 1:
		print(str(directoriesremoved) + ' directory removed')
	else:
		print(str(directoriesremoved) + ' directories removed')
	print('')
	"""

# Loop
while 1:
	sort()
	time.sleep(5)
