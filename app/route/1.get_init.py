#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
#for dirname, _, filenames in os.walk('/kaggle/input'):
    #for filename in filenames:
        #print(os.path.join(dirname, filename))

# Any results you write to the current directory are saved as output.


# In[ ]:


import os
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
from tqdm import tqdm
import cv2
tqdm.pandas() 

import plotly.express as px
import plotly.offline as py
import plotly.figure_factory as ff
import plotly.io as pio
import plotly.graph_objects as go
pio.templates.default = "plotly_dark"
py.init_notebook_mode(connected=True)


# In[ ]:

label_df = pd.read_csv('/kaggle/input/daanforestpark/label2.csv')
label_df.head()
DATASET_DIR = '/kaggle/input/daanforestpark/DaanForestPark-20200403T141012Z-001/DaanForestPark'
