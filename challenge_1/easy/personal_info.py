#!/usr/bin/env python

name = raw_input("What is your name? ")
age = raw_input("What is your age? ")
user_name = raw_input("What is your reddit user name? ")

info = "Your name is {}, you are {} years old, and your reddit username is: {}".format(name, age, user_name)
print info

target = open("user_info.txt", 'w')

target.write(info)
target.write("\n")
target.close()
