#!/usr/bin/env python
# coding: utf-8

# # Assignment 2
# Let's test your knowledge!

# _____
# **Use <code>for</code>, .split(), and <code>if</code> to create a Statement that will print out words that start with 's':**

# In[11]:


st = 'Print only the words that start with s in this sentence'
for sen in st.split():
    if sen[0]=='s':
        print(sen)


# In[5]:


#Code here
 for senetence in st.split()


# ______
# **Use range() to print all the even numbers from 0 to 10.**

# In[12]:


list(range(0,11,2))


# ___
# **Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.**

# In[14]:


#Code Here
lst=[x for x in range(1,51)if x%3==0]
print(lst)


# _____
# **Go through the string below and if the length of a word is even print "even!"**

# In[51]:


st = 'Print every word in this sentence that has an even number of letters'

for a in st.split():  #split data
    if len(a)%2 ==0: #word/2
        print(f'even!{a}')
    else:
        print (a)
    
        


# In[41]:


#Code in this cell


# ____
# **Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".**

# In[18]:


#Code in this cell
for number in range(1,101):
    if number%3==0 & number %5 ==0: # t2seem 5&3
        print(f"fizzbuzz {number}\t\n")
    elif number%3 ==0:
        print(f"fizz {number}\t\n") 
    elif number%5 ==0:
        print(f"buzz {number}\t\n")
    else:
            print(f"not  {number}\t\n")
            


# ____
# **Use List Comprehension to create a list of the first letters of every word in the string below:**

# In[33]:


st = 'Create a list of the first letters of every word in this string'
list1=[s[0] for s in st.split() ]
print(list1)


# In[ ]:


#Code in this cell


# ### Great Job!
