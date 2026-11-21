
# Problem 12 - Imports

import my_functions
my_functions.greet("Benjamin")

from my_functions import greet
greet("Benjamin")

from my_functions import greet as fn
fn("Benjamin")

import my_functions as mn
mn.greet("Benjamin")

from my_functions import *
greet("Benjamin")
