from logging import exception
import pandas as pd
import cx_Oracle
import csv


def dataSelection(B,conn):
    # print('Inside dataSelection')
    ans = 'N'
    if(B == 2):
        # # Establishing Connection
        # cx_Oracle.init_oracle_client(lib_dir = "/Users/rajatsingh/opt/anaconda3/lib/python3.9/site-packages/sqlalchemy/dialects/oracle/instantclient_19_8")
        # conn = cx_Oracle.connect('rxb8700/Themintoo1996@acaddbprod.uta.edu:1523/pcse1p.data.uta.edu')
        # print(conn.version)

        while(1):
            if(ans == 'N'):
                tableName = input('Enter the table you want to display - \n')
                if(tableName == 'BRANCH'):
                    QRY =  'SELECT * FROM BRANCH'
                elif(tableName == 'EMPLOYEE'):
                    QRY =  'SELECT * FROM EMPLOYEE'
                elif(tableName == 'DEPENDENT'):
                    QRY =  'SELECT * FROM DEPENDENT'
                elif(tableName == 'ACCOUNT'):
                    QRY =  'SELECT * FROM ACCOUNT'
                elif(tableName == 'LOAN'):
                    QRY =  'SELECT * FROM LOAN'
                elif(tableName == 'CUSTOMER'):
                    QRY =  'SELECT * FROM CUSTOMER'
                elif(tableName == 'LOAN_PAYMENT'):
                    QRY =  'SELECT * FROM LOAN_PAYMENT'
                elif(tableName == 'SAVINGS'):
                    QRY =  'SELECT * FROM SAVINGS'
                elif(tableName == 'CHECKINGS'):
                    QRY =  'SELECT * FROM CHECKINGS'
                elif(tableName == 'CUST_LOAN'):
                    QRY =  'SELECT * FROM CUST_LOAN'
                elif(tableName == 'CUST_ACCOUNT'):
                    QRY =  'SELECT * FROM CUST_ACCOUNT'

                curr = conn.cursor()
                curr.execute(QRY)
                conn.commit()
                for row in curr:
                    print(row)
                # print(row[0])
                ans = input("Do you want to quit? Y/N : ")
            else:
                break

