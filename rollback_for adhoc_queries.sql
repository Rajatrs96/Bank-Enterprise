4.1	Add a new customer who is a borrower as well as a depositor - ROLLBACK

delete from CUST_ACCOUNT where C_SSN = '234-43-1242';
delete from CUST_LOAN where C_SSN = '234-43-1242';
delete from SAVINGS where ACC_NO = '2928817233';
delete from ACCOUNT where ACC_NO = '2928817233';
delete from LOAN where loan_no = '10020011';
delete from CUSTOMER where C_SSN = '234-43-1242';

4.3	Add a new employee who is a manager  - ROLLBACK

delete from EMPLOYEE where E_SSN = '565-66-1234' and E_TELNO ='4679767654';


4.5	add a new savings account for a customer - ROLLBACK

delete from SAVINGS where ACC_NO = '9928867231';
delete from ACCOUNT where ACC_NO = '9928867231';


4.6	Open a new branch for the bank - ROLLBACK

delete from BRANCH where branch_name = 'Chime';


6.1	Notify a customer that Hey recent transaction has exceeded his overdraft amount. - ROLLBACK

update checkings set ck_depo = '696.02', ck_with = '16.61' where acc_no = '8578277273';

UPDATE ACCOUNT SET TRANS_DATE = '6/2/2021',ACC_BAL = '230.4' WHERE ACC_NO = '8578277273';



