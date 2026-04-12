import os

# Base directory (src/)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Project root (RMK/)
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))

# Data paths
INPUT_DIR = os.path.join(PROJECT_ROOT, "data", "input")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "data", "output")

# Supported formats
SUPPORTED_FORMATS = (".png", ".jpg", ".jpeg")

# Processing settings
RESIZE = False          # Set True if you want to resize images
RESIZE_WIDTH = 800      # Used only if RESIZE = True

# Debug / logging
DEBUG = True
