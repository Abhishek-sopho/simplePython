#!/usr/bin/env python2.7

print "This is the start message"
#creating a list with name x
x=[1,2,3,4,5]
print 'x has:'
for i in x:
    print i,
print

print "changing x[1] to 4"
if(x[1]==2):
    x[1]=4

print x[1]

print "Another list y:"
#created a list of strings y
y=['a','b']

print y
#used * operator on y to see its effect
y=y*2

print y
