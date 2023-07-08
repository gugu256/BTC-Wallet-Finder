import cv2
import numpy as np

def fail(needle_path, haystack_path):
    # Read the images
    needle = cv2.imread(needle_path)
    haystack = cv2.imread(haystack_path)

    # Convert images to grayscale
    needle_gray = cv2.cvtColor(needle, cv2.COLOR_BGR2GRAY)
    haystack_gray = cv2.cvtColor(haystack, cv2.COLOR_BGR2GRAY)

    # Apply template matching
    result = cv2.matchTemplate(haystack_gray, needle_gray, cv2.TM_CCOEFF_NORMED)

    # Define a threshold for similarity
    threshold = 0.8

    # Find the positions where the template matches
    locations = np.where(result >= threshold)

    # Check if any match is found
    if len(locations[0]) > 0:
      return True
    else:
      return False