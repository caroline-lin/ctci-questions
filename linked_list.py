#!/usr/bin/python3

import unittest

class testLinkedList(unittest.TestCase):
    
    def testInserts(self):
        l = LinkedNode(0)
        
        for i in range(1, 10):
            l.append(i)
        
        self.assertEqual( str(l), str(list(range(10))) )
        return

    def testPalin(self): # not a palindrome
        vals = ['a', 'b', 'c']

        l = LinkedNode(vals[0])
        for val in vals[1:]:
            l.append(val)

        self.assertEqual( l.is_palindrome(), False )
        return

    def testPalin_two(self): # even palindrome
        vals = 'abuttuba'
        l = LinkedNode(vals[0])
        for val in vals[1:]:
            l.append(val)
        self.assertEqual( l.is_palindrome(), True )
        return

    def test_odd_palindrome(self):
        vals = 'abcdcba'
        l = LinkedNode(vals[0])
        for val in vals[1:]:
            l.append(val)
        self.assertEqual( l.is_palindrome(), True )
        return


class LinkedNode():
    ''' A linked list implementation with a slightly annoying api'''

    def __init__(self, value):
        self.value = value
        self.next = None
        return

    def __str__(self):
        s = ''
        sep = ', '

        curr = self
        while curr is not None:
            s += str(curr.value) + sep
            curr = curr.next

        s = s[:len(s) - len(sep)] # slice out sep
        return '[' + s + ']'
    
    # ---- some 'woah haskell'-type stuff ----
    
    # mimics accumulation over the linked list
    def _traverse(self, func, ivalue):
        curr = self
        accum = ivalue
        while curr is not None:
            accum = func(curr.value, accum)
            curr = curr.next
        return accum

    # functional programming in a non-functional language
    def altstr(self):
        sep = ', '
        result = self._traverse(lambda value, accumulator : accumulator + str(value) + sep , '')
        result = result[:len(result) - len(sep)]
        return '[' + result + ']'
    
    # ---- back to normal ----

    def append(self, value):
        t = LinkedNode(value)

        curr = self
        while curr.next is not None:
            curr = curr.next
        curr.next = t
        return
    
    # check if this linked list is a palindrome.
    def is_palindrome(self):
        l = []
        curr = self
        while curr is not None: # construct a 'stack' by reference
            l.append(curr.value)
            curr = curr.next

        curr = self
        while curr is not None:
            reverse = l.pop()
            if reverse != curr.value:
                return False
            curr = curr.next
        return True

if __name__ == '__main__':
    unittest.main()
