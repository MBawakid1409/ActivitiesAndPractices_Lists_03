# Activities & Practices
# --------- [Lists] ---------
print("--------- [Lists] ---------")
print("----------------------------------")
# Practise 01
print("Practise #01")
myList0 = ['apple', 'banana', 'pear']
# myList0 = ['apple', 'banana', 'pear']
myList0.append('orange')
# myList0 == ['apple', 'banana', 'pear', 'orange']
print(myList0)
print("----------------------------------")
# Practise 02
print("Practise #02")
# myList0 = ['apple', 'banana', 'pear', 'orange']
myList0.pop() # returns 'orange'
# myList0 == ['apple', 'banana', 'pear']
print(myList0)
print("----------------------------------")
# Practise 03
print("Practise #03")
# myList0 = ['apple', 'banana', 'pear']
colors = ['red', 'yellow', 'green', 'blue']
print(colors[2]) # returns 'green'
favoriteColor0 = colors[2]
print(favoriteColor0)
print("----------------------------------")
# Practise 04
print("Practise #04")
garden = []
garden.append("Apples")
print(garden)
# Output: ['Apples']
garden = ["Tomatoes", "Grapes", "Cauliflower"]
garden.append("Green Beans")
print(garden)
# Output: ['Tomatoes', 'Grapes', 'Cauliflower', 'Green Beans']
print("----------------------------------")
# Practise 05
print("Practise #05")
items_sold = ["cake", "cookie", "bread"]
items_sold_new = items_sold + ["biscuit", "tart"]
print(items_sold_new)
# Output: ['cake', 'cookie', 'bread', 'biscuit', 'tart']
print("----------------------------------")
# Practise 06
print("Practise #06")
orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]
new_orders = ["lilac", "iris"]
orders_combined = orders + new_orders
print(orders_combined)
# Output: ['daisy', 'buttercup', 'snapdragon', 'gardenia', 'lily', 'lilac', 'iris']
print("----------------------------------")
# Practise 07
print("Practise #07")
shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]
last_element = shopping_list[-1]
index5_element = shopping_list[5]
print(index5_element+last_element)
# Output: cerealcereal
print("----------------------------------")
# Practise 08
print("Practise #08")
garden = ['Tomatoes', 'Green Beans', 'Cauliflower', 'Grapes']
garden[2] = "strawberries"
print(garden) # Output: ['Tomatoes', 'Green Beans', 'strawberries', 'Grapes']
garden[-1] = "Raspberries"
print(garden) #Output:['Tomatoes', 'Green Beans', 'strawberries', 'Raspberries']
print("----------------------------------")
# Practise 09
print("Practise #09")
shopping_line = ["cole", "Kip", "Chris", "Sylvana"]
shopping_line.remove("Chris")
print(shopping_line) # Output: ['cole', 'Kip', 'Sylvana']
print("----------------------------------")
# Practise 10
print("Practise #10")
heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64], ["Vik", 68]]
print(heights)
# Output: [['Jenny', 61],['Alexus', 70],['Sam', 67],['Grace', 64],['Vik', 68]] 
ages = [["Aaron", 15], ["Dhruti", 16]]
print(ages) # Outputs: [['Aaron', 15], ['Dhruti', 16]]
print("----------------------------------")
# Practise 11
print("Practise #11")
class_name_test=[["Jenny", 90], ["Alexus", 85.5], ["Sam", 83], ["Ellie", 101.5]]
print(class_name_test)
sams_score = class_name_test[2][1]
print(sams_score) # prints 83
ellies_score = class_name_test[-1][-1]
print(ellies_score) # prints 101.5
print("----------------------------------")
# Practise 12
print("Practise #12")
incoming_class = [["Kenny", "American", 9],
                  ["Tanya", "Russian", 9],
                  ["Madison", "Indian", 7]]
