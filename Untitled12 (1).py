#!/usr/bin/env python
# coding: utf-8

# In[3]:


def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)
print(fib(int(input())))


# In[ ]:




