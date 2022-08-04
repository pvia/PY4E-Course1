# Write a program to prompt the user for hours and rate per hour
# using input to compute gross pay. Pay the hourly rate for the hours
# up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.

hrs=input('Enter hours: ')
rate=input('Enter rate: ')
h=float(hrs)
r=float(rate)
if h <= 40 :
   print(h*r)
else :
   print(40*r+(h-40)*r*1.5)
