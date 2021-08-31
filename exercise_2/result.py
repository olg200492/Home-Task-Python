import os
import glob
from sys import platform

"""
checking if the OS is linux or win32 to select the currect backslash for the OS 
"""

if platform.startswith('linux'):
    slash ='/'
elif platform.startswith('win32'):
    slash = '\\'
"""
getting the current working directory
"""
path = os.getcwd()
"""
creating the path for main_folder
"""
dirPhoto = path+slash+'main_folder'
"""
generating  list of tuppels of paths, folders name, files in a main_folder directory 
"""
dataList = list(os.walk(dirPhoto))
"""
filtering only path names
"""
pathList = list(set(map(lambda i:dataList[i][0],range(len(dataList)))))
"""
filtering only path names for jpg files
"""
photoList = list(filter(None,(map(lambda i:glob.glob(pathList[i]+slash+'*.jpg'),range(len(pathList))))))
"""
convorting the list of lists to one big list for easier iterating
"""
photoList = sum(photoList,[])
"""
creating list of jpg file name by tail 
"""
photoName = list(map(lambda i:os.path.basename(photoList[i]),range(len(photoList))))
print('-------------------------------------------------------------------------------------')
print('3.Names of all the pictures:')
print('\n'.join(map(str, photoName)))
print('-------------------------------------------------------------------------------------')
print('4.The numbers of all the pictures:')
print(len(photoName))
print('-------------------------------------------------------------------------------------')
print('5.The number of all the folders:')
print(len(pathList))
print('-------------------------------------------------------------------------------------')
print('6.The full paths to all the folders:')
print('\n'.join(map(str, pathList)))
print('-------------------------------------------------------------------------------------')
print('\n7.Dictionary with the key is the name of each picture is parent folder and value is a list of all of the pictures inside the parent folder.')
"""
1.creating a list of tupples,each tupple contains the path jpg file parent folder name and jpg file name
2.creating a list of tupples,each tupple contains parent folder name and the jpg file name he contains
3.filtering by using set for the keys(folders name)
4.creating a dictionary, key is folder name ,the values  are filterd and returned as a list by mapping listTupple2 items equal to key
"""
listTupple = list(map(lambda i:os.path.split(photoList[i]),range(len(photoList))))
listTupple2 = list(map(lambda i:(os.path.basename(listTupple[i][0]),listTupple[i][1]),range(len(listTupple))))
keys = list(set(map(lambda i :listTupple2[i][0],range(len(listTupple2)))))
dict = dict(map(lambda key:(key,list(map(lambda k:k[1],filter(lambda item:item[0]==key,listTupple2)))),keys))
print(dict)
print('-------------------------------------------------------------------------------------')
print('\n8.Print a filtered list with the name of the folders that contains the letter i ')
"""
creating list of file names,
filtering only names containing "i" by using find function that retuns an index if i is found or -1 if is not
"""
filesName  = list(map(lambda i:os.path.basename(pathList[i]),range(len(pathList))))
filesNameWithI = list(filter(lambda file: file.find("i") > -1, filesName))
print(filesNameWithI)
