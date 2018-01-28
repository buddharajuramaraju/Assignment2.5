
# coding: utf-8

# ### Problem Statement 1:
# Write a Python program using function concept that maps list of words into a list of
# integers representing the lengths of the corresponding words.
# Hint: ​If a list [ ab,cde,erty] is passed on to the python function output should come as
# [2,3,4]
# Here 2,3 and 4 are the lengths of the words in the list.
# 

# In[1]:


def word_length_map(wordlist):
    length_list = list(map(lambda x:len(x),wordlist))
    return length_list


# In[2]:


word_length_map(["Ramaraju","Buddharaju","Venkata"])


# ### Problem Statement 2:
# Write a Python function which takes a character (i.e. a string of length 1) and returns
# True if it is a vowel, False otherwise.

# In[10]:


def isVowel(single_char):
    if len(single_char) !=1 :
        raise Exception("Invalid Character")
    if single_char.upper() in ['A','E','I','O','U']:
        return True
    else:
        return False
        


# In[11]:


isVowel('e')


# In[12]:


isVowel('M')


# In[14]:


isVowel('A')

