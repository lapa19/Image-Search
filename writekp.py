import numpy as np
import cv2
import pickle
import os
from matplotlib import pyplot as plt

output = open('monuments.pkl', 'wb')

for f in os.listdir('monumentsdb/'):
    print f
    img1 = cv2.imread(str(os.path.join('monumentsdb/', f)), 0)
    h1, w1 = img1.shape[:2]
    img1 = cv2.resize(img1, (int(0.5 * w1), int(0.5 * h1)), interpolation=cv2.INTER_CUBIC)
    sift = cv2.xfeatures2d.SIFT_create()
    kp1, des1 = sift.detectAndCompute(img1, None)
    pickle.dump((des1, str(os.path.join('monumentsdb/', f))), output, pickle.HIGHEST_PROTOCOL)

output.close()
