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


def open_file(path):
    if platform.system() == "Windows":
        os.startfile(path)



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
	print "Search Completed"
	getResults()
	#for Results in searchResults:
		#print Results
	#os.chdir("C:\Users\Manish\Desktop\desktop.ini")