print(incoming_class)
#[['Kenny', 'American', 9], ['Tanya', 'Russian', 9], ['Madison', 'Indian', 7]]
incoming_class[2][2] = 8
print(incoming_class)
#[['Kenny', 'American', 9], ['Tanya', 'Russian', 9], ['Madison', 'Indian', 8]]
incoming_class[-3][-3] = "Ken"
print(incoming_class)
#[['Ken', 'American', 9], ['Tanya', 'Russian', 9], ['Madison', 'Indian', 8]]
print("----------------------------------")
# Practise 13
print("Practise #13")
# .count() - A list method to count the number of occurrences of an element in a list.
# .insert() - A list method to insert an element into a specific index of a list.
# .pop() - A list method to remove an element from a specific index or from the end of a list.
# range() - A built-in Python function to create a sequence of integers.
# len() - A built-in Python function to get the length of a list.
# sort()/sorted() - A method and a built-in function to sort a list.
print("----------------------------------")
print("----------------------------------")
# Practise 14
print("Practise #14")
store_line = ["Karla", "Maxium", "Martim", "Isabelle"]
print(store_line) # ['Karla', 'Maxium', 'Martim', 'Isabelle']
store_line.insert(2, "vikor")
print(store_line) # ['Karla', 'Maxium', 'vikor', 'Martim', 'Isabelle']
print("----------------------------------")
# Practise 15
print("Practise #15")
cs_topics = ["Python", "Data Structures", "Balloon Making", "Algorithms", "Clowns 101"]
removed_element1 = cs_topics.pop()
print(cs_topics) # ['Python', 'Data Structures', 'Balloon Making', 'Algorithms']
print(removed_element1) # Clowns 101
removed_element2 = cs_topics.pop(2)
print(cs_topics) # ['Python', 'Data Structures', 'Algorithms']
print(removed_element2) # Balloon Making
print("----------------------------------")
# Practise 16
print("Practise #16")
my_range = range(10)
print(my_range) # Output: range(0, 10)
print(list(my_range)) # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# list() - is a built-in function that generate list for us
print("----------------------------------")
# Practise 17
print("Practise #17")
my_list = range(2, 9)
print(my_list) # Output: range(2, 9)
print(list(my_list)) # Output: [2, 3, 4, 5, 6, 7, 8]
print("----------------------------------")
# Practise 18
print("Practise #18")
my_range2 = range(2, 9, 2)
print(list(my_range2)) # [2, 4, 6, 8]
my_range3 = range(1, 100, 10)
print(list(my_range3)) # [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
range_five_three = range(5, 15, 3)
print(list(range_five_three)) # [5, 8, 11, 14]
range_diff_five = range(0, 40, 5)
print(list(range_diff_five)) # [0, 5, 10, 15, 20, 25, 30, 35]
print("----------------------------------")
# Practise 19
print("Practise #19")
my_list = [1, 2, 3, 4, 5]
print(len(my_list)) # 5
print("----------------------------------")
# Practise 20
print("Practise #20")
long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]
long_list_len = len(long_list)
print(long_list_len) # Output: 18
print("----------------------------------")
# Practise 21
print("Practise #21")
big_range = range(2, 3000, 10)
big_range_length = len(big_range)
print(big_range_length) # Output: 300
big_range = range(2, 3000, 100)
big_range_length = len(big_range)
print(big_range_length) # Output: 30
print("----------------------------------")
# Practise 22
print("Practise #22")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
sliced_list= letters[1:6]
print(sliced_list) # Output: ['b', 'c', 'd', 'e', 'f']
print("----------------------------------")
# Practise 23
print("Practise #23")
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]
beginning = suitcase[0:2]
print(beginning) # Output: ['shirt', 'shirt']
middle = suitcase[2:4]
print(middle) # Output: ['pants', 'pants']
print("----------------------------------")
# Practise 24
print("Practise #24")
fruits = ["apple", "cherry", "pineapple", "orange", "mango"]
print(fruits[:3]) # Output: ['apple', 'cherry', 'pineapple']
print(fruits[-2:]) # Output: ['orange', 'mango']
print(fruits[:-1]) # Output: ['apple', 'cherry', 'pineapple', 'orange']
print("----------------------------------")
# Practise 25
print("Practise #25")
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]
last_two_elements = suitcase[-2:]
print(last_two_elements) # Output: ['pajamas', 'books']
slice_off_last_three = suitcase[:-3]
print(slice_off_last_three) # Output: ['shirt', 'shirt', 'pants']
print("----------------------------------")
# Practise 26
print("Practise #26")
letters = ["m", "i", "s", "s", "i", "s", "s", "i", "p", "p", "i"]
num_i = letters.count("i")
print(num_i) # Output: 4
number_collection = [[100, 200], [100, 200], [475, 29], [34, 34]]
num_pairs = number_collection.count([100, 200])
print(num_pairs) # Output: 2
print("----------------------------------")
# Practise 27
print("Practise #27")
names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
names.sort()
print(names) # ['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']
names.sort(reverse=True)
print(names) # ['Xander', 'Willow', 'Giles', 'Buffy', 'Angel']
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
sorted_cities = cities.sort()
print(sorted_cities) # Output: None
# Note: The .sort() method does not return any value and thus does not need to be assigned to a variable. This is why we will see the value of None as our output for sorted_cities
cities.sort()
print(cities) # ['London', 'Los Angeles', 'New York', 'Paris', 'Rome']
cities.sort(reverse=True)
print(cities) # ['Rome', 'Paris', 'New York', 'Los Angeles', 'London']
print("----------------------------------")
# Practise 28
print("Practise #28")
names1 = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
sorted_names = sorted(names1)
print(sorted_names) # ['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']
print("----------------------------------")
# Exercise 29
print("Exercise #29")
print("Append Sum")
# Write a function named append_sum that has one parameter - a list named lst.
# The function should add the last two elements of lst together and append the result to lst. It should do this process three times and then return lst.
# For example, if lst started as [1, 1, 2], the final result should be [1, 1, 2,3, 5, 8]

