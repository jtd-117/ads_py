# @file     dlls.py
# @brief    A file for implementing a doubly linked-list stack (DLLS)
# @author   Jude Thaddeau Data
# @note     GitHub: https://github.com/jtd-117
# ---------------------------------------------------------------------------- #

from enum import Enum

# ---------------------------------------------------------------------------- #

class DLLS(object):
    """
    An INTERFACE for a doubly linked-list stack (DLLS)
    """

    class CMPValues(Enum):
        """
        The OUTPUT values permitted by `cmp_fn`, a COMPARISON function that 
        takes 2 variables & outputs which of the variables is less than, equal 
        to, or greater than the other.
        """
        LESS = -1
        EQUAL = 0
        GREATER = 1

    class Node(object):
        """
        A Doubly Linked-List (DLL) node.
        """

        def __init__(self, key):
            self._key = key
            self._next = None
            self._prev = None

        @property
        def key(self):
            """
            Contains the DATA associated with an DLL node.
            """
            return self._key

        @key.setter
        def key(self, new_key):
            self._key = new_key
        
        @key.deleter
        def key(self):
            del self._key
        
        @property
        def next(self):
            """
            A POINTER to a DLL successor node.
            """
            return self._next

        @next.setter
        def next(self, new_next):

            # STEP 1: Ensure the `new_next` is of type `DLLS.Node` or `None`
            if (isinstance(new_next, DLLS.Node) or (new_next is None)):
                self._next = new_next
                return
            
            # STEP 2: `new_next` is an INAPPROPRIATE type
            raise TypeError("`new_next` must be of TYPE `DLLS.Node` or `None`")
        
        @next.deleter
        def next(self):
            del self._next
        
        @property
        def prev(self):
            """
            A POINTER to a DLL predecessor node.
            """
            return self._prev

        @prev.setter
        def prev(self, new_prev):

            # STEP 1: Ensure the `new_prev` is type `DLLS.Node` or `None`
            if (isinstance(new_prev, DLLS.Node) or (new_prev is None)):
                self._prev = new_prev
                return
            
            # STEP 2: `new_prev` is an INAPPROPRIATE type
            raise TypeError("`new_prev` must be of TYPE `DLLS.Node` or `None`")
        
        @prev.deleter
        def prev(self):
            del self._prev

    def __init__(self, cmp_fn):

        # STEP 1: Ensure `cmp_fn` is a function
        if (not callable(cmp_fn)):
            raise TypeError("`cmp_fn` must be of TYPE 'function'")

        # STEP 2: Assign class attributes
        self._cmp_fn = cmp_fn
        self._head = None
        self._tail = None

    @property
    def cmp_fn(self):
        """
        A custom function for COMPARING `DLLS.Node` keys.

        :Parameters:
            - 'v1': The 1st variable for comparison
            - 'v2': The 2nd variable for comparison

        :Return:
            - `1`: if `v1` is GREATER than `v2` 
            - `0`: if `v1` & `v2` are EQUAL
            - `-1`: if `v1` is LESS than `v2` 
        """
        return self._cmp_fn

    @cmp_fn.setter
    def cmp_fn(self, new_cmp_fn):

        # STEP 1: Ensure `new_cmp_fn` is of type 'function'
        if (not callable(new_cmp_fn)):
            raise TypeError("`new_cmp_fn` must be of TYPE 'function'")
        
        # STEP 2: Assign the new comparison function
        self._cmp_fn = new_cmp_fn

    @cmp_fn.deleter
    def cmp_fn(self):
        del self._cmp_fn

    @property
    def head(self):
        """
        The FIRST node in the DLLS.
        """
        return self._head
    
    @head.setter
    def head(self, new_head):

        # STEP 1: Ensure the `new_head` is of TYPE `DLLS.Node` or `None`
        if (isinstance(new_head, DLLS.Node) or (new_head is None)):
            self._head = new_head
            return
        
        # STEP 2: `new_head` is an INAPPROPRIATE type
        raise TypeError("`new_head` must be of TYPE `DLLS.Node` or `None`")
    
    @head.deleter
    def head(self):
        del self._head

    @property
    def tail(self):
        """
        The LAST node in the DLLS.
        """
        return self._tail
    
    @tail.setter
    def tail(self, new_tail):

        # STEP 1: Ensure the `new_tail` is of TYPE `DLLS.Node` or `None`
        if (isinstance(new_tail, DLLS.Node) or (new_tail is None)):
            self._tail = new_tail
            return
        
        # STEP 2: `new_tail` is an inappropriate type
        raise TypeError("`new_tail` must be of TYPE `DLLS.Node` or `None`")
    
    @tail.deleter
    def tail(self):
        del self._tail

    def is_empty(self):
        """
        CHECKS if the DLLS is empty.

        :Return: 
            - `True`: if the DLLS is empty
            - `False`: if the DLLS is NOT empty
        """
        return ((self.head == None) and (self.tail == None))

    def push(self, new_key):
        """
        INSERTS a new TAIL (i.e. END) node in the DLLS.

        :Parameters:
            - `new_key`: is the INFORMATION to be associated with the new 
              TAIL DLLS node

        :Return:
            A POINTER to the NEWLY added DLLS TAIL node
        """
        
        # STEP 1: Adjust the DLLS head pointer
        new_tail = DLLS.Node(new_key)
        new_tail.next = None
        new_tail.prev = self.tail

        # CASE A: This is the 1st DLLS node insertion
        if (self.tail == None):
            self.head = self.tail = new_tail

        # CASE B: NOT the 1st DLLS node insertion
        else:
            self.tail.next = new_tail
            self.tail = new_tail
        
        # STEP 2: Return the NEWLY added DLLS TAIL node
        return self.tail

    def pop(self):
        """
        DELETES the TAIL (i.e. END) node of the DLLS.

        :Return:
            - A POINTER to the new DLLS TAIL node, OR
            - `None`: if the DLLS has NO nodes to delete
        """

        # STEP 1: Check if the DLLS is empty
        if (self.is_empty()):
            return
        
        # STEP 2: Initialise POINTER variables
        old_tail = self.tail
        self.tail = old_tail.prev

        # CASE A: The only DLLS node deleted
        if (self.tail == None):
            self.head = None

        # CASE B: At LEAST 2 DLLS node remaining
        else:
            self.tail.next = None

        # STEP 3: Return the new DLLS TAIL node
        return self.tail

    def __iterative_search(self, target_key):
        """
        ITERATIVELY searches the DLLS & returns a node that MATCHES the target 
        search data.

        :Parameters:
            - `target_key`: is the DESIRED search data to be queried in the DLLS

        :Return:
            - A POINTER to the DLLS node that MATCHES the target search data, OR 
            - `None`: to indicate that NO matches were found
        """
        
        # STEP 1: Linear search the DLLS up to the TAIL node
        curr = self.head
        while (curr):

            # STEP 2: Check if a MATCH was detected
            if (self.cmp_fn(curr.key, target_key) == DLLS.CMPValues.EQUAL.value):
                return curr

            # STEP 3: NO match detected, move to the next node
            curr = curr.next

        # STEP 4: Indicate that NO matches were detected
        return None

    def __recursive_search(self, target_key, self_head):
        """
        RECURSIVELY searches the DLLS & returns a node that MATCHES the target 
        search data.

        :Parameters:
            - `target_key`: is the DESIRED search data to be queried in the DLLS
            - `self_head`: is the CURRENT instance's head node (i.e. self.head)

        :Return: 
            - A POINTER to the node that MATCHES the target search data, OR
            - `None`: to indicate that NO matches were found
        """

        # BASE CASE 1: Went beyond the TAIL node OR ZERO nodes remain
        if (not self_head):
            return None
        
        # BASE CASE 2: Found a match
        if (self.cmp_fn(self_head.key, target_key) == DLLS.CMPValues.EQUAL.value):
            return self_head

        # RECURSIVE CASE: Still more DLLS nodes to search
        return self.__recursive_search(target_key, self_head.next)

    def search(self, target_key, mode = 'i'):
        """
        SEARCHES the DLLS & returns the 1st instance of a DLLS node who's key 
        MATCHES the target search key.

        :Parameters:
            - `target_key`: is the DESIRED search data to be queried in the DLLS
            - `mode` (optional): a SINGLE character `str` that indicates if  
              the DLLS search is conducted iteratively 'i' (default), or 
              recursively 'r'

        :Return: 
            - A POINTER to the node that MATCHES the target search data, OR
            - `None`: to indicate that NO matches were found
        """

        # CASE A: Mode is an INAPPROPRIATE type
        if (not isinstance(mode, str)):
            raise TypeError("`mode` must of TYPE `str`")

        # CASE B: Use the ITERATIVE search method
        elif (mode == 'i'):
            return self.__iterative_search(target_key)

        # CASE C: Use the RECURSIVE search method
        elif (mode == 'r'):
            return self.__recursive_search(target_key, self.head)

        # CASE D: Mode is an INAPPROPRIATE value
        else:
            raise ValueError("`mode` must be of VALUE 'i' or 'r'")