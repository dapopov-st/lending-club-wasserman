import os
from pathlib import Path

DATAPATH = Path('..') / 'data'
if not os.path.exists(DATAPATH):
    os.mkdir(DATAPATH)

APPROVED_LOANS_CSV = DATAPATH / 'accepted_2007_to_2018Q4.csv'

if not os.path.exists(APPROVED_LOANS_CSV):
    raise OSError(f'{APPROVED_LOANS_CSV} does not exist! Please place in the data directory.')

SELECTED_FEATURES = ['id',
                     'addr_state', # Need to dummify
                     'annual_inc',
                     'application_type', # Need to binarize 
                     'days_since_first_credit', # Derived field
                     'disbursement_method', # Need to binarize
                     'dti',
                     'earliest_cr_line',
                     'emp_length', # Need to convert to number and add NAs
                     'emp_title', # Needs to be encoded
                     'fico_score_average', # Derived field
                     #'fico_range_high', # Used to derive the average
                     #'fico_range_low', # Used to derive the average
                     'grade', # Need to dummify or be ordinal encoded
                     'home_ownership', # Need to dummify
                     'initial_list_status', # Need to dummify (binarize)
                     'installment',
                     'int_rate',
                     'issue_d',
                     'loan_amnt',
                     'open_acc', 
                     'pub_rec', 
                     'pub_rec_bankruptcies',
                     'purpose', # Need to dummify
                     'sub_grade', # Need to dummify or be ordinal encoded
                     'term', # Need to convert to integer from string
                     'verification_status',
                     'zip_code' # Need to dummify
                    ]

TARGET_COL = 'loan_status' # Only look at Fully Paid/Charged Off

VARS_TO_DUMMIFY = [ 'addr_state', 
                    'application_type',
                    'disbursement_method', 
                    'emp_title', 
                    'grade', 
                    'home_ownership', 
                    'initial_list_status', 
                    'purpose',  
                    'verification_status',
                    'zip_code'
                    ]