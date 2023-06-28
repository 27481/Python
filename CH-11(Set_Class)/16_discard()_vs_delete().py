""" In Python, both the discard() and remove() methods are used to remove elements from a set. However, there is a key difference between them:

discard() method: The discard() method removes an element from a set if it is present, but does not raise an error if the element is not found in the set.

remove() method: The remove() method removes an element from a set if it is present, but raises a KeyError error if the element is not found in the set. """



""" 
the main difference between discard() and remove() methods in Python sets. discard() removes the element from the set if it is present, without raising an error if it is not present. 
remove() removes the element from the set if it is present, but raises a KeyError error if it is not present.

It is important to note that both methods modify the original set in-place, and do not return any value.
"""