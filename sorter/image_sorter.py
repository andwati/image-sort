import shutil
from pathlib import Path

import cv2
import numpy as np

# Thresholding parameters
threshold_value = 100
max_value = 255
threshold_type = cv2.THRESH_BINARY


def is_image_below_threshold(image_path, size_threshold):
    """If the image size is below the threshold, regardless of the thresholding
    result, the image will be moved to the reject folder.

    Args:
        image_path (_type_): _description_
        size_threshold (_type_): _description_

    Returns:
        _type_: _description_
    """
    image_path = Path(image_path)
    size = image_path.stat().st_size
    return size < size_threshold


def process_image(image_path,pass_folder,reject_folder,size_threshold=75*1024):
    """_summary_

    Args:
        image_path (_type_): _description_
        pass_folder (_type_): _description_
        reject_folder (_type_): _description_
        size_threshold (_type_, optional): _description_. Defaults to 75*1024.
    """
    image_path = Path(image_path)
    filename = image_path.name
    image  = cv2.imread(str(image_path))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # threshold(src, dst, threshold value, max value, threshold type)
    _, threshold = cv2.threshold(gray, threshold_value, max_value, threshold_type)
    
    
    if np.sum(threshold) > 0:
        destination_folder = pass_folder
    else:
        destination_folder = reject_folder
        
    if is_image_below_threshold(image_path, size_threshold):
        destination_folder = reject_folder
        
    shutil.move(str(image_path), str(destination_folder / filename))