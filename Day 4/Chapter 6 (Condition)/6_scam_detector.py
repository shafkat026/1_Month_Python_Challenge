# A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. 
# Write a program to detect these spams.

t1="make a lot of money"
t2="buy now"
t3="subscribe this"
t4="click this"

message= input("Enter your Message:\t").lower()


if(t1 in message or t2 in message or t3 in message or t4 in message):
    print("This comment is a spam")
else:
    print("This comment is not a spam")