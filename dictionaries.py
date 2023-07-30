# dictionary like as an array object key pair value exist.
#  it start with {}

myDictionary = {'firstName': 'Ayub','lastName' : 'Ali',"age": "29", "profession":"Web App Developer"}

print( f"My full name is, { myDictionary['firstName'] } {myDictionary['lastName']}")
# here f is f-string which is used in begenning before start a string to access any properties properties into a string using {} bracket.

# nested dictionary
details = {'fullName' : 'Md Ayub Ali', 'company':'codecracky', 'employee': {"total": 200, "avSallary":30000, "shif": 'Day','size':[100,200,300]}}
print(details['employee']['size'][2])

# in an dictionary you will be able to write array also.
