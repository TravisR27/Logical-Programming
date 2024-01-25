# This task i will show to make a if,elif,else statement in logical order.

# List of the different symbols you will use and meanings of Boolean code and Operators
# == This means Equal to
# >= This means Greater than/equal to >/>=
# <= This means Less than/equal to </<=
# != This means Not equal to
# + which add values on either side
# (And) which is a conjunction operation which determines whether the statement is true

# This will ask the user to enter there swimming time in minutes
swim = int(input("Enter time taken for swimming in minutes: "))
print("Time taken for Swimming task:", swim)

# This will ask the user to enter there cycling time in minutes
cycle = int(input("Enter time taken for Cycling in minutes: "))
print("Time taken for Cycling task:", cycle)

# This will ask the user to enter there running time in minutes
run = int(input("Enter time taken for Running in minutes: "))
print("Time taken for Running task:", run)

# This is my variable in adding all the above conditions to get the total time taken
total_time = swim+cycle+run
print("Total time taken for Triathlon",total_time)

# The if condition is the total time is between 0 and 100 print the message "provincial colors"
if total_time >0 and total_time <=100:
    print("Provincial Colors")

# This elif condition is if time is between 100-105 print "provincial half colors"
elif total_time > 100 and total_time <=105:
    print("Provincial Half Colors")

# The elif condition stating if the total time is >= 106 and <= equal to 110 print the message "provincial scroll"
elif total_time >= 106 and total_time <=110:
    print("Provincial Scroll")

# The else condition will apply if all the above conditions are all False
else:
    print("No Award")
# Output message of No Award printed if all conditions are not met.