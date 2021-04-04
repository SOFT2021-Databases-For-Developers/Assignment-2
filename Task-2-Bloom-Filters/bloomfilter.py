import math
import mmh3
from bitarray import bitarray

# Class for the bloom filter
class BloomFilter(object):
 
    # Initialize the class with a constructor
    def __init__(self, items_count, fp_prob):
        self.fp_prob = fp_prob  # False positive rate
        self.size = self.get_size(items_count, fp_prob) # Size of the bit array
        self.hash_count = self.get_hash_count(self.size, items_count) # Number of hash functions to use
        self.bit_array = bitarray(self.size) # Create bitarray of the given size
        self.bit_array.setall(0) # initialize all bits as 0
 
    # Add item to the filter
    def add(self, item):
        digests = [] # Create array to cache digests
        for i in range(self.hash_count): 
            # Create digest for given item.
            # It is used as a seed for the mmh3.hash() function. 
            # The digest is created differently depending on the seed
    
            digest = mmh3.hash(item, i) % self.size
            digests.append(digest)

            # Set all bits to TRUE in the bit array
            self.bit_array[digest] = True
 

    # Check if item is present in the filter
    def check(self, item):
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size

            # Check if any of the bits is FALSE or TRUE.
            # If a bit is false, it's not present in the filter, else there is a probability that it exists
            if self.bit_array[digest] == False:
                return False # FALSE = Likely not present
        return True # TRUE = Likely present in filter
 
    # Return the size of the bit array
    def get_size(self, n, p):

        # The formula for calculating the size
        m = -(n * math.log(p))/(math.log(2)**2)
        return int(m)
 
    # Return the hash count of the bit array
    def get_hash_count(self, m, n):
        # The formula for calculating the hash
        # m is the size of the bit array
        # n is the number of items expected to be present in the filter
        k = (m/n) * math.log(2)
        return int(k)