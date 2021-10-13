"""
File: path.py
Name: Chia-Lin Ko
Create Date: March 7, 2021
------------------------
This program aims to set the path parameter
"""
import os

# ROOT_DIR: full path up to the irrc
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + "/.."

# catalog
PATH_CATALOG        = ROOT_DIR + '/../data/COSMOS/Catalog/'
PATH_ORG_CATALOG    = ROOT_DIR + '/../original_data/COSMOS/Catalog/'

# image
PATH_IMG    = ROOT_DIR + '/../data/COSMOS/Image/'

# table
PATH_TABLE  = ROOT_DIR + '/../data/COSMOS/Tables/'

# figure
PATH_FIGURE = ROOT_DIR + '/output/Figures/'
