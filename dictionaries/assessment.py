"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    words = phrase.split()

    word_count = {}

    for word in words:
        # If word exists in word_count add one to the value count,
        # otherwise, add it to the dictionary with value 1
        word_count[word] = word_count.get(word, 0) + 1

    return word_count


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon.

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If melon name does not exist, return 'No price found'.

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """
    melon_prices = {
        'Watermelon': 2.95,
        'Cantaloupe': 2.50,
        'Musk':       3.25,
        'Christmas':  14.25,
    }

    if melon_name in melon_prices:
        return melon_prices[melon_name]
    else:
        return 'No price found'



def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

        >>> word_length_sorted(["porcupine", "ok"])
        [(2, ['ok']), (9, ['porcupine'])]
    """

    word_lengths = {}

    for word in words:
        word_len = len(word)

        # Add words to dictionary with (word-length, word) as keys and values
        if word_len in word_lengths:
            word_lengths[word_len].append(word)
        else:
            word_lengths[word_len] = [word,]

    for lengths in word_lengths:
        # Sort the list of words for each word-length key
        word_lengths[lengths].sort()

    # return a sorted list of key,value tuples
    return sorted(word_lengths.items())


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    english_to_pirate = {
        'sir':         'matey',
        'hotel':       'fleabag inn',
        'student':     'swabbie',
        'man':         'matey',
        'professor':   'foul blaggart',
        'restaurant':  'galley',
        'your':        'yer',
        'excuse':      'arr',
        'students':    'swabbies',
        'are':         'be',
        'restroom':    'head',
        'my':          'me',
        'is':          'be',
    }

    words = phrase.split()

    for i, word in enumerate(words):
        # If word is in the dictionary, replace word with pirate translation
        if word in english_to_pirate:
            words[i] = english_to_pirate[word]

    return ' '.join(words)


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    def make_letter_dict(names):
        """Create dictionary with (first letters, word) as keys and values"""
     
        first_letters = {}

        for name in names:

            # First letter  
            fl = name[0]

            # Add (first letter, word) to dictionary or append word to 
            # word list if letter already exists.
            if fl in first_letters:
                first_letters[fl].append(name)
            else:
                first_letters[fl] = [name,]

        return first_letters

    # First name in the names list starts the chain
    word_chain = [names[0],]

    # Create dictionary of words in names, excluding the first one
    first_letters = make_letter_dict(names[1:])

    # Last letter of the name becomes the first letter of the next
    fl = names[0][-1]

    while True:
        if fl in first_letters:
            
            # Append the first word in the list to the word chain
            word = first_letters[fl][0]
            word_chain.append(word)

            # Remove the word from the dictionary either by slicing the 
            # word list, or removing the key if it's the last word
            if len(first_letters[fl]) > 1:
                first_letters[fl] = first_letters[fl][1:]
            else:
                del first_letters[fl]

            # The new first letter is the last letter of the previous word
            fl = word[-1]
     
        else:
            break

    return word_chain

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
