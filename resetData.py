from Data_Ins import *
from Data_Select import *
from Query import *
from report import *
from updateTrans import *

cx_Oracle.init_oracle_client(lib_dir = "/Users/rajatsingh/opt/anaconda3/lib/python3.9/site-packages/sqlalchemy/dialects/oracle/instantclient_19_8")
conn = cx_Oracle.connect('rxb8700/Themintoo1996@acaddbprod.uta.edu:1523/pcse1p.data.uta.edu')
print(conn.version)

curr = conn.cursor()
curr.execute('''
delete from CUST_ACCOUNT where C_SSN = '234-43-1242'
''')
curr.execute('''
delete from CUST_LOAN where C_SSN = '234-43-1242'
''')
curr.execute('''
delete from SAVINGS where ACC_NO = '2928817233'
''')
curr.execute('''
delete from ACCOUNT where ACC_NO = '2928817233'
''')
curr.execute('''
delete from LOAN where loan_no = '10020011'
''')
curr.execute('''
delete from CUSTOMER where C_SSN = '234-43-1242'
''')
conn.commit()
print('4.1 Successfully Deleted')

curr = conn.cursor()
curr.execute('''
delete from EMPLOYEE where E_SSN = '565-66-1234' and E_TELNO ='4679767654'
''')
conn.commit()
print('4.3 Successfully Deleted')

curr = conn.cursor()
curr.execute('''
delete from SAVINGS where ACC_NO = '9928867231'
''')
curr.execute('''
delete from ACCOUNT where ACC_NO = '9928867231'
''')
conn.commit()
print('4.5 Successfully Deleted')

curr = conn.cursor()
curr.execute('''
delete from BRANCH where branch_name = 'Chime'
''')
conn.commit()
print('4.6 Successfully Deleted')


#Reseting Trigger Statements
# print("Deleting trigger statements")
# curr = conn.cursor()
# curr.execute('''
# DELETE FROM CHECKINGS WHERE ACC_NO = '8578277273'
# ''')
# conn.commit()
# print('Successfully deleted from checkings table')

# curr2 = conn.cursor()
# curr2.execute('''
# DELETE FROM ACCOUNT WHERE ACC_NO = '8578277273'
# ''')
# conn.commit()
# print('Successfully deleted from Account Table')



# # 4.1
# delete from CUST_ACCOUNT where C_SSN = '234-43-1242';
# delete from CUST_LOAN where C_SSN = '234-43-1242';
# delete from SAVINGS where ACC_NO = '2928817233';
# delete from ACCOUNT where ACC_NO = '2928817233';
# delete from LOAN where loan_no = '10020011';
# delete from CUSTOMER where C_SSN = '234-43-1242';

# #  4.3
# #delete from EMPLOYEE where E_SSN = '565-66-1234' and E_TELNO ='4679767654';

# # 4.5
#  #delete from SAVINGS where ACC_NO = '9928867231';
# #delete from ACCOUNT where ACC_NO = '9928867231';
# # 4.6
#  #delete from BRANCH where branch_name = 'Chime';