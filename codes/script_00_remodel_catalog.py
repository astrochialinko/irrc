"""
File: script_00_remodel_catalog.py
Name: Chia-Lin Ko
Date: Jul 23, 2021
Last Modified Date: Oct 13, 2021
------------------------
This program aims to rename and convert the original catalog 
from the archive websites to csv and fits format for analysis.
"""
import os
from astropy.table import Table

# my own packing
from path import PATH_CATALOG, PATH_ORG_CATALOG


def main():

    # VLA 3 GHz COSMOS-XS Survey    
    remodel_table(
        fn_in = PATH_ORG_CATALOG+'radio_VLA/COSMOS_XS/'+'apjabb77at6_mrt.txt',
        fn_out = PATH_CATALOG+'cosmos_vla_3GHz_10GHz_XS_2021cat',
        added_col_name='_3GHzXS',
        is_save_csv=True,
        is_save_fits=True
        )

    
# Function for remodel tables
def remodel_table(fn_in, fn_out, added_col_name=None, is_save_csv=True, is_save_fits=True):
    t = Table.read(fn_in, format="ascii.cds")
    if added_col_name is not None:
        rename_column(t, added_col_name)
    if is_save_csv:
        table2csv(t, fn_out+'.csv')
    if is_save_fits:
        table2fits(t, fn_out+'.fits')

def rename_column(astro_table, added_col_name):
    col_names = astro_table.colnames
    for col_name in col_names:
        astro_table.rename_column(col_name, col_name+added_col_name)

def table2csv(astro_table, fn_out):
    astro_table.write(fn_out, format='csv', overwrite=True)

def table2fits(astro_table, fn_out):
    astro_table.write(fn_out, format='fits', overwrite=True)

def table2latex(astro_table, fn_out):
    astro_table.write(fn_out, format='latex', overwrite=True)


if __name__ == '__main__':
    main()
