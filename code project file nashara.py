# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
                                      #day 1
print("hello world")#helloworld 
print("1")#numbers
print("2020")#time
print("being 17")
print('5*2=10')
print('5/2=2.5')      
print('5-2=3')
print('5^2=25')
print('8/9*3~2.6')
5*2
5/2
5-2
5^2
8/9*3
def add(a,b):
    add = a+b
    print(add)
add(4,6)    
add(9,12)
def add3(c,d,e):
    add3 = c+d+e
add3(1,2,4)
 print("the sum of"c,d,"and," e ", is =" add3 )
add3(1,1,1)   
print('the sum of' a,b, "=" , add)
add(1,2)
add3(1,2,3)#day One 
 def add33(a,b,c)
     add33(a+b+c):
         add33(1,1,1)
add(1,1)
add(1,1)
print(add)
def add(a,b):
    add= a+b
    print(add)
add(1,1)
def add(a,b):
    add = a+b
print(add)
add(1,2)    
def 
                                    #day 2

                #daY 2 #create funtion multiplication of 3 numbers
def aqua(a,b,c):
    aqua = a*b*c
    print("the product of" ,a,b, "and" ,c, "is" ,aqua)

aqua(2,1,1)

print()

#addition of 3 numbers 
def water(a,b,c):
    water = a+b+c
    print(water)
#area of Triangle 
water(1,1,1)

def area(b,h):
    area = 1/2*b*h
    print("the area of a triangle with base" ,b, "and height" ,h, "is" ,area)
    
area(2,3)   

area(35,12)   


def chocolatebox(a,b,c):
    chocolatebox = a=darkchocolateb=whitechocolatec=milkchocolate 
    print(chocolate)
    



                                 #chocolate box
chocolate1="milkchocolate"
chocolate2="darkchocolate"
chocolate3="whitechocolate"

A=5
B=8
C=6

print(chocolate1,A+3)
print(chocolate2,C+2)
print(chocolate3,B+2)



                                        #math library 
import math
dir(math)

math.factorial(7)
math.factorial(9)
math.sqrt(350)
math.pow(2.718281828459045,2)


math.exp(2)

math.pow(35,9)

math.pi

                                      #day 3 
import math

                            #dict data structure



chocolate1 = {"milk":5}
chocolate2 = {"dark":6}
chocolate3 = {"white":8}

chocolatebox = {'milk':5,"dark":6,"white":8}

chocolatebox

                                    #List


student1 = ['steve',32,'M']
student2 = ["lia",28,"F"]
student3 = ['vin',45,"M"]
student4 = ['katie',38,'F']

print(student1,student2,student3,student4)

import pandas

students = [student1,student2,student3,student4]

                                    #day 4 work


studentlist = pandas.DataFrame(students, columns = ['name','age','gender'])
print(studentlist)

studentlist['age']

import plotly                             







   #LIST WITHIN A LIST 




studentsinfo = [['steve',32,'m'],["lia",28,'f'],["vin",45,'m'],['katie',38,'f']]


studentsinfo

student1[0]

milk1 = {5:'chocolate'}
milk2 = [5,'chocolate']

milk1



                                        #importing panda



import pandas

dir(pandas)

                                    #creating a data frame

studentsclass = pandas.DataFrame(studentsinfo,columns=('name','age','gender'))

studentsclass

                                         #read data file

df = pandas.read_excel('GISdata.xlsx', sheet_name = ')

chocolatebox = {'milk':5,"dark":6}

chocolatebox1=[chocolatebox]

 
                               #creating data files
import pandas


chocolatebox

chocolateboxx = pandas.DataFrame(chocolatebox1,columns=['type','quantity'])

chocolateboxx

chocolatebox3 = pandas.DataFrame(chocolatebox2,columns=('type','quantity'))

chocolatebox3



                                    #Plotly


import plotly

dir(plotly)

from plotly.offline import plot

import plotly.graph_objs as go

studentclass = [['steve',32],["lia",28],["vin",45],['katie',38]]

studentclass1 = pandas.DataFrame(studentclass,columns=('name','age'))

studentagegraph = go.Bar(x=studentclass1['name'], y= studentclass1['age'])



plot([studentagegraph])


                        #day 4 working on presentation 
dir(pandas)
import pandas
import pandas as pd
import plotly

from plotly.offline import plot 
import plotly.graph_objs as go


wodf = pandas.read_excel('GISdata.xlsx',sheet_name = 'womenOccupation' )
wodf

womenocupation = go.Bar(x=wodf['occupation'], y=wodf['women'],
                        marker = {'color': wodf['women'], 'colorscale' : 'Picnic'})


plot([womenocupation])


womenocupation = go.Bar(x=wodf['occupation'], y=wodf['women'],
                        marker = {'color': wodf['women'], 'colorscale' : 'Jet'})




This is the list of Plotly colorscales:
[‘Blackbody’,
‘Bluered’,
‘Blues’,
‘Earth’,
‘Electric’,
‘Greens’,
‘Greys’,
‘Hot’,
‘Jet’,
‘Picnic’,
‘Portland’,
‘Rainbow’,
‘RdBu’,
‘Reds’,
‘Viridis’,
‘YlGnBu’,
‘YlOrRd’]















































