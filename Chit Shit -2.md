# ======== List in Python ========

**Python Lists**

- Lists are ordered collection of data items.
- They store multiple items in a single variable.
- List items are separated by commas and enclosed within square brackets [].
- Lists are changeable meaning we can alter them after creation.

**List Comprehension**

 → List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.


**List Methods**

- **list.sort()** → This method sorts the list in ascending order. The original list is updated.

- **list.sort(reverse=True)** → To print the list in the descending orders.

- **reverse()** → This method reverses the order of the list.

- **index()** → This method returns the index of the first occurrence of the list item.

- **count()** → Returns the count of the number of items with the given value.

- **copy()** → Returns copy of the list. This can be done to perform operations on the list without modifying the original list.

- **append()** → This method appends items to the end of the existing list.

- **insert()** → This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.

- **extend()** → This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.

- **Concatenating two lists** → You can simply concatenate two lists to join two lists.



# ======== Tuple in Python ========

**Python Tuple**

Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are separated by commas and enclosed within round brackets (). Tuples are unchangeable meaning we can not alter them after creation.

**★ Tuples are immutable**

**★ Manipulating Tuples**

→ Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.

|                          **SYNTAX**                             |   
| :---------------------------------------------------------------| 
|                                                                 |   
|  `countries = ("Spain", "Italy", "India", "England", "Germany")`|
|  `temp = list(countries)`                                       |
|  `temp.append("Russia")       #add item`                      |
|  `temp.pop(3)                 #remove item`                     |
|  `temp[2] = "Finland"         #change item`                     |  
|  `countries = tuple(temp)`                                      |  
|  `print(countries)`                                             |  
| :---------------------------------------------------------------|
|                           **OUTPUT**                            |
| :---------------------------------------------------------------|
|  `('Spain', 'Italy', 'Finland', 'Germany', 'Russia')`           |


**★ Methods in Tuples**

- index() → The index() Method returns the first occurance of the element from the tuple

|              **SYNTAX**            |   
| :----------------------------------| 
|                                    |   
|  `tuple.index(element, start, end)`|

  