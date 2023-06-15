import shutil
import cv2
import pytesseract
from pathlib import Path
import numpy as np

def recognize_numbers(image_path,pass_folder,reject_folder):
    # Load the image using OpenCV
    image = cv2.imread(image_path)
    
    # Preprocess the image (convert to grayscale and apply thresholding)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # Perform text extraction using Tesseract OCR
    text = pytesseract.image_to_string(binary, config='--psm 6')
    
    # Filter out non-numeric characters
    numbers = ''.join(filter(str.isdigit, text))
    
    return numbers

# Usage
image_path = '../InCMSImages'
result = recognize_numbers(image_path)
print('Recognized numbers:', result)
