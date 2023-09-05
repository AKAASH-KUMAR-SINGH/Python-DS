import os
from itertools import islice
from scipy import pi
import numpy as np

DATA_FOLDER ='driving-datasets-master'
TRAIN_FILE= os.path.join(DATA_FOLDER,'data.txt')
LIMIT=None


split=0.8
X=[]
y=[]

with open(TRAIN_FILE) as fp:
    for line in islice(fp,LIMIT):
        path,angle=line.strip().split()
        full_path=os.path.join(DATA_FOLDER,path)
        x.append(full_path)

        y.append(float(angle)*pi/100)

        y=np.array(y)
        print("Successful!!!")