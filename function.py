# define the function with def keyword and function name

def my_def():
    print('Hello world')
my_def()

# return allow to save the result to a variable

def say_hello():
    return 'Hello python'
my_result = say_hello()
print (my_result)

my_list = [2,4,5,6,8,7,10,33,543]
def checker(list_to_checker):
   for num in list_to_checker:
      if(num == 10):
         return True
   return False
print(checker(my_list))
