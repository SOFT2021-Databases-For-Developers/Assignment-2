# Assignment 1 - Rational Databases
- Jonatan Bakke https://github.com/JonatanMagnusBakke
- Jonas Hein - https://github.com/Zenzus
- Thomas Ebsen - https://github.com/Srax 
- [Exercise Link](misc/Assignment.pdf)


## Setup
What you'll need:
1. Python 3
2. Nodejs

## How to run the python tasks
1. Open your CMD
2. Navigate to the root folder of the task you wish to run
3. Write `python program.py` to run the program.

## How to run the js task
1. Open your CMD
2. Navigate to [Task-4-map-and-reduce](/Task-4-map-and-reduce)
3. Write `node Task4MapAndReduce.js` to run the program.

## Task 1 - Investigation
#### What is the point of NoSQL databases?
The point of noSQL is that it is flexibil compared to normal SQL. One thing that makes noSQL more flexibil is the way that noSQL doesn't have the same rules as normal sql.  

This makes processes like storing unstructured data easy, you can fx store the data as json data so you don't have to think about how the data has to be split into tables. This non-rigid nature of NoSQL also makes it much easier to update the structure of the database.  

Another point of noSQL can be found in the performance it brings to the table compared to sql. This is because in SQL you have to access data across multiple tables. Whereas with noSQL you have everything in one place which makes noSQL much faster than normal SQL.

#### What is the CAP theorem? 
The CAP theorem is like the classic statement you hear “Cheap, Fast, and Good: Pick Two”.
CAP is a theorem that applies to distributed systems for storing data on one or more machines, these machines can be physical or virtual machines, that faktore does not change the theorem. CAP stands for consistency, availability, and partition tolerance (the ‘C,’ ‘A’ and ‘P’ in CAP). And the theorem clams that you can only achieve two of the three of  consistency, availability, and partition tolerance. 

**Consistency**  
Means that all clients can see the same data simultaneously which means when data is updated on one note the note must update all the other notes. 

**Availability**  
Means that you can always get a data response, even if one or more notes are down.  
Another way to say this is that any working note must always return a valid response.

**Partition Tolerance**
Is about temporarily delayed/breaks in the connection between two nodes. And Partition tolerance means that if a delay/break occurs, the cluster must continue to work.

#### What are the ideal use cases of HBase?
The strong point of HBase lies how excellent it is in scalability and performance for big workloads, HBase also comes with autoload balancing and failover features that makes it ideal for big applications with big and growing workloads, and is the reason that it is used by Facebook for there message infrastructure and Twitter uses it for transactional tables in Twitter's production backend.




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

## Task 3 - Huffman Coding
<img src="Task-3-Huffman-Coding\img\huffmantree.png">
See the code

## Task 4 - Map and Reduce
See the code