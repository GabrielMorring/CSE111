import random

def main():
    x = 'past'
    y = 'present'
    z = 'future'

    print(f'\n{get_determiner(1).title()} {get_noun(1)} {get_verb(1, x)}.')
    print(f'\n{get_determiner(2).title()} {get_noun(2)} {get_verb(2, x)}.')
    print(f'\n{get_determiner(1).title()} {get_noun(1)} {get_verb(1, y)}.')
    print(f'\n{get_determiner(2).title()} {get_noun(2)} {get_verb(2, y)}.')
    print(f'\n{get_determiner(1).title()} {get_noun(1)} {get_verb(1, z)}.')
    print(f'\n{get_determiner(2).title()} {get_noun(2)} {get_verb(2, z)}.')


    print(f'\n{get_determiner(1).title()} {get_noun(1)} {get_verb(1, x)} {get_prepositional_phrase(1)}.')
    print(f'\n{get_determiner(2).title()} {get_noun(2)} {get_verb(2, x)} {get_prepositional_phrase(2)}.')
    print(f'\n{get_determiner(1).title()} {get_noun(1)} {get_verb(1, y)} {get_prepositional_phrase(1)}.')
    print(f'\n{get_determiner(2).title()} {get_noun(2)} {get_verb(2, y)} {get_prepositional_phrase(2)}.')
    print(f'\n{get_determiner(1).title()} {get_noun(1)} {get_verb(1, z)} {get_prepositional_phrase(1)}.')
    print(f'\n{get_determiner(2).title()} {get_noun(2)} {get_verb(2, z)} {get_prepositional_phrase(2)}.')

    
def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is a word
    like "the", "a", "one", "two", "some", "many". If quantity == 1,
    this function will return either "the" or "one". Otherwise
    this function will return either "some" or "many".

    Parameter
        quantity: an integer. If quantity == 1, this function will
            return a determiner for a singular noun. Otherwise this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["the", "one"]
    else:
        words = ["some", "many"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


def get_noun(quantity):
    """Return a randomly chosen noun. If quantity == 1, this
    function will return one of these ten singular nouns:
        "adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"
    Otherwise, this function will return one of these ten
    plural nouns:
        "adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"

    Parameter
        quantity: an integer that determines if the
            returned noun is singular or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        words = ["adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"]
    else:
        words = [ "adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"]

    return random.choice(words)

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past", this
    function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this function will
    return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1, this function
    will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of these
    ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameter
        quantity: an integer that determines if the returned
            verb is singular or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == 'past':
        words = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    
    elif tense == 'present' and quantity == 1:
        words = [ "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    
    elif tense == 'present' and quantity != 1:
        words = [ "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]    
    
    elif tense == 'future':
        words = [ "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    return random.choice(words)

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    return random.choice(words)

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and nouns are singular or plural.
    Return: a prepositional phrase.
    """
   
    return get_preposition() + ' ' + get_determiner(quantity) + ' ' + get_noun(quantity) 

main()