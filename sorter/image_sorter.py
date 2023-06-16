import shutil
import logging
from pathlib import Path

import cv2
import numpy as np

# Thresholding parameters
threshold_value = 100
max_value = 255
threshold_type = cv2.THRESH_BINARY

# configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s" , datefmt="%Y-%m-%d %H:%M:%S")
logger = logging.getLogger(__name__)

def is_image_below_threshold(image_path, size_threshold):
    """Check if the image size is below the threshold.

    If the image size is below the threshold, regardless of the thresholding result,
    the image will be moved to the reject folder.

    Args:
        image_path (str): Path to the image file.
        size_threshold (int): Size threshold in bytes.

    Returns:
        bool: True if the image size is below the threshold, False otherwise.
    """
    image_path = Path(image_path)
    size = image_path.stat().st_size
    return size < size_threshold


def process_image(image_path,pass_folder,reject_folder,size_threshold=75*1024):
    """Process an image by applying thresholding and moving it to the appropriate folder.

    Args:
        image_path (str): Path to the image file.
        pass_folder (str): Path to the pass folder for images that pass the test.
        reject_folder (str): Path to the reject folder for images that fail the test.
        size_threshold (int, optional): Size threshold in bytes. Defaults to 75*1024.
    """
    image_path = Path(image_path)
    filename = image_path.name
    image  = cv2.imread(str(image_path))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
     # Apply thresholding (src, dst, threshold value, max value, threshold type)
    _, threshold = cv2.threshold(gray, threshold_value, max_value, threshold_type)
    
    
    if np.sum(threshold) > 0:
        destination_folder = pass_folder
    else:
        destination_folder = reject_folder
        
    if is_image_below_threshold(image_path, size_threshold):
        destination_folder = reject_folder
        
    try:
        shutil.move(str(image_path), str(destination_folder / filename))
        logger.info(f"Image {image_path.name} processed moved to {destination_folder}")
    except shutil.Error as e:
        logger.error(f"Error processing image {image_path.name}: {str(e)}")
    except cv2.error as e:
        logger.error(f"Error processing image {image_path.name}: {str(e)}")