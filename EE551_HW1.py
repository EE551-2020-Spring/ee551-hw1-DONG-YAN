#!/usr/bin/python

"""
Python Core object Types
"""

import math

def numbers_and_strings():
    """
    This is to review numbers and strings and basic operations.
    """
    # Assign a string "EE551" to a variable x
    x = "EE551"

    # Assign a string "Stevens" to a variable y
    y = "Stevens"
    # Repeat variable y 5 times
    z = y*5
    # What is the length of z?
    len(z)
    # Concatenate variable y with string " is good"
    m = y+" is good"
    print(m)
    # Replace "good" with "awesome" in variable m and assign it to a new variable n
    n = m.replace("good","awesome")
    print(n)
    return x, y, z, length, m, n


def lists():
    """
    This is to review basic operations with lists.
    """
    n = "Stevens is awesome"

    # Split variable n on a delimiter space into a list of substrings
    p = n.split()
    print(p)
    # Get all the items past the first of the third substring
    r=p[2].replace("awesome","wesome")
    print(r)
    # Create a 3 x 3 matrix as nested list such that
    #   first row is [1, 4, 5]
    #   second row is [6, 10, 11]
    #   third row is [12, 17, 38]
    import numpy as np
    C=np,matrix([[1,4,5],[6,10,11],[12,17,38]])
    print(C)
    # Collect the items in the last column of matrix A using list comprehension
    def last_column(C):
    m = c.tolist()
    lst = []

    for i in range(len(c)):
        lst.append(c[i][-1])
    
    return lst
    last_column(C)
    d=last_column(C)
    # Collect only the even items of the diagonal of matrix C using list comprehension
    o=[1,10,38,5,10,12]
    o.remove[4]
    print(o)
    
    # We can convert a single character to its underlying integer code (e.g., its ASCII byte value)
    # by passing it to the built-in ord function. Generate a list of these integers to represent
    # each character of the string "Stevens" using list comprehension.

    return p, r, c, d, o


def dictionaries():
    """
    This is to review basic operations with dictionaries.
    """
    # Create a dictionary that maps:
    #   fruit => "apple"
    #   quantity => 4
    #   color => "green"
    f={'fruit':'apple','quantity':'4','color':'green'}
    print(f)
    # Get the item in dictionary f that the key "fruit" maps to
    f['fruit']
    # Increase the quantity of f by 1
    # IMPLEMENT IT HERE
    f['quantity']=5
    print(f)
    # Create a nested dictionary where:
    #   name => {first_name => "Grace", last_name => "Hopper"} (a dictionary)
    #   jobs => ["scientist", "engineer"] (a list)
    #   age => 85
    name={'first_name':'Grace','last_name':'Hopper'}
    jobs=["scientist","engineer"]
    age="85"
    a={"name","jobs","age"}
    # Add "programmer" to the list of jobs Grace has
    # IMPLEMENT IT HERE
    jobs.append("programmer")
    print(jobs)
    # Get the third job Grace has that you recently added
    p= jobs[2]
    # Use the sort() function to get sorted keys of amazing_grace in alphabetically ascending order
    k = [key for key in amazing_grace.keys()];
    k.sort()
    return a, f, p, k

numbers_and_strings()
lists()
dictionaries()





