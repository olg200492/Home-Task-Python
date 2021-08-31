l = [["name", "dinner"], ["Abraham", "Avi"], ["Hello", "Tree", "Door"], ["Name",
"Glass", "Two", "am"]]
#Unify all the sub lists to a one bigger list.
l=sum(l,[])
#1.Capitalize each string in the list
#2.Utilizing set built in data type in Python to remove duplicates
#3.Convorting to list
l = (list(set(map(lambda x:x.capitalize(), l))))
#4.Printing only strings len is equel or larger then 5(they have more then 2 characters in the middle of them)
print (list(filter(lambda str:len(str)>=5,l)))


