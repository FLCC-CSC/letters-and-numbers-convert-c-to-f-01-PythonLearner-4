# FILE NAME - convert_C_to_F_01.py

# NAME: Michael Orcutt
# DATE: 2/14/2025
# BRIEF DESCRIPTION: A program to convert Celsius to Farenheit 



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions below
# 4. The Sample Output has been included in this code for your convenience




    
# Don't forget to cast user input as a float!
    
########## ENTER YER CODE BELOW THIS LINE ##########



    
def convert_c_to_f():
    C = float(input("\nEnter a temperature in Celsius: "))
    F = C * 9 / 5 + 32
    print(f'\n{C} degrees Celsius is {F} degrees Fahrenheit.\n') 

convert_c_to_f()

########### END YER CODE ABOVE THIS LINE ###########





########################################
#          SAMPLE OUTPUT
########################################

'''

Enter a temperature in Celsius: 100

100.0 degrees Celsius is 212.0 degrees Fahrenheit.

'''



'''

Enter a temperature in Celsius: -40

-40.0 degrees Celsius is -40.0 degrees Fahrenheit.

'''



'''

Enter a temperature in Celsius: 1

1 degrees Celsius is 33.8 degrees Fahrenheit.

'''



########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What does `float` mean?

float defines a floating point number ( a number with one decimal place ) to work with more precision.



2. Why do you think it is important to use `float` as opposed to
   a different type of variable type?

It is important to use float when working with temperatures because the scale of temperatures are quite different. Celsius uses a smaller range of numbers to refer to temperatures that are referred to by a much larger range of numbers so one number converted to celsius might be inaccurate by several degrees due to rounding.



'''
