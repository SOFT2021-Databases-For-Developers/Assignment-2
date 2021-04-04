from bloomfilter import BloomFilter
from random import shuffle

item_count = 10 # no of items to add
false_positive_probability = 0.05 # false positive probability

# Define bloom filter
bloomf = BloomFilter(item_count,false_positive_probability)

print("SIZE OF BIT ARRAY: {}".format(bloomf.size))
print("FALSE POSITIVE PROBABILITY: {}".format(bloomf.fp_prob))
print("NUMBER OF HASH FUNCTIONS: {}".format(bloomf.hash_count))
print("-------------------------------")

# List of words to be added to the filter
word_present = ['concede','concedes','battlefield', 'battlefields', 'waterfall', 'waterfalls', 'house', 'houses', 'meadow', 'meadows']

# List of words to not add to the array. Used to put up against the words added to the filter to check whether or not the bloom filter is correct.
word_absent = ['chance', 'code', 'fail', 'gone', 'deck', 'bytes', 'bingbong', 'anders', 'nine', 'word']

# Add each item in word_present to the bloom filter
for item in word_present:
	bloomf.add(item)

# Shuffle both arrays
shuffle(word_present)
shuffle(word_absent)

# List of words to test probability.
# We combine the first 10 words in the word_present array with all of the words in the word_absent array
test_words = word_present[:5] + word_absent

# Shuffle the array
shuffle(test_words)

# Iterate through each word in test_words and check it's probability
for word in test_words:
	if bloomf.check(word):
		if word in word_absent:
			print("'{}' is a false positive!".format(word))
		else:
			print("'{}' is probably present!".format(word))
	else:
		print("'{}' is definitely not present!".format(word))
