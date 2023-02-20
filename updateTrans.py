from logging import exception
import pandas as pd
import cx_Oracle
import csv


def updateTransaction(E,conn):
    res = "Y"
    if(E == 4):
        
        while(1):
            if(res == "Y" or res == "y"):
                # print("Inside updateTrans")
                # Establishing Connection
                # cx_Oracle.init_oracle_client(lib_dir = "/Users/rajatsingh/opt/anaconda3/lib/python3.9/site-packages/sqlalchemy/dialects/oracle/instantclient_19_8")
                # conn = cx_Oracle.connect('rxb8700/Themintoo1996@acaddbprod.uta.edu:1523/pcse1p.data.uta.edu')
                # print(conn.version)
                print("\n")
                print("Select from below query options- ")
                print("1.Add a new customer who is a borrower as well as a depositor")
                print("2.Are there new loans for the same customer with all loan details")
                print("3.Add a new employee who is a manager")
                print("4.Executor loan payment transaction")
                print("5.Add a new savings account for a customer")
                print("6.Open a new branch for the bank")
                inp = input("Ans: ")

                if(inp == "1"):
                    # print("Inside inp = 1")
                    #4.1 Add a new customer who is a borrower as well as a depositor.
                    curr = conn.cursor()
                    curr.execute('''
                    INSERT INTO CUSTOMER (C_SSN,C_NAME,C_STREET,C_CITY,E_SSN) VALUES ('234-43-1242','Jan Williams','Blueridge','Orlando','340-45-6621')''')
                    curr.execute('''
                    INSERT INTO LOAN (LOAN_NO,LOAN_AMT,BRANCH_NAME) VALUES ('10020011','345.50','Bank of India')''')
                    curr.execute('''
                    INSERT INTO ACCOUNT (ACC_NO,ACC_BAL,TRANS_DATE,ACCOUNT_TYPE,BRANCH_NAME) VALUES ('2928817233','500','4/14/2022','Savings','Bank of India')''')
                    curr.execute('''
                    INSERT INTO SAVINGS (SV_DEPO,SV_WITH,INT_RATE,ACC_NO) VALUES ('500','0','2.0','2928817233')''')
                    curr.execute('''
                    INSERT INTO CUST_LOAN (C_SSN,LOAN_NO) VALUES ('234-43-1242','10020011')''')
                    curr.execute('''
                    INSERT INTO CUST_ACCOUNT(C_SSN,ACC_NO) VALUES ('234-43-1242','2928817233')''')
                    conn.commit()
                    print("Inserted new customer successfully")

                    curr.execute('''
                    select * from CUST_ACCOUNT where C_SSN = '234-43-1242'
                    ''')
                    conn.commit()
                    for row in curr:
                        print(row)
                
                elif(inp == '2'):
                    # #4.2 Are there new loan for the same customer with all loan details.

                    curr = conn.cursor()
                    curr.execute('''
                    select Loan.LOAN_NO,Loan.LOAN_AMT,Loan.BRANCH_NAME from Loan, cust_loan where cust_loan.c_ssn = '234-43-1242' and cust_loan.loan_no = loan.LOAN_NO
                    ''')
                    conn.commit()
                    print("\n")
                    print("Loan Details")
                    for row in curr:
                        print(row)

                elif(inp == '3'):
                    # print("Inside inp = 3")
                    #4.3 Add a new employee who is a manager.
                    curr = conn.cursor()
                    curr.execute('''
                    INSERT INTO EMPLOYEE (E_SSN,E_TELNO,E_NAME,E_STDATE,E_LENGTH,MGR_SSN,BRANCH_NAME,E_TYPE) VALUES ('565-66-1234','4679767654','Bruce Lee',SYSDATE,'0','565-66-1234','HDFC Bank','Personal Banker')
                    ''')
                    conn.commit()
                    print("New Employee as a manager added successfully")


                    print("\n")
                    curr = conn.cursor()
                    curr.execute('''
                    select * from Employee where E_SSN = '565-66-1234'
                    ''')
                    conn.commit()
                    for row in curr:
                        print(row)

                elif(inp == '4'):

                # # 4.4	Executor loan payment transaction.
                    curr = conn.cursor()
                    curr.execute('''
                        select customer.e_ssn, sum(loan.loan_amt) as loans_gained, count(loan.loan_no) as total_loans_sold
                        from loan inner join cust_loan on loan.loan_no = cust_loan.loan_no
                        inner join customer on cust_loan.c_ssn = customer.c_ssn group by customer.e_ssn
                    ''')
                    conn.commit()
                    print("Executor Transactions - ")
                    for row in curr:
                        print(row)

                elif(inp == '5'):
                    # print("Inside inp = 5")
                    # 4.5	add a new savings account for a customer.
                    curr = conn.cursor()
                    curr.execute('''
                    INSERT INTO ACCOUNT (ACC_NO,ACC_BAL,TRANS_DATE,ACCOUNT_TYPE,BRANCH_NAME) VALUES ('9928867231','0','4/16/2022','Savings','HDFC Bank')
                    ''')
                    curr.execute('''
                    INSERT INTO SAVINGS (SV_DEPO,SV_WITH,INT_RATE,ACC_NO) VALUES ('100','0','2.3','9928867231')
                    ''')
                    conn.commit()
                    print("Added new savings account for the customer")

                    curr.execute('''
                    select * from SAVINGS where ACC_NO = '9928867231'
                    ''')
                    conn.commit()
                    for row in curr:
                        print(row)
                
                elif(inp == '6'):
                    # print("Inside inp = 6")
                    # 4.6	Open a new branch for the bank.
                    curr = conn.cursor()
                    curr.execute('''
                    INSERT INTO BRANCH (BRANCH_NAME,ASSETS,CITY) VALUES ('Chime','1000','Frisco')
                    ''')
                    conn.commit()
                    print("Added new branch")
                    curr.execute('''
                    select * from BRANCH where BRANCH_NAME = 'Chime'
                    ''')
                    conn.commit()
                    for row in curr:
                        print(row)
                res = input("Do you wish to opt for other options - Y/N: ")
            else:
                break

