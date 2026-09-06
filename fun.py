# function:



# word="malayalam"
# print(word==word[::-1])     #reverse is true.

# if word==word[::-1]:
#     print("palindrome")
# else:                        #if the reverse and normal word is same then the function is true.
#     print("not palindrome")  #palindrom=true by using the if condition.

# def check_palindrome(word):       #def is keyword  , check_palindrome if name , word is parameter.
#     if word==word[::-1]:
#         print("palindrome")         #15 16 17 18 are code block
#     else:
#         print("not palindrome") 
# check_palindrome("malayalam")       # arguements
# check_palindrome("radar")
# check_palindrome("racecar")

# def marriage_function(bride,groom):
    # print(groom,"weds",bride)
    # print(bride,"weds",groom)
    
# marriage_function("seetha","ram")
# marriage_function("rajee","chinna")
# marriage_function("surya","roja")
# marriage_function("ramesh","pushpa")
# marriage_function("urmila","laxman")

# _----------------add numbers:---------------------

# def add_two_numbers(n1,n2):
#     print(n1+n2)
# add_two_numbers(9,2)                  #applicabile for only real values
# add_two_numbers(34,78)


# def add_three_nums(a,b,c,):
#     print(a+b+c)
# add_three_nums(2,3,4)
# add_three_nums(52,95,26)

# a=1
# b=3
# c=9
# add_three_nums(a,b,c)                #if we give the values to the variable then it will work otherwise it will not works.


# sum_of_nums:

# def sum_three_nums(a,b,c,):
#     print((a+b)/2)
# sum_three_nums(2,3,4)
# sum_three_nums(52,95,26)

# sum is even_or_odd:
# def add_two_nums(n1,n2):
#     print(n1+n2)

# s=add_two_nums(5,3)
# print(s)
# def is_even_or_odd(n):
#     if n%2==0:
#         print("even")
#     else:
#         print("odd")
# is_even_or_odd(s)


# def marriage_function(bride,groom):
#     print(bride,"weds",groom)
#     print(groom,"weds",bride)

# marriage_function("pardhu","mounik")



# reg_user_id="gnaneshwar"
# reg_password=12345

# def user_login(user_id,_password):
#     if reg_user_id==user_id and reg_password==_password:
#         return True
#     else:
#         return False

# valid=user_login("gnaneshwar",12345)
# def show_reels(is_logged_in):
#     if is_logged_in==True:
#         return("show_reels")
#     else:
#         return("plz_login_first")
# print(show_reels(valid))



# reg_user_id='Pandu'
# reg_pass="p@1234"

# def user_login(user,_password):
#     if reg_user_id==user and reg_pass==_password:
#         return True
#     else:
#         return False

# valid=user_login("Pandu","p@1234")
# def show_interface(is_login):
#     if is_login==True:
#         return(show_interface)
#     else:
#         return("login_first")
# print(show_interface(valid))

#==============================**********PARAMETERS******===============================
# function is a reusable block of code.
# param : they are variable to store the values passed.
# 
# revision:

# def revison():
#     print("revison function")
# revison()

# def wish(name):
#     print("good morning",name)
#     return("good morning",name)
# wish("kohli")
# wish("raju")
# wish("manu")
# wish("roja")
# wish("rahul")


# types of parameters:

# 1-> positional-----------------------------------------------------

# def full_name(first_name,last_name):
#     return last_name+" "+first_name
# print(full_name("vagadi","mounika"))
# print(full_name("durgam","pandu"))


#     return first_name+" "+last_name
# print(full_name("Durgam","Gnaneshwar"))
# print(full_name("Thogam","Rajeshwari"))


# 2-> default:-------------------------------------------------------

# def add_nums(a,b=0):
#     return a+b
# print(add_nums(10))

# def welcome(name="User"):
#     return "Hello +"+name
# print(welcome())

# def add_nums(a,b=-5):
#     return a+b
# print(add_nums(10))

# def add_nums(a=5,b=0):
#     return a+b
# print(add_nums(10))

# def add_nums(a=2,b=1):
#     return a+b
# print(add_nums(10))

# def pyar(name="rajeshwari"):
#     return "love you "+ name
# print(pyar())

# def excuse(value="anna"):
#     return "sorry "+value
# print(excuse())

# 3-> keyword-------------------------------------------------------

# def full_name(first_name,second_name):
#     return first_name+ "" + second_name
# print(full_name("Gnan ","Durgam"))

# def full_name(first_name,second_name):
#     return second_name + "" + first_name
# print(full_name("Gnan ","Durgam "))

# def full_name(first_name,second_name):
#     return first_name+ "" + second_name
# print(full_name(first_name="Gnan " ,second_name="Durgam"))


# 4-> *args---------------------------------------------------------
# def add_nums(*args):
#     total=0
#     for i in args:
#         total+=1
#     return total
# print(add_nums())

# def add_nums(*args):
#     total=0
#     for i in args:
#         total+=1
#     return total
# print(add_nums(45,8,65,2,6,-55,45,359+8,-44))




# 5-> **kwargs

# def detail(**kwargs):
#     return kwargs
# print(detail(name="gnan",age=25,employee=True,city="hyd",email="gnan@gmai.com"))


# def detail(**kwargs):
#     return kwargs
# print(detail(name="pandu",age=30,employee=True,city="hyd",email="pandu@gmai.com"))

# def add_nums(*args):
#     return args

# print(add_nums(15,5,6,8,4,9,5,6,3,2,7,9,4,6,3,2,1,4,5,6,2,3,1,6,4,6,1,3,1,5,6,4,1,4,9,4,56,6,1,))
# print(len(add_nums())

# def is_even(n):
#     return n%2==0
# def add_nums(a,b,c,d,fun):
#     total=a+b+c+d
#     return fun(total)
# print(add_nums(1,5,2,8,is_even))

# # higher order function(HOF):
# is a function which takes another function as a parameter/ returns another function asparamer

# # call back:
# is a function which is passed as aparameter to another function




# position
# default
# keyword
# *args
# **kwrgs
# callback
# hof

print("hi")


