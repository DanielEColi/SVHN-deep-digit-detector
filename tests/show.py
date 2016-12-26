#-*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import cv2

def plot_contours(img, regions):
    n_regions = len(regions)
    n_rows = int(np.sqrt(n_regions)) + 1
    n_cols = int(np.sqrt(n_regions)) + 2
    
    # plot original image 
    plt.subplot(n_rows, n_cols, n_rows * n_cols-1)
    plt.imshow(img)
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
      
    for i, region in enumerate(regions):
        clone = img.copy()
        cv2.drawContours(clone, region.reshape(-1,1,2), -1, (0, 255, 0), 1)
        (x, y, w, h) = cv2.boundingRect(region.reshape(-1,1,2))
        cv2.rectangle(clone, (x, y), (x + w, y + h), (255, 0, 0), 1)
        plt.subplot(n_rows, n_cols, i+1), plt.imshow(clone)
        plt.title('Contours'), plt.xticks([]), plt.yticks([])
     
    plt.show()


def plot_bounding_box(img, bounding_boxes):
    """
    Parameters:
        img (ndarray)
        
        bounding_boxes (list of ndarray) : (y1, y2, x1, x2) ordered
    """
    
    n_regions = len(bounding_boxes)
    n_rows = int(np.sqrt(n_regions)) + 1
    n_cols = int(np.sqrt(n_regions)) + 2
    
    # plot original image 
    plt.subplot(n_rows, n_cols, n_rows * n_cols-1)
    plt.imshow(img)
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
      
    for i, box in enumerate(bounding_boxes):
        clone = img.copy()
        
        y1, y2, x1, x2 = box
        cv2.rectangle(clone, (x1, y1), (x2, y2), (255, 0, 0), 1)
        plt.subplot(n_rows, n_cols, i+1), plt.imshow(clone)
        plt.title('Contours'), plt.xticks([]), plt.yticks([])
     
    plt.show()


