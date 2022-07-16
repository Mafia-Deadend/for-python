
# #Loops
# Practice 

#to print a table of multiplication for the number entered by the user
# num = int(input("input the number of which you want the table"))
# for i in range(1,11):
#     print( str(num)," x ",str(i)," = ",str(i*num))


#problem2::: to print those names starting with H in a list saying greetings to them
# l1 = ["Harry", "Sajjad", "Shubham", "Sarim", "Hammad"]


# for name in l1:
  
#     if name.startswith("H"):
#       print("Assalam alaikom " , name)


#problem3 solving problem 1 using while loop  
# i=0
# num = int(input("enter the number you want the table"))
# while i<10:
    
#      i=i+1
#      print(str(num),"x",str(i),"="  ,str(i*num))


# #problem4 to check whether the given number is  a prime or not
 
# num = int(input("input the number : "))
# prime = True

# for i in range(2,num):
#     if(num%i == 0):
#         prime = False
#         break
# if prime :
#     print("The number is prime")
# else:
#     print("The number is not a prime")



#problem5 to find the sum of the first 10 Natural numbers


Nat = [1,2,3,4,5,6,7,8,9,10,11]
i=0
while i<10:
    
      n=i
      i=i+1
   
      sum = Nat[n]+Nat[i] 
      Nat[i] = sum
       
      print(sum)



#problem 6 



# num = int(input("write the number to find factorial  : "))
# factorial= 1
# for i in range(1,num+1):
#     factorial = factorial*i
# print("The factorial of",num," is ",factorial )
    




# #while LOOP
# a=int(input("enter a value less than 10','asd"))
# while (a<10):
#     print(a)
#     a=a+1
# print("your value is greater than 10")  
# # ////////////////////////////////
# # For LOOP
# b=['apples','bannas','mangoes','kellas', 'asdsa', 'sadsa', 'dasd', 'asdas']
# for i in range (1,2,7):
#     print(b[i])
#     i=i+1 
#     i+=1