from logging import exception
import pandas as pd
import cx_Oracle
import csv



def queries(C,conn):
    # print('Inside queries function')
    if(C == 3):
        # 6.1 Notify a customer that Hey recent transaction has exceeded his overdraft amount
        curr = conn.cursor()
        curr.execute('''
        UPDATE CHECKINGS SET CK_DEPO = '0', CK_WITH = '350' where ACC_NO = '8578277273'
        ''')
        conn.commit()
        print('Withdrawal updated successfully')

        # curr2 = conn.cursor()
        # curr2.execute('''
        # DELETE FROM CHECKINGS WHERE ACC_NO = '8578277273'
        # ''')
        # conn.commit()
        # print('Successfully deleted')

        curr1 = conn.cursor()
        curr1.execute('''
        UPDATE ACCOUNT SET TRANS_DATE = SYSDATE,ACC_BAL = ACC_BAL-350 WHERE ACC_NO = '8578277273'
        ''')
        conn.commit()
        print('Updated Transaction')
        curr = conn.cursor()

        # curr.execute('''
        # INSERT INTO CHECKINGS (CK_DEPO,CK_WITH,OVERDRAFTS,ACC_NO) VALUES (696.02,16.61,6,8578277273)
        # ''')

        # curr2 = conn.cursor()
        # curr2.execute('''
        # DELETE FROM ACCOUNT WHERE ACC_NO = '8578277273'
        # ''')
        # conn.commit()
        # print('Successfully deleted in Account Table')

        curr = conn.cursor()
        curr.execute('''
        SELECT * FROM CHECKINGS
        '''
        )
        conn.commit()
        for row in curr:
            if(row[3] == 8578277273):
                acc1 = row[1]
        print('Your recent transaction =  ',acc1)

        curr = conn.cursor()
        curr.execute('''
        SELECT * FROM ACCOUNT
        '''
        )
        conn.commit()
        for row in curr:
            if(row[0] == 8578277273):
                acc2 = row[1]

        print('Your current account balance = ',acc2)
        if(acc1>acc2 or acc2<0):
            print("\n")
            print('Hey! your recent transaction has exceeded overdraft amount')





        # 6.2 Notify an employee that he has a 10 year work anniversary..
        print("\n")
        print('Employees who have completed 10 years-\n')

        curr = conn.cursor()
        curr.execute('''
        SELECT * FROM EMPLOYEE
        '''
        )

        conn.commit()
        for row in curr:
            if(row[4] == 10):
                empName = row[2]
                print('Congrats ' +empName+' on your 10 years of Work Anniversay!')

