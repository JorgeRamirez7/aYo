"""Gets a unique random element from a list.
There is never a repeated list item for at least 4 calls. 
Must be a minimum of 4 variables"""
import random

from collections import deque

class RandomElementSkill():
    def __init__(self, original_list):
        """Copies the parameter original_list to it's own self variable and a randomized list.
            
            Args:
                original_list: The list that will be randomized.
        """
        self.original_list = original_list
        self.last_item = None
        self.penultimate_item = None
    
        self.shuffle_random_list()

        self.last_item = self.randomized_list[0]
        self.penultimate_item = self.randomized_list[1]

    def shuffle_random_list(self):
        """Shuffles the items in random_list."""
        self.randomized_list = deque()
    
        for item in self.original_list:
            self.randomized_list.append(item)
      
        random.shuffle(self.randomized_list)

        """If the next 2 elements to be popped are the same as the 2 previously popped elements, then reshuffle random list."""
        while(self.randomized_list[len(self.randomized_list) - 1] == self.last_item or 
        self.randomized_list[len(self.randomized_list) - 1] == self.penultimate_item or
        self.randomized_list[len(self.randomized_list) - 2] == self.last_item or 
        self.randomized_list[len(self.randomized_list) - 2] == self.penultimate_item):
            self.shuffle_random_list()

        self.last_item = self.randomized_list[0]
        self.penultimate_item = self.randomized_list[1]

    def get_random_element(self):
        """Gets the random element from a list."""
        """List must contain at least 4 elements."""
        if len(self.original_list) < 4:
            return "OH NOOOOO"

        if not self.randomized_list:
            self.shuffle_random_list()
      
        return self.randomized_list.pop()