def append_sum(lst):
  addTwoElements = lst[-2] + lst[-1]
  lst.append(addTwoElements)
  addTwoElements2 = lst[-2] + lst[-1]
  lst.append(addTwoElements2)
  addTwoElements3 = lst[-2] + lst[-1]
  lst.append(addTwoElements3)
  return lst

print(append_sum([1, 1, 3]))
# Output: [1, 1, 3, 4, 7, 11]  
print("----------------------------------")
# Exercise 30
print("Exercise #30")
print("More Than N")
# Create a function named more_than_n that has three parameters named lst, item, and n.
# The function should return True if item appears in the list more than n times. The function should return False otherwise.
def more_than_n(lst, item, n):
  if lst.count(item) > n:
    return True
  else:
    return False 

print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3)) # True
print(more_than_n([2, 3, 4], 2, 1)) # False
print("----------------------------------")
# Exercise 31
print("Exercise #31")
print("Middle Item")
# Create a function called middle_element that has one parameter named lst.
# If there are an odd number of elements in lst, the function should return the middle element. If there an even number of elements, the function should return the average of the middle two elements.
def middle_element(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2) - 1] + lst[int(len(lst)/2)]
    # مافهمته هنا ان النصف الأول يقوم بتحديد مكان الأندكس الذي نريده
    # ثم يقوم بإضافة ذلك مرة آخرى لتحديد مكان العنصر الذي بعده
    # لكن!! لماذا  ناقص واحد؟؟ هذا ما أريد ان افهمه
    # برجاء توضيح وظيفة ناقص واحد
    # الشرح:
    # لأن اللينجث يبدأ من 1 والأندكس يبدأ من صفر . المصفوفة الاولى طولها 6 لو قسمتها على اثنين بيعطيك 3 . 3 بتشير للرقم 4 - في المصفوفة الاولى فتحتاج تنقص منه 1 عشان تاخذ العنصر الي قبله
    return sum / 2 
  else:
    return lst[int(len(lst)/2)]

print(middle_element([5, 2, -7, -4, 4, 5])) # - 5.5
print(middle_element([3, 5, 11, 2, 4, 8, 9])) # 2
print("----------------------------------")
# Exercise 32
print("Exercise #32")
print("Append Size")
# Create a function called append_size that has one parameter named lst.
# The function should append the size of lst (inclusive) to the end of lst. The function should then return this new list.
# For example, if lst was [23, 42, 108], the function should return [23, 42, 108, 3] because the size of lst was originally 3.
def append_size(lst):
  lst.append(len(lst))
  return lst

print(append_size([23, 42, 108]))  # [23, 42, 108, 3]
print(append_size([13, 90, 430, 88, 67])) #[13, 90, 430, 88, 67, 5]
print("----------------------------------")
# Exercise 33
print("Exercise #33")
print("Larger List")
# Write a function named larger_list that has two parameters named lst1 and lst2.
# The function should return the last element of the list that contains more elements. If both lists are the same size, then return the last element of lst1
def larger_list(lst1, lst2):
  if len(lst1) >= len(lst2):
    return lst1[-1]
  else:
    return lst2[-1]    

print(larger_list([5, 9, 7],[2, 10, 46, 87, 23])) # 23
print(larger_list([2, 10, 46, 87],[5, 9, 7])) # 87
print("----------------------------------")
# Exercise 34
print("Exercise #34")
print("Combine Sort")
# Write a function named combine_sort that has two parameters named lst1 and lst2.
# The function should combine these two lists into one new list and sort the result.
# Return the new sorted list.
def combine_sort(lst1, lst2):
  combined_list = lst1[0:] + lst2[0:]
  sorted_list = sorted(combined_list)
  return sorted_list

