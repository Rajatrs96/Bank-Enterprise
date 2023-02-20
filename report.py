from logging import exception
import pandas as pd
import cx_Oracle
import csv

def reportData(D,conn):
    if(D == 5):
        # Establishing Connection
        # cx_Oracle.init_oracle_client(lib_dir = "/Users/rajatsingh/opt/anaconda3/lib/python3.9/site-packages/sqlalchemy/dialects/oracle/instantclient_19_8")
        # conn = cx_Oracle.connect('rxb8700/Themintoo1996@acaddbprod.uta.edu:1523/pcse1p.data.uta.edu')
        # print(conn.version)
        
        curr = conn.cursor()
        curr.execute('''
        select LOAN.loan_no as ACC_LOAN_NO, sum(distinct(loan.loan_amt))-sum(distinct(loan_payment.amount)) as BALANCE, 
        NULL as type from loan full outer join loan_payment on loan.loan_no = loan_payment.loan_no
        where loan.branch_name = 'Chase Bank' group by loan.loan_no union select account.acc_no , account.acc_bal,account.account_type as type from
        account where branch_name = 'Chase Bank'
        ''')
        conn.commit()
        # curr = conn.cursor()
        print("\n")
        print("Report for Chase Bank")
        for row in curr:
            print(row)
