"""

Create a script to merge contents of split files so that the first file has 1million reads the second has the same million plus another , ther third three million etc.
The files will then all have their kmers counted by jellyfish_count.

input = list of all split files. For this time ( 16/FEB/2017) I will be doing each of 8 samples individually in indiviudal files and so will use this script several times independantly but 
dont have to worry about renaming things and overwirting them. I will also run teh split command by hand  individually and not write a wrapper

In brief:1) remove new characters of file names and put the file names in a list 2) for each item in the list open that item and the oen before it and read through the item before appending each line to the item next in the list. 
                

"""




import sys


files = open(sys.argv[1])
list_of_files = [ ]

for eachfile in files:
        eachfile = eachfile.replace("\n", "")
        list_of_files.append(eachfile)
        print(list_of_files)

files.close()

for i in range (1, len(list_of_files)):
        with open(list_of_files[i], "a") as x, open(list_of_files[i-1], "r") as y:
                for each_line in y:
                        x.write(each_line)
                x.close(), y.close()

