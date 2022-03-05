"""
File: script_make_crossmatch.py
Name: Chia-Lin Ko
Date: Jun 09, 2021
Last Modified Date: Mar 04, 2022
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

    # cross match
    crossmatch_450um(fn_dict)
    crossmatch_1d4GHz(fn_dict)
    crossmatch_3GHz(fn_dict)

    
#-----------------------------------------------------------
# Functions for crossmatch tables
def set_filename():
    fn_dict = {}

    # original catalog
    fn_dict['fn_JCMT_450umUgne']  = '%scosmos_jcmt_450um_SEDUgne_2020cat.csv'%(PATH_CATALOG)
    fn_dict['fn_JCMT_450umLim']   = '%scosmos_jcmt_450um_2020cat.csv'%(PATH_CATALOG)
    fn_dict['fn_JCMT_450umGao']   = '%scosmos_jcmt_450um_2021cat.csv'%(PATH_CATALOG)
    fn_dict['fn_VLA_1d4GHzdp']    = '%scosmos_vla_1d4GHz_dp_2011cat.csv'%(PATH_CATALOG)
    fn_dict['fn_VLA_1d4GHzXS']    = '%scosmos_vla_1d4GHz_XS_2021cat.csv'%(PATH_CATALOG)
    fn_dict['fn_VLA_3GHzlp']      = '%scosmos_vla_3GHz_2017cat.csv'%(PATH_CATALOG)
    fn_dict['fn_VLA_3GHzAGN']     = '%scosmos_vla_3GHz_multiAGN_2017cat.csv'%(PATH_CATALOG)
    fn_dict['fn_VLA_3GHzXS']      = '%scosmos_vla_3GHz_10GHz_XS_2021cat.csv'%(PATH_CATALOG)
    fn_dict['fn_IRAC']            = '%scosmos_irac_2007cat.csv'%(PATH_CATALOG)
    fn_dict['fn_MIPS_LeFloch']    = '%scosmos_mips_24um_LeFloch_2008cat.csv'%(PATH_CATALOG)
    fn_dict['fn_MIPS_whwang']     = '%scosmos_mips_24um_whwang_2020cat.csv'%(PATH_CATALOG)

    # cross-matched catalog
    fn_dict['fn_match_3GHzlpAGN']                           = '%scosmos_match_3GHzlpAGN.csv'%(PATH_CATALOG_CROSSMATCH)
    fn_dict['fn_match_3GHzlpAGN_1d4GHzdp']                  = '%scosmos_match_3GHzlpAGN_1d4GHzdp.csv'%(PATH_CATALOG_CROSSMATCH)
    fn_dict['fn_match_3GHzlpAGN_1d4GHzXS']                  = '%scosmos_match_3GHzlpAGN_1d4GHzXS.csv'%(PATH_CATALOG_CROSSMATCH)

    # Ugne based crossmatch catalogs
    fn_dict['fn_match_UgneLim']                             = '%scosmos_match_450umUgneLim.csv'%(PATH_CATALOG_CROSSMATCH)
    fn_dict['fn_match_UgneLim_1d4GHzXS']                    = '%scosmos_match_450umUgneLim_1d4GHzXS.csv'%(PATH_CATALOG_CROSSMATCH)
    fn_dict['fn_match_UgneLim_1d4GHzXS_3GHzlp']             = '%scosmos_match_450umUgneLim_1d4GHzXS_3GHzlp.csv'%(PATH_CATALOG_CROSSMATCH)
    fn_dict['fn_match_UgneLim_1d4GHzXS_3GHzlp_irac']        = '%scosmos_match_450umUgneLim_1d4GHzXS_3GHzlp_irac.csv'%(PATH_CATALOG_CROSSMATCH)
    fn_dict['fn_match_UgneLim_1d4GHzXS_3GHzlp_mips']        = '%scosmos_match_450umUgneLim_1d4GHzXS_3GHzlp_mips.csv'%(PATH_CATALOG_CROSSMATCH)
    fn_dict['fn_match_UgneLim_1d4GHzXS_3GHzlp_mips_irac']   = '%scosmos_match_450umUgneLim_1d4GHzXS_3GHzlp_mips_irac.csv'%(PATH_CATALOG_CROSSMATCH)

    # Lim based crossmatch catalogs
    fn_dict['fn_match_Lim_1d4GHzXS']                        = '%scosmos_match_450umLim_1d4GHzXS.csv'%(PATH_CATALOG_CROSSMATCH)
    fn_dict['fn_match_Lim_1d4GHzXS_3GHzlp']                 = '%scosmos_match_450umLim_1d4GHzXS_3GHzlp.csv'%(PATH_CATALOG_CROSSMATCH)
    fn_dict['fn_match_Lim_1d4GHzXS_3GHzlp_irac']            = '%scosmos_match_450umLim_1d4GHzXS_3GHzlp_irac.csv'%(PATH_CATALOG_CROSSMATCH)
    fn_dict['fn_match_Lim_1d4GHzXS_3GHzlp_mips']            = '%scosmos_match_450umLim_1d4GHzXS_3GHzlp_mips.csv'%(PATH_CATALOG_CROSSMATCH)
    fn_dict['fn_match_Lim_1d4GHzXS_3GHzlp_mips_irac']       = '%scosmos_match_450umLim_1d4GHzXS_3GHzlp_mips_irac.csv'%(PATH_CATALOG_CROSSMATCH)

    # Gao based crossmatch catalogs
    fn_dict['fn_match_GaoLim']                             = '%scosmos_match_450umGaoLim.csv'%(PATH_CATALOG_CROSSMATCH)
    fn_dict['fn_match_GaoLim_1d4GHzXS']                    = '%scosmos_match_450umGaoLim_1d4GHzXS.csv'%(PATH_CATALOG_CROSSMATCH)
    fn_dict['fn_match_GaoLim_1d4GHzXS_3GHzlp']             = '%scosmos_match_450umGaoLim_1d4GHzXS_3GHzlp.csv'%(PATH_CATALOG_CROSSMATCH)
    fn_dict['fn_match_GaoLim_1d4GHzXS_3GHzlp_irac']        = '%scosmos_match_450umGaoLim_1d4GHzXS_3GHzlp_irac.csv'%(PATH_CATALOG_CROSSMATCH)
    fn_dict['fn_match_GaoLim_1d4GHzXS_3GHzlp_mips']        = '%scosmos_match_450umGaoLim_1d4GHzXS_3GHzlp_mips.csv'%(PATH_CATALOG_CROSSMATCH)
    fn_dict['fn_match_GaoLim_1d4GHzXS_3GHzlp_mips_irac']   = '%scosmos_match_450umGaoLim_1d4GHzXS_3GHzlp_mips_irac.csv'%(PATH_CATALOG_CROSSMATCH)

    return fn_dict

def adjust_450umLim(fn, col_name):
    
    df = pd.read_csv(fn)

    # rename RA and Dec
    df = df.rename(columns={'RA_450_450umLim':'RA_450umLim'})
    df = df.rename(columns={'DEC_450_450umLim':'DEC_450umLim'})

    # add_first_column_as_index
    df = df.drop([col_name], axis=1, errors='ignore')
    df.insert(0,col_name, df.index)

    df.to_csv(fn, index=False, header=True)

def split_column_to_another_column(fn, column_name, new_column_name):
    df = pd.read_csv(fn)
    df = df.drop([new_column_name], axis=1, errors='ignore')
    df.insert(0, new_column_name, df[column_name].str.split("_",expand=True)[1])
    df.to_csv(fn, index=False, header=True)

def crossmatch_450um(fn_dict):

    input_dict = {} # filename, column_ra, column_dec
    input_dict['JCMT_450umUgne']   = [fn_dict['fn_JCMT_450umUgne'] ]
    input_dict['JCMT_450umGao']    = [fn_dict['fn_JCMT_450umGao'],   'RA_450umGao',     'Dec_450umGao']
    input_dict['JCMT_450umLim']    = [fn_dict['fn_JCMT_450umLim'],   'RA_450umLim',     'DEC_450umLim']

    # create the ID_450umLim for the 450umLim and the 450SEDUgne csv files
    adjust_450umLim(fn_dict['fn_JCMT_450umLim'], 'ID_450umLim')
    split_column_to_another_column(fn_dict['fn_JCMT_450umUgne'], 'ID_450umSEDUgne', 'ID_450umLim')

    # cross match with JCMT 450 um, Lim
    do_merge_value(input_dict, f1_key= 'JCMT_450umUgne', f2_key = 'JCMT_450umLim', 
        f1_value='ID_450umLim', f2_value='ID_450umLim', join_type = 'inner', fn_match = fn_dict['fn_match_UgneLim'] )    
    do_merge_radec(input_dict, f1_key= 'JCMT_450umGao',  f2_key = 'JCMT_450umLim', radius=4, fn_bestmatch = fn_dict['fn_match_GaoLim'])

def set_450umID(fn_in):
    # Ugne SED

    df = pd.read_csv(fn_in)
    df.insert(0,'ID_450umLim', df.index)

    # Lim 
    df = pd.read_csv(fn_in)
    df.insert(0,'ID_450umLim', df['ID_450umSEDUgne'].str.split("_",expand=True)[1])

def crossmatch_1d4GHz(fn_dict):  

    input_dict = {} # filename, column_ra, column_dec
    input_dict['VLA_1d4GHzXS']      = [fn_dict['fn_VLA_1d4GHzXS'],     'RA_1d4GHzXS',       'DEC_1d4GHzXS']
    input_dict['match_UgneLim']     = [fn_dict['fn_match_UgneLim'],    'RA_450umLim',       'DEC_450umLim']
    input_dict['JCMT_450umLim']     = [fn_dict['fn_JCMT_450umLim'],    'RA_450umLim',       'DEC_450umLim']
    input_dict['match_GaoLim']      = [fn_dict['fn_match_GaoLim'],     'RA_450umGao',       'Dec_450umGao']

    do_merge_radec(input_dict, f1_key= 'match_UgneLim', f2_key = 'VLA_1d4GHzXS', radius=3, fn_bestmatch = fn_dict['fn_match_UgneLim_1d4GHzXS'])
    do_merge_radec(input_dict, f1_key= 'JCMT_450umLim', f2_key = 'VLA_1d4GHzXS', radius=3, fn_bestmatch = fn_dict['fn_match_Lim_1d4GHzXS'])
    do_merge_radec(input_dict, f1_key= 'match_GaoLim',  f2_key = 'VLA_1d4GHzXS', radius=3, fn_bestmatch = fn_dict['fn_match_GaoLim_1d4GHzXS'])

def crossmatch_3GHz(fn_dict):

    input_dict = {} # filename, column_ra, column_dec
    input_dict['VLA_3GHzlp']                = [fn_dict['fn_VLA_3GHzlp']  ]
    input_dict['VLA_3GHzAGN']               = [fn_dict['fn_VLA_3GHzAGN'] ]
    input_dict['VLA_3GHzlpAGN']             = [fn_dict['fn_match_3GHzlpAGN'],               'ra_3GHzlp',    'dec_3GHzlp']
    input_dict['VLA_1d4GHzdp']              = [fn_dict['fn_VLA_1d4GHzdp'],                  'ra_1d4GHzdp',  'dec_1d4GHzdp']
    input_dict['VLA_1d4GHzXS']              = [fn_dict['fn_VLA_1d4GHzXS'],                  'RA_1d4GHzXS',  'DEC_1d4GHzXS']
    
    input_dict['VLA_3GHzlpAGN_1d4GHzdp']    = [fn_dict['fn_match_3GHzlpAGN_1d4GHzdp'],    'ra_3GHzlp',      'dec_3GHzlp']
    input_dict['VLA_3GHzlpAGN_1d4GHzXS']    = [fn_dict['fn_match_3GHzlpAGN_1d4GHzXS'],    'ra_3GHzlp',      'dec_3GHzlp']

    input_dict['match_UgneLim_1d4GHzXS']    = [fn_dict['fn_match_UgneLim_1d4GHzXS'],    'RA_450umLim',    'DEC_450umLim']
    input_dict['match_Lim_1d4GHzXS']        = [fn_dict['fn_match_Lim_1d4GHzXS'],        'RA_450umLim',    'DEC_450umLim']
    input_dict['match_GaoLim_1d4GHzXS']     = [fn_dict['fn_match_GaoLim_1d4GHzXS'],     'RA_450umGao',    'Dec_450umGao']
    
    do_merge_value(input_dict, f1_key= 'VLA_3GHzlp', f2_key = 'VLA_3GHzAGN', 
        f1_value='id_3GHzlp', f2_value='ID_VLA_3GHzMultiAGN', join_type = 'outer', fn_match = fn_dict['fn_match_3GHzlpAGN'])
    do_merge_radec(input_dict, f1_key= 'VLA_3GHzlpAGN', f2_key = 'VLA_1d4GHzdp', radius=1, fn_bestmatch = fn_dict['fn_match_3GHzlpAGN_1d4GHzdp'])
    do_merge_radec(input_dict, f1_key= 'VLA_3GHzlpAGN', f2_key = 'VLA_1d4GHzXS', radius=1, fn_bestmatch = fn_dict['fn_match_3GHzlpAGN_1d4GHzXS'])

    do_merge_radec(input_dict, f1_key= 'match_UgneLim_1d4GHzXS',f2_key = 'VLA_3GHzlpAGN_1d4GHzXS', radius=4, fn_bestmatch = fn_dict['fn_match_UgneLim_1d4GHzXS_3GHzlp'])
    do_merge_radec(input_dict, f1_key= 'match_Lim_1d4GHzXS',    f2_key = 'VLA_3GHzlpAGN_1d4GHzXS', radius=4, fn_bestmatch = fn_dict['fn_match_Lim_1d4GHzXS_3GHzlp'])
    do_merge_radec(input_dict, f1_key= 'match_GaoLim_1d4GHzXS', f2_key = 'VLA_3GHzlpAGN_1d4GHzXS', radius=4, fn_bestmatch = fn_dict['fn_match_GaoLim_1d4GHzXS_3GHzlp'])
    #set_RadioDet(fn_dict['fn_match_UgneLim_1d4GHzXS_3GHzlp'],   fn_dict['fn_match_UgneLim_1d4GHzXS_3GHzlp'])
    #set_RadioDet(fn_dict['fn_match_Lim_1d4GHzXS_3GHzlp'],       fn_dict['fn_match_Lim_1d4GHzXS_3GHzlp'])
    #set_RadioDet(fn_dict['fn_match_GaoLim_1d4GHzXS_3GHzlp'],    fn_dict['fn_match_GaoLim_1d4GHzXS_3GHzlp'])

def set_RadioDet(fn_in, fn_out):

    df = pd.read_csv(fn_in)
    df['ra_radio']      = np.where(df['ra_3GHzlp'].notna(), df['ra_3GHzlp'], df['RA_1d4GHzXS'])
    df['ra_err_radio']  = np.where(df['ra_3GHzlp'].notna(), df['ra_err_3GHzlp'], df['E_RA_1d4GHzXS'])
    df['dec_radio']     = np.where(df['ra_3GHzlp'].notna(), df['dec_3GHzlp'], df['DEC_1d4GHzXS'])
    df['dec_err_radio'] = np.where(df['ra_3GHzlp'].notna(), df['dec_err_3GHzlp'], df['E_DEC_1d4GHzXS'])
    df['radio_det']     = np.where(df['ra_3GHzlp'].notna(), '3',
                                   np.where(df['RA_1d4GHzXS'].notna(), '1.4', np.nan))

    if 'Unnamed: 0' in df.columns:
        df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)

    # save csv
    df.to_csv(fn_out, index=True, header=True)
    print('Save matched catalog %s'%(fn_out))


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
        df_m.to_csv(fn_match, index=False, header=True)
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
        df_m.to_csv(fn_allmatch, index=False, header=True)
        print('Save all-match catalog %s'%(fn_allmatch))
    if fn_bestmatch is not None:
        df_bm.to_csv(fn_bestmatch, index=False, header=True)
        print('Save best-match catalog %s'%(fn_bestmatch))
    if fn_innerjoin is not None:
        df_bmi.to_csv(fn_innerjoin, index=False, header=True)
        print('Save best-match, inner join catalog %s'%(fn_innerjoin))
    

if __name__ == '__main__':
    main()
