# tuple is same to the list expcept the () sign. 
# list are muteable where tuples ase immutable. 

myList = [1,3,4,54,5, 'Md Ali Ershad']
my_tuples = (22,45,66,6,'md Ayub ali')

myList[2]=  'New value added'

# myTuples[3] = 'try to add' //will create error

print(my_tuples[4])
# using items() method you can see the actuall data type list or tuples.
print(my_tuples.items())