#!/usr/bin/env python
# coding: utf-8

import warnings
from datetime import datetime
from typing import Optional
import pandas as pd
import re

def expand_mixed(df: pd.DataFrame, types=None) -> pd.DataFrame:
    '''
    Args:
        types: list of types to expand (default: list, dict, tuple)
        df: DataFrame
    Returns:
        DataFrame with the dict values as series, identifier by combination of the series and dict keys, and datatypes inferred and converted
        '''
    #expand non-nested lists, dicts, tuples in df into columns with a prefix
    if types is None:
        types = [list, dict, tuple]
        
    for col in df.columns:
        non_nested_enumeration = (df[col].dropna().map(lambda x: type(x) in types and not any(type(y) in types for y in x)))
        
        if non_nested_enumeration.all():
            #expand and prefix
            expanded = pd.DataFrame(df[col].dropna().tolist())
            expanded = expanded.add_prefix(col + '_')
            
            #add recursion
            expanded = expand_mixed(expanded)
            
            #drop expanded
            df.drop(columns=[col], inplace=True)
            
            df = pd.concat([df, expanded], axis=1)
        return df

def dtype_inference(df: pd.DataFrame) -> pd.DataFrame:
    #applying infer_objects()
    df = df.infer_objects()
    
    #process columns with mixed dtypes
    for col in df.columns:
        weird = (df[[col]].applymap(type) != df[[col]].iloc[0].apply(type)).any(axis=1)
        if len(df[weird]) > 0:
            df = df.join(df.pop(col).str.extract("(?P<{}_numbers>\d+)?(?P<{}_text>\D+)?".format(col, col)))
    null_cols = []
    for col in df.columns:
        if df[col].isnull().sum()/len(df) == 1:
            df = df.drop(col, 1)
            null_cols.append(col)
    for col in null_cols:
        c = col.split('_')
        if c[-1] == 'text':
            c2 = c[:-1]
            c2.append('numbers')
            df = df.rename(columns={'_'.join(c2):'_'.join(c[:-1])})
        elif c[-1] == 'numbers':
            c2 = c[:-1]
            c2.append('text')
            df = df.rename(columns={'_'.join(c2):'_'.join(c[:-1])})
            
    ###DATETIME
    #identify date columns separated into day, month, year
    col_day, col_year, col_month = 0,0,0
    for col in df.columns:
        if col.lower() == 'day':
            col_day = col
        if col.lower() == 'month':
            col_month = col
        if col.lower() == 'year':
            col_year = col
            
    if col_day != 0:
        df[col_day] = df[col_day].apply(lambda x: '0'+str(x) if len(str(x))<2 else x)
        if col_month != 0:
            df[col_month] = df[col_month].apply(lambda x: '0'+str(x) if len(str(x))<2 else x)
            df['Date_combined'] = df[col_day].astype(str) + '-' + df[col_month].astype(str)
            df = df.drop([col_day, col_month], 1)
            if col_year != 0:
                df['Date_combined'] = df['Date_combined'] + '-' + df[col_year].astype(str)
                df = df.drop([col_year], 1)
    
    #identifies datetime cols; extracts from text if combined
    for col in df.columns:
        col_name = str(col) +'_datetime'
        try:
            df[col_name] = pd.to_datetime(df[col].apply(lambda x: re.search(r'\d{2}/\d{2}/\d{4}', x).group()), format='%d/%m/%Y')
            df = df.drop(col, 1)
        except (AttributeError, TypeError) as e:
            try:
                df[col_name] = pd.to_datetime(df[col].apply(lambda x: re.search(r'\d{2}-\d{2}-\d{4}', x).group()), format='%d-%m-%Y')
                df = df.drop(col, 1)      
            except (AttributeError, TypeError) as e:
                try:
                    df[col_name] = pd.to_datetime(df[col].apply(lambda x: re.search(r'\d{4}-\d{2}-\d{2}', x).group()), format='%Y-%m-%d')
                    df = df.drop(col, 1)
                except (AttributeError, TypeError) as e:
                    try:
                        df[col_name] = pd.to_datetime(df[col].apply(lambda x: re.search(r'\d{4}/\d{2}/\d{2}', x).group()), format='%Y/%m/%d')
                        df = df.drop(col, 1)
                    except (AttributeError, TypeError) as e:
                        try:
                            df[col_name] = pd.to_datetime(df[col].apply(lambda x: re.search(r'\d{2}/\d{2}/\d{2}', x).group()))
                            df = df.drop(col, 1)
                        except (AttributeError, TypeError) as e:
                            try:
                                df[col_name] = pd.to_datetime(df[col].apply(lambda x: re.search(r'\d{2}-\d{2}-\d{2}', x).group())) 
                                df = df.drop(col, 1)
                            except (AttributeError, TypeError) as e:
                                pass
        
    #remove duplicates
    duplicate_cols = set()
    for x in range(df.shape[1]):
        col = df.iloc[:,x]
        for y in range(x+1, df.shape[1]):
            other_col = df.iloc[:,y]
            if col.equals(other_col):
                duplicate_cols.add(df.columns.values[y])
    df = df.drop(columns=duplicate_cols)
    
    return df






