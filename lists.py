# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kenzie assignment: Lists!
"""
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Instructions:
# Complete each function below by writing the code for it. main() is already
# set up to test all the functions with a few different inputs, printing 'OK'
# for each function once it returns the correct result.
# The starter code for each function includes a bare 'return' which is just a
# placeholder for your code.

# Your name, plus anyone who helped you with this assignment.
# Give credit where credit is due.
__author__ = "Kamela Williamson"
# Did zip_merge and empty_filter with Mai
# https://www.w3resource.com/python-exercises/list/python-data-type-list-exercise-5.php
# https://www.w3schools.com/python/ref_string_startswith.asp
# https://www.w3resource.com/python-exercises/list/python-data-type-list-exercise-6.php
# https://www.geeksforgeeks.org/python-remove-empty-strings-from-list-of-strings/
# https://www.geeksforgeeks.org/python-remove-empty-strings-from-list-of-strings/
# https://www.askpython.com/python/built-in-methods/python-filter-function
# https://www.geeksforgeeks.org/append-extend-python/


# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.


def match_ends(words):
    # your code here
    # empty string
    str = 0
    for compare in words:
        if len(compare) > 1 and compare[0] == compare[-1]:
            str += 1
    return str


# B. front_x
# Given a list of strings, return a list with the strings in
# sorted order, except group all the strings that begin with
# 'x' first.
# Example:
#   ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
#   ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each
# of them before combining them.


def front_x(words):
    # your code here
    x_words = []
    not_x = []
    # x is first
    # look up why i had to wrap it in () and why i had to use letter before for
    x_words = sorted([letter for letter in words if letter[0] == 'x'])
    not_x = sorted([letter for letter in words if letter[0] != 'x'])
    # holy crap it let me do it

    return x_words + not_x

# C. sort_last
# Given a list of non-empty tuples, return a list sorted in
# increasing order by the last element in each tuple.
# Example
#   [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
#   [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element from each tuple.


def sort_last(tuples):
    # your code here
    # why do they have to be on the same line?
    def last_element(i): return i[-1]
    return sorted(tuples, key=last_element)


# D. remove_adjacent
# Given a list of numbers, return a list where all adjacent
# equal elements have been reduced to a single element.
# Example:
#   [1, 2, 2, 3] -> [1, 2, 3]
# You may create a new list or modify the passed in list.
# Hint: Don't use set()
# this is confusing. took me hours


def remove_adjacent(nums):
    # your code here
    # return a list
    final_list = []
    for num in nums:
        if len(final_list) == 0 or num != final_list[-1]:
            final_list.append(num)
    return final_list


# E. zip_merge
# Given two lists, combine the values from their corresponding
# indices into a single list.
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# result = ['My', 'name', 'is', 'Kelly']
# Hint: Think of it as "zipping" two lists together.  Is there
# a built-in function in python that will do this?


def zip_merge(list1, list2):
    return [p1 + p2 for p1, p2 in zip(list1, list2)]

# F. empty_filter
# Given a single list containing strings, empty strings, and
# None values:  Return a new list with the same elements, but
# strip out (filter) the empty strings and None values away.
# example: list1 = ["Mike", "", "Emma", None, "Kelly", "", "Brad", None]
# result:  ["Mike", "Emma", "Kelly", "Brad"]
# Hint: There is a Python idiom for doing this.  Can you find it?


def empty_filter(list1):
    # your code here
    list1 = list(filter(None, list1))
    return list1


# G. linear_merge
# Given two lists sorted in increasing order, create and
# return a merged list of all the elements in sorted order.
# You may modify the passed in lists.
# The solution should work in "linear" time, making a single
# pass of both lists.
# Hint: Don't use `sort` or `sorted` -- they are not O(n)
# linear time and the two lists are already provided in
# ascending sorted order.


def linear_merge(list1, list2):
    # your code here
    # single_pass = list1 + list2
    # single_pass.sort()
    # return single_pass
    result = []
    while len(list1) and len(list2):
        if list1[0] < list2[0]:
            result.append(list1.pop(0))
        else:
            result.append(list2.pop(0))
    result.extend(list1)
    result.extend(list2)
    return result
