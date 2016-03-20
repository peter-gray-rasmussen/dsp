# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

```
Done
```

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

```
Key similarities: Values of lists and tuples can be of any type and are indexed by integers
Key differences: Lists are mutable but tuples are immutable and you can use tuples as keys in dictionaries but not lists

You can't use lists as keys in dictionaries because lists are not hashable.
```

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

```
["Set is an unordered collection of unique and immutable objects"] (http://www.python-course.eu/sets_frozensets.php)
Lists, however, are mutable and can contain redundant elements.
```

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

```
Python's lambda:
*Is a tool for building functions
*Enables creation of anonymous functions on the fly
*Not neccessary but makes coding easier

For example, the following sorts the tuples by the third key in ascending order: 

student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
]

student_tuples = sorted(student_tuples, key=lambda student: student[2]) # sort by age
print student_tuples

```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

```
List comprehensions provide a concise way to create lists. Examples of list comprehension:
evens1  = [x for x in range(1, 20+1) if x % 2 ==0]
print evens1

# Example of map
squares = map(lambda x: x**2, range(1, 20+1))
print squares

# Example of filter
the_list = [x for x in range(1, 20+1)]
evens2 = filter(lambda x: x % 2 ==0, the_list)
print evens2

# Example of a set comprehension
a = {x for x in 'petergrayrasmussen' if x not in 'gray'}
print a

# Example of a dictionary comprehension
d = {n: n**2 for n in range(5)}
print d
```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

```
937 days
```

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

```
513 days
```

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

```
7850 days
```

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

```
Done
```

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

```
Done
```

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

```
Done
```
---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)

```
Done
```



