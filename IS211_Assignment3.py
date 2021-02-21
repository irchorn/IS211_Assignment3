#!/usr/bin/env python
# coding: utf-8

# In[129]:



if __name__ == "__main__":    
    import urllib.request
    import re
    import csv


    
all_images = []
with urllib.request.urlopen('http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv') as response:
    lines = [l.decode('utf-8') for l in response.readlines()]
    csvData = csv.reader(lines)
    count = 0
    for row in csvData:
        column1 = row[0]
        x = re.findall(r"\bjpg|\bgif|\bGIF|\bjpeg|\bPNG", column1)
        if x:
            all_images.append(column1)
        count += 1

print(all_images)


    


# In[125]:


percent = (len(all_images) / count) * 100
print("Image requests account for {}% of all request".format(percent))


# In[154]:


weblog_lines=weblog.split("\r'n")
weblog_lines[0]


# In[147]:



with urllib.request.urlopen('http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv') as response:
    lines = [l.decode('utf-8') for l in response.readlines()]
    csvData = csv.reader(lines)
    
    for row in csvData:
        column3 = row[0]
        x = re.findall(r"Firefox|Chrome|InternetExplorer|Safari'", column3)
        if x:
           all_browsers.append(column3)
        count += 1

print(all_browsers)


# In[145]:


percent = (len(all_browsers) / count) * 100
print("Browser requests account for {}% of all request".format(percent))


# In[152]:


weblog.split("\r'n")


# In[176]:



with urllib.request.urlopen('http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv') as response:
    lines = [l.decode('utf-8') for l in response.readlines()]
    csvData = csv.reader(lines)
pattern = re.compile(r'(Firefox)w*')
matches = re.findall(pattern, " " .join (lines))
print("Firefox : ", len(matches))


# In[177]:


pattern = re.compile(r'(Chrome)w*')
matches = re.findall(pattern, " " .join (lines))
print("Chrome : ", len(matches))


# In[179]:


pattern = re.compile(r'(InternetExplorer)w*')
matches = re.findall(pattern, " " .join (lines))
print("Internet Explorerer : ", len(matches))


# In[180]:


pattern = re.compile(r'(Safari)w*')
matches = re.findall(pattern, " " .join (lines))
print("Safari : ", len(matches))


# In[ ]:




