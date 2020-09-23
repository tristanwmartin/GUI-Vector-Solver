# Sine, Cosine, Tangent (SOH CAH TOA)
'''
math.sin(x) returns sine of x radians
math.cos(x) returns cosine of x radians
math.tan(x) returns tangent of x radians

math.degrees(x) converst angle x from radians to degrees
math.radians(x) converts angle x from degrees to radians
'''

#imports
import math

#define pi
pi=3.14159265359

#tkinter gui test
import tkinter as tk
# Following packages are probably unneccesary but were included for sake of future expansion of this GUI
from tkinter import *
from tkinter.messagebox import *



def reset ():                   # Reset function which clears all entry fields
    num1.delete(0, 'end')
    num2.delete(0, 'end')
    num3.delete(0, 'end')
    num4.delete(0, 'end')
    blank.delete(0, 'end')
    blank2.delete(0, 'end')
    blank3.delete(0, 'end')
    blank4.delete(0, 'end')
    xsum.delete(0, 'end')
    ysum.delete(0, 'end')
    resultant.delete(0, 'end')
    r_angle.delete(0, 'end')
    
def show_answer():              # Logic for calculating components as well as displaying them in fields
    blank.delete(0, 'end')
    blank2.delete(0, 'end')
    blank3.delete(0, 'end')
    blank4.delete(0, 'end')
    xsum.delete(0, 'end')
    ysum.delete(0, 'end')       
    resultant.delete(0, 'end')  # Ensure all fields are cleared before doing operations    
    magnitude1= float(num1.get())
    theta1= float(num2.get())
    Mx1 = magnitude1 * math.cos(math.radians(theta1))
    My1 = magnitude1 * math.sin(math.radians(theta1))
    blank.insert(0, round(Mx1, 2))          # insert result into field
    blank2.insert(0, round(My1, 2))         # ''
    magnitude2 = float(num3.get())          
    theta2 = float(num4.get())
    Mx2 = magnitude2 * math.cos(math.radians(theta2))
    My2 = magnitude2 * math.sin(math.radians(theta2))
    blank3.insert(0, round(Mx2, 2))
    blank4.insert(0, round(My2, 2))
    xsum.insert(0, round(Mx1 + Mx2, 2))
    ysum.insert(0, round(My1 + My2, 2))
    resultant.insert(0, (math.sqrt(((float(xsum.get())) ** 2) + ((float(ysum.get())) ** 2)), 2))
    r_angle.insert(0, (math.atan((float(ysum.get()) / float(xsum.get())))) * (180/pi))

def add_vector2():
    Label(main, text = "Vector 2 Magnitude:").grid(row=0, column=2)
    Label(main, text = "Vector 2 Angle:").grid(row=1, column=2)
    Label(main, font=("Calibri", 8, "italic"), fg="grey", text = "(Measure from the same point of reference)").grid(row=2, column=2)
    Label(main, relief=RIDGE, width=20, pady=5, text = "The X\N{SUBSCRIPT TWO} Component is:").grid(row=3, column=2)
    Label(main, relief=RIDGE, width=20, pady=5, text = "The Y\N{SUBSCRIPT TWO} Component is:").grid(row=4, column=2)
    num3.grid(row=0, column=3)
    num4.grid(row=1, column=3)
    blank3.grid(row=3, column=3)
    blank4.grid(row=4, column=3)
    xsum.grid(row=7, column=3)
    ysum.grid(row=8, column=3)
    resultant.grid(row=9, column=3)
    r_angle.grid(row=10, column=3)
    Label(main, text = "Sum of X Components:").grid(row=7, column=2)
    Label(main, text = "Sum of Y Components:").grid(row=8, column=2)
    Label(main, text = "Resultant Magnitude:").grid(row=9, column=2)
    Label(main, text = "Resultant Angle (degrees):").grid(row=10, column=2)


main = Tk()
Label(main, anchor="e", text = "Vector 1 Magnitude:").grid(row=0)
Label(main, anchor="e", text = "Vector 1 Angle:").grid(row=1)
Label(main, relief=RIDGE, width=20, pady=5, text= "X\N{SUBSCRIPT ONE} Component =").grid(row=3)
Label(main, relief=RIDGE, width=20, pady=5, text = "Y\N{SUBSCRIPT ONE} Component =").grid(row=4)

# Instantiate all fields for Vector 1
num1 = Entry(main)
num2 = Entry(main)
num3 = Entry(main)
num4 = Entry(main)
blank = Entry(main)
blank2 = Entry(main)
blank3 = Entry(main)
blank4 = Entry(main)
xsum = Entry(main)
ysum = Entry(main)
resultant = Entry(main)
r_angle = Entry(main)


num1.grid(row=0, column=1)
num2.grid(row=1, column=1)
main.grid_rowconfigure(2, minsize=20)
blank.grid(row=3, column=1)
blank2.grid(row=4, column=1)

Button(main, text='Quit', command=main.destroy).grid(row=7, column=0, sticky=W, pady=10)
Button(main, width=10, height=5, text='Solve', command=show_answer).grid(row=6, column=1, sticky=W, pady=3)
Button(main, width=10, text='Reset', command=reset, fg="red").grid(row=7, column=1, sticky=W, pady=0)
addbutton = Button(main, text='++Vector 2', command=add_vector2, fg="blue").grid(row=6, column=2, sticky=W, pady=10)


main.title("Vector Solver 9000") 
mainloop()

''' # Legacy version of this program which is used within the Python IDLE

#Get Magnitude and Angle input
print('\nVECTOR SOLVER\n')
print('Vector 1:')
magnitude1 = float(input('Input Magnitude of Vector 1:\n'))
theta1 = float(input('Input Angle 1 in degrees:\n'))
print('Vector 2:')
magnitude2 = float(input('Input Magnitude of Vector 2:\n'))
theta2 = float(input('Input Angle 2 in degrees:\n'))
print('Vector 3:')
magnitude3 = float(input('Input Magnitude of Vector 3:\n'))
theta3 = float(input('Input Angle 3 in degrees:\n'))

#Calculate x and y components using trig

Mx1 = magnitude1 * math.cos(math.radians(theta1))
My1 = magnitude1 * math.sin(math.radians(theta1))
print('X1 component =', round(Mx1, 1),'\nY1 component =', round(My1, 1))
Mx2 = magnitude2 * math.cos(math.radians(theta2))
My2 = magnitude2 * math.sin(math.radians(theta2))
print('X2 component =', round(Mx2, 1),'\nY2 component =', round(My2, 1))
#third vector experiment
Mx3 = magnitude3 * math.cos(math.radians(theta3))
My3 = magnitude3 * math.sin(math.radians(theta3))
print('X3 component =', round(Mx3, 1),'\nY3 component =', round(My3, 1))

#Sum of x and y components

sum_mx = Mx1 + Mx2 + Mx3
sum_my = My1 + My2 + My3
resultant = math.sqrt(((sum_mx) ** 2) + ((sum_my) ** 2))
print('The resultant is', round(resultant, 3))
resultant_angle = (math.atan((sum_my / sum_mx))) * (180/pi)
print('The resultant angle is', resultant_angle)

'''
