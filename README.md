# Search
Recursive File/Folder Searching Python Script

# Softwares and Libraries
1. Python 2.7
2. OS Module
3. SYS Module
4. PLATFORM Module
5. SUBPROCESS Module ( idk why :P )

# Introduction
This Search Program allows the user to search for File/Folder. The File/Folder to be searched for must be specified
as well as the PATH to be searched.<br>
This Script/Program ( whatever you may call ) uses Recursive Directory Listing ( I just made that up :P ) that
allows faster execution of the program. 

# Working of the Script
1. Script opens up the directory list using os.listdir(PATH)
2. Searches for the File/Folder
3. If Folder/File is found! --> Prints out the Directory + FILENAME/FOLDERNAME
4. Enters the next directory which is not listed under visitedDirectory[]
5. If a FILE is encountered, which cannot be TRAVERSED ( :P ) it recognises it and CONTINUES the process.
6. Continues until all the Folders/Directories in the PATH are Traversed.
7. PRINTS the results on screen with individual INDICES.
8. Prompts the user for INDEX to open the Branch. (Enter '0' to exit the script)
9. Program ENDS if the INDEX is valid and opens it.

# Script
1. searchDir.py - Initial Python Script to to basic task
2. searchDir_v2.py - Updated Python Script to open the requested Result

# Updated
First Update : 16 April 2017 Time: 09:51 PM IST<br>

# License
  MIT License
  Copyright (c) 2017 Manish Devgan
  
 # gabru-md 

