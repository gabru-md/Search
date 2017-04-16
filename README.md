# Search
Recursive File/Folder Searching Python Script

# Softwares and Libraries
1. Python 2.7
2. OS Module

# Introduction
This Search Program allows the user to search for File/Folder. The File/Folder to be searched for must be specified
as well as the PATH to be searched.
This Script/Program ( whatever you may call ) uses Recursive Directory Listing ( I just made that up :P ) that
allows faster execution of the program. 

# Working of the Script
1. Script opens up the directory list using os.listdir(PATH)
2. Searches for the File/Folder
  1. If Folder/File is found! --> Prints out the Directory + FILENAME/FOLDERNAME
3. Enters the next directory which is not listed under visitedDirectory[]
  1. If a FILE is encountered, which cannot be TRAVERSED ( :P ) it recognises it and CONTINUES the process.
4. Continues until all the Folders/Directories in the PATH are Traversed.
5. Ends and PRINT the length of searchResults[] 

# License
  MIT License
  Copyright (c) 2017 Manish Devgan
  
 # gabru-md 

