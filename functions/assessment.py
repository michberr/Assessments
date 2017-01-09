"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE: Write your own function declarations - Part 1 questions aren't
included in the doctest.

PART TWO:

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    >>> calculate_price(25, "CA")
    27.0

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0)
    150

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

PART THREE: Write your own function declarations - Part 3 questions aren't
included in the doctest.

"""

###############################################################################

# PART ONE

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.

#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', where are you from?" depending on what the function from part
#        (a) evaluates to.

# a
def is_my_town(town_name):
    """Returns boolean value for whether town is my hometown (Seattle).

    >>> is_my_town("San Francisco")
    False

    """
    return town_name is "Seattle"


def combine_names(first_name, last_name):
    """Returns a concatenated string of first name and last name.

    >>> combine_names("Michelle", "Berry")
    'Michelle Berry'

    P.S. I really wanted to call this function "cat_names" as a bash pun
    """

    return first_name + " " + last_name


def make_introduction(hometown, first_name, last_name):
    """Prints introduction that depends on whether hometown is shared.

    >>> make_introduction("San Francisco", "Balloonicorn",  "Jones")
    Hi, Balloonicorn Jones, where are you from?

    """

    full_name = combine_names(first_name, last_name)

    if is_my_town(hometown):
        print "Hi %s, we're from the same place!" % (full_name)
    else:
        print "Hi, %s, where are you from?" % (full_name)


###############################################################################

# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry."


def is_berry(fruit):
    """Determines if fruit is a strawberry, cherry, or blackberry.

    >>> is_berry("Strawberry")
    True

    >>> is_berry(3)
    Fruit argument must be a string.

    """
    try:
        return fruit.lower() in ["strawberry", "cherry", "blackberry"]
    except AttributeError:
        print "Fruit argument must be a string."


# (b) Write another function, shipping_cost(), which calculates shipping cost
#     by taking a fruit name as a string and calling the is_berry() function
#     within the shipping_cost() function. Your function should return 0 if
#     is_berry() == True, and 5 if is_berry() == False.

def shipping_cost(fruit):
    """Calculates shipping cost of fruit.

    Shipping cost is $0 if fruit is a berry.
    Shipping cost is $5 if fruit is not a berry.

    """

    if is_berry(fruit):
        return 0
    else:
        return 5


# 2. Make a function that takes in a number and a list of numbers. It should
#    return a new list containing the elements of the input list, along with
#    given number, which should be at the end of the new list.

def append_to_list(lst, num):
    """Appends the num argument to the end of the list."""

    lst.append(num)

    return lst


# 3. Write a function calculate_price to calculate an item's total cost by
#    adding tax, and any fees required by state law.

#    Your function will take as parameters (in this order): the base price of
#    the item, a two-letter state abbreviation, and the tax percentage (as a
#    two-digit decimal, so, for instance, 5% will be .05). If the user does not
#    provide a tax rate it should default to 5%.

#    CA law requires stores to collect a 3% recycling fee, PA requires a $2
#    highway safety fee, and in MA, there is a commonwealth fund fee of $1 for
#    items with a base price under $100 and $3 for items $100 or more. Fees are
#    added *after* the tax is calculated.

#    Your function should return the total cost of the item, including tax and
#    fees.

def calculate_price(base_price, state, tax=0.05):
    """ calculates an item's sale price including tax and state fees.

    args:
        base_price: the price in USD before taxes/fees.
        state: two-letter state abbreviation.
        tax: tax rate as two digit decimal e.g. 7% = 0.07. Default is 5%.

    returns:
        full price of item

    Note:
    I would prefer the my function return the full_price rounded to two 
    decimals. However, the way the doctests were written, the function sometimes
    returns a float and sometimes an integer.

    If I had control over the doctests, I would return this instead:
    return round(full_price, 2)

    """
    fees = {'CA': lambda x: x * 0.03,
            'PA': lambda x: 2,
            'MA': lambda x: 1 if x < 100 else 3,
    }

    full_price = base_price * (1 + tax)
    if state in fees:
        full_price += fees[state](base_price)

    return full_price



###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


# 1. Make a new function that takes in a list and any number of additional
# arguments, appends them to the list, and returns the entire list. Hint: this
# isn't something we've discussed yet in class; you might need to google how to
# write a Python function that takes in an arbitrary number of arguments.

def append_to_list2(lst, *args):
    """Appends variable number of arguments to a list.

    >>> append_to_list2([1,3,5], 4, 6, [8, 10])
    [1, 3, 5, 4, 6, [8, 10]]
    
    """

    lst.extend(list(args))
    return(lst)




# 2. Make a new function with a nested inner function.
# The outer function will take in a word.
# The inner function will multiply that word by 3.
# Then, the outer function will call the inner function.
# Output will be the original function argument and the result of the inner
# function.

# Example:

#>>> outer("Balloonicorn")
#('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')

def outer(outer_word):
    """Returns a tuple with a string and the string copied three times.

    >>> outer("Balloonicorn")
    ('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')

    """
    def inner(inner_word):
        """ Returns a string copied three times into a new string"""
        return inner_word * 3

    word_x_3 = inner(outer_word)
    return (outer_word, word_x_3)


###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
