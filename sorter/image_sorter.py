import shutil
from pathlib import Path

import cv2
import numpy as np

# Thresholding parameters
threshold_value = 100
max_value = 255
threshold_type = cv2.THRESH_BINARY


def process_image(image_path,pass_folder,reject_folder):
    image_path = Path(image_path)
    filename = image_path.name
    image  = cv2.imread(str(image_path))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, threshold_value, max_value, threshold_type)
    
    
    if np.sum(threshold) > 0:
        destination_folder = pass_folder
    else:
        destination_folder = reject_folder
        
    shutil.move(str(image_path), str(destination_folder / filename))