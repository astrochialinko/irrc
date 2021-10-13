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

# original catalog
catalog_org_vla    = ROOT_DIR + '/Original_Data/COSMOS/Catalog/VLA/'

# catalog
catalog             = ROOT_DIR + '/data/COSMOS/Catalog/'
catalog_crossmatch = ROOT_DIR + '/data/COSMOS/Catalog/CrossMatch/'

# image
image_jcmt  = ROOT_DIR + '/data/COSMOS/Image/submm_JCMT/'
image_vla   = ROOT_DIR + '/data/COSMOS/Image/radio_VLA/'

# table
table   = ROOT_DIR + '/data/Tables/'

# figure
figure  = ROOT_DIR + 'output/Figures/'