print(combine_sort([4, 8, 6],[3, 5, 7])) # [3, 4, 5, 6, 7, 8]
print("----------------------------------")
# Exercise 35
print("Exercise #35")
print("Every Three Numbers")
# Create a function called every_three_nums that has one parameter named start.
# The function should return a list of every third number between start and 100 (inclusive). For example, every_three_nums(91) should return the list [91, 94, 97, 100]. If start is greater than 100, the function should return an empty list
def every_three_nums(start):
  return list(range(start, 101, 3))

print(every_three_nums(82)) # [82, 85, 88, 91, 94, 97, 100]
print("----------------------------------")
# Exercise 36
print("Exercise #36")
print("Remove Middle")
# Create a function named remove_middle which has three parameters named lst, start, and end.
# The function should return a list where all elements in lst with an index between start and end (inclusive) have been removed.
# For example, the following code should return [4, 23, 42] because elements at indices 1, 2, and 3 have been removed:
# remove_middle([4, 8, 15, 16, 23, 42], 1, 3)
def remove_middle(lst, start, end):
  result = lst[:start] + lst[end+1:]
  return result 

# [01]
print("-----[01]-----")
print(remove_middle([4, 8, 15, 16, 23, 42], 0, 1)) # [15, 16, 23, 42]
print(remove_middle([4, 8, 15, 16, 23, 42], 0, 2)) # [16, 23, 42]
print(remove_middle([4, 8, 15, 16, 23, 42], 0, 3)) # [23, 42]
print(remove_middle([4, 8, 15, 16, 23, 42], 0, 4)) # [42]
print(remove_middle([4, 8, 15, 16, 23, 42], 0, 5)) # []
# [02]
print("-----[02]-----")
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 0))
# [4, 8, 15, 16, 23, 42]
print(remove_middle([4, 8, 15, 16, 23, 42], 2, 0)) 
# [4, 8, 8, 15, 16, 23, 42]
print(remove_middle([4, 8, 15, 16, 23, 42], 3, 0))
# [4, 8, 15, 8, 15, 16, 23, 42]
print(remove_middle([4, 8, 15, 16, 23, 42], 4, 0))
# [4, 8, 15, 16, 8, 15, 16, 23, 42]
print(remove_middle([4, 8, 15, 16, 23, 42], 5, 0))
# [4, 8, 15, 16, 23, 8, 15, 16, 23, 42]
# [03]
print("-----[03]-----")
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 2)) # [4, 16, 23, 42]
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3)) # [4, 23, 42]
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 4)) # [4, 42]
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 5)) # [4]
# [04]
print("-----[04]-----")
print(remove_middle([4, 8, 15, 16, 23, 42], 5, 1)) 
# [4, 8, 15, 16, 23, 15, 16, 23, 42]
print(remove_middle([4, 8, 15, 16, 23, 42], 4, 1)) 
# [4, 8, 15, 16, 15, 16, 23, 42]
print(remove_middle([4, 8, 15, 16, 23, 42], 3, 1))
[4, 8, 15, 15, 16, 23, 42]
print(remove_middle([4, 8, 15, 16, 23, 42], 2, 1))
# [4, 8, 15, 16, 23, 42]
# [05]
print("-----[05]-----")
print(remove_middle([4, 8, 15, 16, 23, 42], 2, 3)) # [4, 8, 23, 42]
print(remove_middle([4, 8, 15, 16, 23, 42], 2, 4)) # [4, 8, 42]
print(remove_middle([4, 8, 15, 16, 23, 42], 2, 5)) # [4, 8]
# [06]
print("-----[06]-----")
print(remove_middle([4, 8, 15, 16, 23, 42], 5, 2))
# [4, 8, 15, 16, 23, 16, 23, 42]
print(remove_middle([4, 8, 15, 16, 23, 42], 4, 2)) 
# [4, 8, 15, 16, 16, 23, 42]
print(remove_middle([4, 8, 15, 16, 23, 42], 3, 2))
# [4, 8, 15, 16, 23, 42]
# [07]
print("-----[07]-----")
print(remove_middle([4, 8, 15, 16, 23, 42], 3, 4)) # [4, 8, 15, 42]
print(remove_middle([4, 8, 15, 16, 23, 42], 3, 5)) # [4, 8, 15]
# [08]
print("-----[08]-----")
print(remove_middle([4, 8, 15, 16, 23, 42], 5, 3))
# [4, 8, 15, 16, 23, 23, 42]
print(remove_middle([4, 8, 15, 16, 23, 42], 4, 3))
# [4, 8, 15, 16, 23, 42]
# [09]
print("-----[09]-----")
print(remove_middle([4, 8, 15, 16, 23, 42], 4, 5)) # [4, 8, 15, 16]
# [10]
print("-----[10]-----")
print(remove_middle([4, 8, 15, 16, 23, 42], 5, 4)) # [4, 8, 15, 16, 23, 42]
print("----------------------------------")
# Exercise 37
print("Exercise #37")
print("More Frequent Item")
# Create a function named more_frequent_item that has three parameters named lst, item1, and item2.
# Return either item1 or item2 depending on which item appears more often in lst.
# If the two items appear the same number of times, return item1.
def more_frequent_item(lst, item1, item2):
  if lst.count(item1) >= lst.count(item2):
    return item1
  else:
    return item2

