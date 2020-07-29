question 1
#Accept a String input
# Accept a search String to search in the above input
# Verify if the search String is present in the input string and the position and number of occurrences


# In[2]:


import re 
 
MyString1 =  " I want to go to Finland because the landscape is beatiful."
MyString2 ="land"
  
if re.search( MyString2, MyString1 ): 
    print("YES,string '{0}' is present in string '{1}' " .format(MyString2,MyString1)) 
else: 
    print("NO,string '{0}' is not present in string {1} " .format(MyString2, MyString1) ) 


# In[17]:



# occurrences of path
def countFreq(pat, txt): 
  k = len(pat) 
  o = len(txt) 
  res = 0
    
  
  for i in range(o - k + 1): 
        
        
      j = 0
      for j in range(k): 
          if (txt[i + j] != pat[j]): 
              break

      if (j == k - 1): 
          res += 1
          j = 0
  return res 
    

if __name__ == '__main__': 
  txt = "I want to go to Finland because the landscape is beatiful."
  pat = "want"
  print(countFreq(pat, txt)) 
  

 


# In[22]:


#position
def isSubstring(s1, s2): 
    k = len(s1) 
    o = len(s2) 
  
    
    for i in range(o - k + 1): 
  
         
        for j in range(k): 
            if (s2[i + j] != s1[j]): 
                break
              
        if j + 1 == k : 
            return i 
  
    return -1
  
 
if __name__ == "__main__": 
    s1 = "want"
    s2 = "I want to go to Finland because the landscape is beatiful."
    res = isSubstring(s1, s2) 
    if res == -1 : 
        print("Not present") 
    else: 
        print("Present at index " + str(res)) 
  


# In[ ]:




