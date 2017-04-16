import sys
import os


# This is a simple file browser
# List of Visited Folders
# List of Folders in the current folder / path
# Recursive calls to the next Folder


searchElement = ""
searchPath = ""
searchResults = [] 

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
			print str(newPath)
		
		try:
			if newPath not in visitedFolder:
				os.chdir(newPath)
				visitedFolder.append(str(newPath))
				recursiveFileBrowser(newPath,searchElement)
		except WindowsError:
			continue


	#print "Length of Visited Folders: " + str(len(visitedFolder))

if __name__ == "__main__":
	try:
		searchElement = str(sys.argv[1])
	except IndexError:
		searchElement = str(raw_input("Enter the Search Element: "))

	try:
		searchPath = str(sys.argv[2])
	except IndexError:
		searchPath = str(raw_input("Enter the Path to be Searched: "))

	
	recursiveFileBrowser(searchPath,searchElement)
	print len(searchResults)
	#for Results in searchResults:
		#print Results
	#os.chdir("C:\Users\Manish\Desktop\desktop.ini")
