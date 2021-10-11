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
catalog_jcmt       = ROOT_DIR + '/data/COSMOS/Catalog/submm_JCMT/'
catalog_vla        = ROOT_DIR + '/data/COSMOS/Catalog/radio_VLA/'
catalog_irac       = ROOT_DIR + '/data/COSMOS/Catalog/nearIR_IRAC/'
catalog_mips       = ROOT_DIR + '/data/COSMOS/Catalog/midIR_MIPS/'
catalog_opt        = ROOT_DIR + '/data/COSMOS/Catalog/opt_COSMOS2015/'
catalog_crossmatch = ROOT_DIR + '/data/COSMOS/Catalog/CrossMatch/'

# image
image_jcmt  = ROOT_DIR + '/data/COSMOS/Image/submm_JCMT/'
image_vla   = ROOT_DIR + '/data/COSMOS/Image/radio_VLA/'

# table
table   = ROOT_DIR + '/data/Tables/'

# figure
figure  = ROOT_DIR + 'output/Figures/'