print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3)) # 3
print("----------------------------------")
# Exercise 38
print("Exercise #38")
print("More Frequent Item")
# Create a function named double_index that has two parameters: a list named lst and a single number named index.
# The function should return a new list where all elements are the same as in lst except for the element at index. The element at index should be double the value of the element at index of the original lst.
# If index is not a valid index, the function should return the original list.
# For example, the following code should return [1, 2, 6, 4] because the element at index 2 has been doubled:
# double_index([1, 2, 3, 4], 2)
# After writing your function, un-comment the call to the function that we've provided for you to test your results.
def double_index(lst, index):
  # Checks to see if index is too big
  # if index >= len(lst):
  #   return lst
  # else:
    # Gets the original list up to index
  new_lst = lst[0:index]
  # Adds double the value at index to the new list
  new_lst.append(lst[index]*2)
  # Adds the rest of the original list
  new_lst = new_lst + lst[index+1:]
  return new_lst

print(double_index([1, 2, 3, 4], 2)) # [1, 2, 6, 4]
print(double_index([3, 8, -10, 12], 2)) # [3, 8, -20, 12]
print("----------------------------------")
# --------- (Tuples) ---------
print("--------- (Tuples) ---------")
print("What are tuples?")
print("A Tuple is a collection of Python objects separated by commas. In someways a tuple is similar to a list in terms of indexing, nested objects and repetition but a tuple is immutable unlike lists which are mutable")
print("----------------------------------")
print("Creating tuples")
my_info = ('Mohammad', 33, 'Programmer')
print(my_info) # ('Mohammad', 33, 'Programmer')
print(my_info[0]) # Mohammad
print(my_info[1]) # 33
print(my_info[2]) # Programmer
print("----------------------------------")
# my_info[0] = 'Ahmad' 
# TypeError: 'tuple' object does not support item assignment
print("----------------------------------")
print("Unpacking tuples")
name, age, occupation = my_info
print(name) # Mohammad
print(age)  # 33
print(occupation)  # Programmer
print("----------------------------------")
one_element_tuple = (4)
print(one_element_tuple) # 4
# if we eant it in tuple we'll do like this
one_element_tuple = (4,)
print(one_element_tuple) # (4,)
print("----------------------------------")
# --------- (Combining Lists) ---------
print("--------- (Combining Lists) ---------")
# Combining Lists: The Zip Function
# Learn about a popular Python built-in function called zip().
print("The zip() function allows us to quickly combine associated data-sets without needing to rely on multi-dimensional lists. While zip() can work with many different scenarios, we are going to explore only a single one in this section.")
print("Let's use a list of student names and associated heights as our example data set:")
names = ["Jenny", "Alexus", "Sam", "Grace"]
heights = [61, 70, 67, 64]
names_and_heights = zip(names, heights)
print(names_and_heights) # <zip object at 0x0000019CEB5C98C0>
print("This zip object contains the location of this variable in our computer's memory. Convert this object into a useable list by using the built-in function list():")
converted_list = list(names_and_heights)
print(converted_list) 
# [('Jenny', 61), ('Alexus', 70), ('Sam', 67), ('Grace', 64)]
# Note: Our inner lists don't use square brackets [ ] around the values. This is because they have been converted into tuples (an immutable type of list).
# --------- (Combining Lists: Activity) ---------
print("--------- (Combining Lists: Activity) ---------")
# Use zip() to create a new variable called names_and_dogs_names that combines owners and dogs_names lists into a zip object.
# Then, create a new variable named list_of_names_and_dogs_names by calling the list() function on names_and_dogs_names.
# Print list_of_names_and_dogs_names.
owners = ["Jenny", "Alexus", "Sam", "Grace"]
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]
names_and_dogs_names = zip(owners, dogs_names)
list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)
# [('Jenny', 'Elphonse'), ('Alexus', 'Dr. Doggy DDS'), ('Sam', 'Carter'), ('Grace', 'Ralph')]