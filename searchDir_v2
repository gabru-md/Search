# Author	:	Manish Devgan
# Github Name	:	gabru-md
# Github Link	:	https://github.com/gabru-md
# Date		:	16 April 2017
# Updated : 16 April 2017 09:44 PM

import sys
import os
import platform
import subprocess


# This is a simple file browser
# List of Visited Folders
# List of Folders in the current folder / path
# Recursive calls to the next Folder


searchElement = ""
searchPath = ""
searchResults = [] 


def open_file():
	index = raw_input("\nEnter Index to Open (Enter 0 to Exit): ")

	if platform.system() == "Windows" and int(index) > 0:
		try:
			os.startfile(searchResults[int(index) - 1])
		except IndexError:
			print "\nIndex not found! :("
			open_file()
	elif int(index) == 0:
		sys.exit()



def recursiveFileBrowser(path,searchElement):
	visitedFolder = []
	#print path
	#raw_input()
	dirList = os.listdir(str(path))
	#print str(len(dirList)) + "\n"
	for name in dirList:
		newPath = path + "\\" + name
		#print name
		if searchElement.lower() in name.lower():
			searchResults.append(str(newPath))
			#print str(newPath)
		
		try:
			if newPath not in visitedFolder:
				os.chdir(newPath)
				visitedFolder.append(str(newPath))
				recursiveFileBrowser(newPath,searchElement)
		except WindowsError:
			continue


	#print "Length of Visited Folders: " + str(len(visitedFolder))
def getArgs():
	global searchElement
	global searchPath
	try:
		searchElement = str(sys.argv[1])
	except IndexError:
		searchElement = str(raw_input("Enter the Search Element: "))
	
	try:
		searchPath = str(sys.argv[2])
	except IndexError:
		searchPath = str(raw_input("Enter the Path to be Searched: "))



def getResults():
	i = 0
	for Results in searchResults:
		i = i + 1
		print str(i) + " : " + Results[len(searchPath):]
		


if __name__ == "__main__":
	getArgs()	
	recursiveFileBrowser(searchPath,searchElement)
	print "\nSearch Completed"
	print "\n"
	getResults()
	print "\n"
	#index = raw_input()
	open_file()
	#for Results in searchResults:
		#print Results
	#os.chdir("C:\Users\Manish\Desktop\desktop.ini")
