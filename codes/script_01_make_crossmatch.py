"""
File: script_make_crossmatch.py
Name: Chia-Lin Ko
Date: Jun 09, 2021
Last Modified Date: Nov 05, 2021
------------------------
This program aims to crossmatch tables.
"""
import numpy as np
import pandas as pd
import os

# my own packing
from path import PATH_CATALOG, PATH_CATALOG_CROSSMATCH
import FuncTableCrossmatch as tc


def main():

    fn_dict = set_filename()

    # create the directory if not exist
    isExist = os.path.exists(PATH_CATALOG_CROSSMATCH)
    if not isExist:
        os.makedirs(PATH_CATALOG_CROSSMATCH)
        print(f'Create new directory: {PATH_CATALOG_CROSSMATCH}')

    # create the ID_450umLim for the 450umLim and the 450SEDUgne csv files
    add_first_column_as_index(fn_dict['fn_JCMT_450um_Lim'], 'ID_450umLim')
    split_column_to_another_column(fn_dict['fn_JCMT_450um_Ugne'], 'ID_450umSEDUgne', 'ID_450umLim')
    crossmatch_450um(fn_dict)

    

def set_filename():
    fn_dict = {}

    # original catalog
    fn_dict['fn_JCMT_450um_Ugne']  = '%scosmos_jcmt_450um_SEDUgne_2020cat.csv'%(PATH_CATALOG)
    fn_dict['fn_JCMT_450um_Lim']   = '%scosmos_jcmt_450um_2020cat.csv'%(PATH_CATALOG)
    fn_dict['fn_JCMT_450um_Gao']   = '%scosmos_jcmt_450um_2021cat.csv'%(PATH_CATALOG)

    # Ugne based crossmatch catalogs
    fn_dict['fn_match_Ugne_Lim']                            = '%scosmos_match_450um_Ugne_Lim.csv'%(PATH_CATALOG_CROSSMATCH)

    # Gao based crossmatch catalogs
    fn_dict['fn_match_Gao_Lim']                             = '%scosmos_match_450um_Gao_Lim.csv'%(PATH_CATALOG_CROSSMATCH)


    return fn_dict

def add_first_column_as_index(fn, col_name):
    df = pd.read_csv(fn)
    df = df.drop([col_name], axis=1, errors='ignore')
    df.insert(0,col_name, df.index)
    df.to_csv(fn, index=True, header=True)

def split_column_to_another_column(fn, column_name, new_column_name):
    df = pd.read_csv(fn)
    df = df.drop([new_column_name], axis=1, errors='ignore')
    df.insert(0, new_column_name, df[column_name].str.split("_",expand=True)[1])
    df.to_csv(fn, index=True, header=True)


def crossmatch_450um(fn_dict):

    fn_Ugne         = fn_dict['fn_JCMT_450um_Ugne']
    fn_Lim          = fn_dict['fn_JCMT_450um_Lim']
    fn_Gao          = fn_dict['fn_JCMT_450um_Gao']
    fn_Ugne_Lim     = fn_dict['fn_match_Ugne_Lim']
    fn_Gao_Lim      = fn_dict['fn_match_Gao_Lim']

    input_dict = {} # filename, column_ra, column_dec
    input_dict['JCMT_450um_Ugne']   = [fn_Ugne]
    input_dict['JCMT_450um_Gao']    = [fn_Gao,   'RA_450umGao',    'Dec_450umGao']
    input_dict['JCMT_450um_Lim']    = [fn_Lim,   'RA_450_450umLim',    'DEC_450_450umLim']

    # cross match with JCMT 450 um, Lim
    do_merge_value(input_dict, f1_key= 'JCMT_450um_Ugne', f2_key = 'JCMT_450um_Lim', 
        f1_value='ID_450umLim', f2_value='ID_450umLim', join_type = 'inner', fn_match = fn_Ugne_Lim)    
    do_merge_radec(input_dict, f1_key= 'JCMT_450um_Gao',  f2_key = 'JCMT_450um_Lim', radius=4, fn_bestmatch = fn_Gao_Lim)

def set_450umID(fn_in):
    # Ugne SED

    df = pd.read_csv(fn_in)
    df.insert(0,'ID_450umLim', df.index)

    # Lim 
    df = pd.read_csv(fn_in)
    df.insert(0,'ID_450umLim', df['ID_450umSEDUgne'].str.split("_",expand=True)[1])

def do_merge_value(input_dict, f1_key, f2_key, f1_value, f2_value, join_type='inner', fn_match=None):
    # init parm
    fn_f1 = input_dict[f1_key][0]
    fn_f2 = input_dict[f2_key][0]

    print('-------------------------------------------------')
    print('Start to merge catalog %s and %s'%(f1_key, f2_key))
    df1 = pd.read_csv(fn_f1)
    df2 = pd.read_csv(fn_f2)

    df_m = df1.merge(df2, left_on=f1_value, right_on=f2_value, how=join_type, suffixes=['_1', '_2'])
    print('The match number is: %d'%(df_m.shape[0]))
    if 'Unnamed: 0' in df_m.columns:
        df_m.drop(df_m.columns[df_m.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)

    # save csv
    if fn_match is not None:
        df_m.to_csv(fn_match, index=True, header=True)
        print('Save matched catalog %s'%(fn_match))
 

def do_merge_radec(input_dict, f1_key, f2_key, radius=1, 
        fn_allmatch = None, fn_bestmatch = None, fn_innerjoin = None):

    # init parm
    fn_f1, ra_f1, dec_f1 = input_dict[f1_key]
    fn_f2, ra_f2, dec_f2 = input_dict[f2_key]

    print('-------------------------------------------------')
    print('Start to merge catalog %s and %s'%(f1_key, f2_key))
    df1 = pd.read_csv(fn_f1)
    df2 = pd.read_csv(fn_f2)
    ind, dist = tc.crossmatch_angular(  X1 = df1[[ra_f1, dec_f1]].values, 
                                        X2 = df2[[ra_f2, dec_f2]].values,
                                        max_distance = radius/3600, return_dist = True)
    df_m    = tc.merge_df(df1, df2, ind, dist)      # all match
    df_bm   = tc.best_match(df_m, df_m.columns[0])  # best match
    df_bmi  = tc.inner_join(df_bm)                  # inner join
    print('The all match number is: %d'%(df_m.shape[0]))
    print('The best match number is: %d'%(df_bm.shape[0]))
    print('The inner join best match number is: %d'%(df_bmi.shape[0]))

    # save csv
    if fn_allmatch is not None:
        df_m.to_csv(fn_allmatch, index=True, header=True)
        print('Save all-match catalog %s'%(fn_allmatch))
    if fn_bestmatch is not None:
        df_bm.to_csv(fn_bestmatch, index=True, header=True)
        print('Save best-match catalog %s'%(fn_bestmatch))
    if fn_innerjoin is not None:
        df_bmi.to_csv(fn_innerjoin, index=True, header=True)
        print('Save best-match, inner join catalog %s'%(fn_innerjoin))
    

if __name__ == '__main__':
    main()
