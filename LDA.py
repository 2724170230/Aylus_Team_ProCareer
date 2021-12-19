#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('nvidia-smi')


# In[3]:


import os
from google.colab import drive

drive.mount('/content/drive')
path = '/content/drive/My Drive'

os.chdir(path)
os.listdir(path)


# In[2]:


from tensorflow.python.client import device_lib
device_lib.list_local_devices()


# In[3]:


ls


# In[4]:





# In[ ]:


from pprint import pprint
from artifici_lda.lda_service import train_lda_pipeline_default


'''FR_STOPWORDS = [
    "le", "les", "la", "un", "de", "en",  # stop words
    "a", "b", "c", "d",  # 1 char words are removed too
    "est", "sur", "tres", "donc", "sont",  # can even mix in some more common words / borderline stop words.
    # even having slang/texto stop words can be good:
    "ya", "pis", "yer"]
# Note: this list of stop words is poor and has been crafted for this example.
'''
FR_STOPWORDS = [","]


fr_comments = concepts

transformed_comments, top_comments, _1_grams, _2_grams = train_lda_pipeline_default(
    fr_comments,
    n_topics=2,
    stopwords=FR_STOPWORDS,
    language='french')
# More languages: 
# ['danish', 'dutch', 'english', 'finnish', 'french', 'german', 'hungarian', 'italian', 
#  'norwegian', 'porter', 'portuguese', 'romanian', 'russian', 'spanish', 'swedish', 'turkish']

pprint(transformed_comments)
pprint(top_comments)
pprint(_1_grams)
pprint(_2_grams)


# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("data_with_concepts.csv")


# In[3]:


data.dropna(inplace=True)


# In[3]:


data.head()


# In[4]:


concepts = data['concepts'].tolist()


# In[5]:


divided_concepts = []
for concept in concepts:
  concept = concept[:-1]
  for i in range(len(concept.split(","))):
    divided_concepts.append(concept.split(",")[i])
    if i == 2:
      break


# In[6]:


len(divided_concepts)


# In[ ]:





# In[ ]:





# In[ ]:





# In[12]:


small_concept = divided_concepts[:1500]


# In[33]:


small_concept


# In[ ]:


from pprint import pprint
from artifici_lda.lda_service import train_lda_pipeline_default


'''FR_STOPWORDS = [
    "le", "les", "la", "un", "de", "en",  # stop words
    "a", "b", "c", "d",  # 1 char words are removed too
    "est", "sur", "tres", "donc", "sont",  # can even mix in some more common words / borderline stop words.
    # even having slang/texto stop words can be good:
    "ya", "pis", "yer"]
# Note: this list of stop words is poor and has been crafted for this example.
'''
FR_STOPWORDS = [","]


fr_comments = divided_concepts[:1000]

transformed_comments, top_comments, _1_grams, _2_grams = train_lda_pipeline_default(
    fr_comments,
    n_topics=50,
    stopwords=FR_STOPWORDS,
    language='englsh')
# More languages: 
# ['danish', 'dutch', 'english', 'finnish', 'french', 'german', 'hungarian', 'italian', 
#  'norwegian', 'porter', 'portuguese', 'romanian', 'russian', 'spanish', 'swedish', 'turkish']

pprint(transformed_comments)
pprint(top_comments)
pprint(_1_grams)
pprint(_2_grams)

dic = {}
for i in range(len(transformed_comments)):
  comments = transformed_comments[i].tolist()
  index = comments.index(max(comments))
  if top_comments[index] not in dic.keys():
    dic[top_comments[index]] = []
    dic[top_comments[index]].append(small_concept[i])
  else:
    dic[top_comments[index]].append(small_concept[i])
processed_data = pd.DataFrame(dict)
processed_data.to_csv("topic_clustering.csv")


# In[ ]:


top_comments


# In[ ]:


dic = {}
for i in range(len(transformed_comments)):
  comments = transformed_comments[i].tolist()
  index = comments.index(max(comments))
  if top_comments[index] not in dic.keys():
    dic[top_comments[index]] = []
    dic[top_comments[index]].append(small_concept[i])
  else:
    dic[top_comments[index]].append(small_concept[i])


# In[ ]:


for key in dic.keys():
  print(key)
  print(dic[key])


# In[ ]:





# In[ ]:


data.dropna(inplace=True)


# In[13]:


pip install translitcodec


# In[14]:


pip install PyStemmer


# In[23]:


pip install lda


# In[30]:


import numpy as np
import lda
import lda.datasets
X = lda.datasets.load_reuters()
print(X)
vocab = lda.datasets.load_reuters_vocab()
print("This is vocab " + str(vocab))
titles = lda.datasets.load_reuters_titles()
print("This is title: " + str(titles))
X.shape

X.sum()

model = lda.LDA(n_topics=100, n_iter=1500, random_state=1)
model.fit(X)  # model.fit_transform(X) is also available
topic_word = model.topic_word_  # model.components_ also works
n_top_words = 40
for i, topic_dist in enumerate(topic_word):
  topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words+1):-1]
  print('Topic {}: {}'.format(i, ' '.join(topic_words)))

'''
Topic 0: british churchill sale million major letters west britain
Topic 1: church government political country state people party against
Topic 2: elvis king fans presley life concert young death
Topic 3: yeltsin russian russia president kremlin moscow michael operation
Topic 4: pope vatican paul john surgery hospital pontiff rome
Topic 5: family funeral police miami versace cunanan city service
Topic 6: simpson former years court president wife south church
Topic 7: order mother successor election nuns church nirmala head
Topic 8: charles prince diana royal king queen parker bowles
Topic 9: film french france against bardot paris poster animal
Topic 10: germany german war nazi letter christian book jews
Topic 11: east peace prize award timor quebec belo leader
Topic 12: n't life show told very love television father
Topic 13: years year time last church world people say
Topic 14: mother teresa heart calcutta charity nun hospital missionaries
Topic 15: city salonika capital buddhist cultural vietnam byzantine show
Topic 16: music tour opera singer israel people film israeli
Topic 17: church catholic bernardin cardinal bishop wright death cancer
Topic 18: harriman clinton u.s ambassador paris president churchill france
Topic 19: city museum art exhibition century million churches set'''


# In[19]:


rm -r /tmp/


# In[8]:


import os
os.environ['JOBLIB_TEMP_FOLDER'] = '/tmp'


# In[ ]:




