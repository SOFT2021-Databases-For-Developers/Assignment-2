# Assignment 1 - Rational Databases
- Jonatan Bakke https://github.com/JonatanMagnusBakke
- Jonas Hein - https://github.com/Zenzus
- Thomas Ebsen - https://github.com/Srax 
- [Exercise Link](misc/Assignment.pdf)


## Setup
What you'll need:
1. Python 3
2. Java
3. Your favorite IDE that can run java. We use IntelliJ

## How to run the python tasks
1. Open your CMD
2. Navigate to the root folder of the task you wish to run
3. Write `python program.py` to run the program.

## How to run the js task

## Task 1 - Investigation
#### What is the point of NoSQL databases?
The point of noSQL is that it is flexibil compared to normal SQL. One thing that makes noSQL more flexibil is the way that noSQL doesn't have the same rules as normal sql.  

This makes processes like storing unstructured data easy, you can fx store the data as json data so you don't have to think about how the data has to be split into tables. This non-rigid nature of NoSQL also makes it much easier to update the structure of the database.  

Another point of noSQL can be found in the performance it brings to the table compared to sql. This is because in SQL you have to access data across multiple tables. Whereas with noSQL you have everything in one place which makes noSQL much faster than normal SQL.


## Task 2 - Bloom Filters
#### What is a bloom filter?  
A Bloom filter is a data structure designed to tell you, rapidly and memory-efficiently, whether an element is present in a set.  
  
#### What is an advantage of bloom filters over hash tables?
Bloom filter is that it is space efficient and super fast.

### What is a disadvantage of bloom filters?
Bloom filter is using probability to find out whether or not an item exists in the filter. There is a slight chance that an item is missed or reported as a false positive due to this nature.

####  Using your language of choice, implement a bloom filter with add and check functions. The backing bit-array can simply be a long (64 bit integer).
Check the code.

#### If you are to store one million ASCII strings with an average size of 10 characters in a hash set, what would be the approximate space consumption?
Approximately 100.000.000

#### How many bits per element are required for a 1% false positive rate?
The following equation is used to calculate the required number of bits of space per key.  

E is the false false positive rate.  
  

 1.44log2(1/E) = 1.44log(2(1/0,01)) = 9,56715291328  

 So we need approximately 10 bits per element to reach a false positive rate of 1%.  

 ####  How many bits per element are required for a 5% false positive rate?  
 1.44log2(1/E) = 1.44log(2(1/0,05)) = 6,22357645664  

So we need approximately 7 bits per element to reach a false positive rate of 5%.  

#### If you are to store one million ASCII strings with an average size of 10
characters in a bloom filter, what would be the approximate space consumption, given an allowed false positive rate of 5%?.

6,22357645664 * 10.000.000 = 62.235.765 bits