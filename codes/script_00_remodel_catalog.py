"""
File: script_00_remodel_catalog.py
Name: Chia-Lin Ko
Date: Jul 23, 2021
Last Modified Date: Oct 14, 2021
------------------------
This program aims to rename and convert the original catalog 
from the archive websites to csv and fits format for analysis.
"""
import os
from astropy.table import Table

# my own packing
from path import PATH_CATALOG, PATH_ORG_CATALOG


def main():

    fn_in_lst, fn_out_lst, add_col_name_lst = read_catalog_txt('catalog.txt')

    # create the directory if not exist
    isExist = os.path.exists(PATH_CATALOG)
    if not isExist:
        os.makedirs(PATH_CATALOG)
        print(f'Create new directory: {PATH_CATALOG}')

    # remodel the catalog based on the catalog.txt file
    for i in range(len(fn_in_lst)):
        remodel_table(
            fn_in = PATH_ORG_CATALOG+fn_in_lst[i],
            fn_out = PATH_CATALOG+fn_out_lst[i],
            added_col_name=add_col_name_lst[i],
            is_save_csv=True,
            is_save_fits=True
        )
    

# Function for remodel tables
def read_catalog_txt(fn_txt):
    with open(fn_txt) as f:
        lines = f.readlines()

    # Remove prefix strings from list 
    pref = '#'
    lines = [ele for ele in lines if not ele.startswith(pref)]

    # read the txt
    fn_in_lst, fn_out_lst, add_col_name_lst = [], [], []
    for line in lines:
        seg=line[:-1].split()
        fn_in_lst.append(seg[0])
        fn_out_lst.append(seg[1])
        add_col_name_lst.append(seg[2])
    
    return  fn_in_lst, fn_out_lst, add_col_name_lst


def remodel_table(fn_in, fn_out, added_col_name=None, is_save_csv=True, is_save_fits=True):
    
    # input table format
    if 'txt' in fn_in:
        tb_format ='ascii.cds'
    elif 'fits' in fn_in:
        tb_format = 'fits'
    elif 'csv' in fn_in:
        tb_format = 'csv'

    t = Table.read(fn_in, format=tb_format)

    if added_col_name is not None:
        rename_column(t, added_col_name)

    # save the output table
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
