2.	Write queries to retrieve and print all the data you entered. Try to print the 
data so that it is easy to understand (print appropriate headings first before printing data).

SELECT * FROM BRANCH;
SELECT * FROM EMPLOYEE;
SELECT * FROM DEPENDENT;
SELECT * FROM ACCOUNT;
SELECT * FROM SAVINGS;
SELECT * FROM CHECKINGS;
SELECT * FROM LOAN;
SELECT * FROM LOAN_PAYMENT;
SELECT * FROM CUSTOMER;
SELECT * FROM CUST_ACCOUNT;
SELECT * FROM CUST_LOAN;

4.1	Add a new customer who is a borrower as well as a depositor.

INSERT INTO CUSTOMER (C_SSN,C_NAME,C_STREET,C_CITY,E_SSN) VALUES ('234-43-1242','Jan Williams','Blueridge','Orlando','340-45-6621');
INSERT INTO LOAN (LOAN_NO,LOAN_AMT,BRANCH_NAME) VALUES ('10020011','345.50','Bank of India');
INSERT INTO ACCOUNT (ACC_NO,ACC_BAL,TRANS_DATE,ACCOUNT_TYPE,BRANCH_NAME) VALUES ('2928817233','500','4/14/2022','Savings','Bank of India');
INSERT INTO SAVINGS (SV_DEPO,SV_WITH,INT_RATE,ACC_NO) VALUES ('500','0','2.0','2928817233');
INSERT INTO CUST_LOAN (C_SSN,LOAN_ID) VALUES ('234-43-1242','10020011');
INSERT INTO CUST_ACCOUNT(C_SSN,ACC_ID) VALUES ('234-43-1242','2928817233');


4.2	Are there new loan for the same customer with all loan details.
select Loan.LOAN_NO,Loan.LOAN_AMT,Loan.BRANCH_NAME from Loan, cust_loan where cust_loan.c_ssn = '234-43-1242' and cust_loan.loan_no = loan.LOAN_NO;

4.3	Add a new employee who is a manager.

INSERT INTO EMPLOYEE (E_SSN,E_TELNO,E_NAME,E_STDATE,E_LENGTH,MGR_SSN,BRANCH_NAME,E_TYPE) VALUES 
('565-66-1234','4679767654','Bruce Lee',sysdate,'0','565-66-1234','HDFC Bank','Personal Banker');

4.4	Executor loan payment transaction.
select customer.e_ssn, sum(loan.loan_amt) as loans_gained, count(loan.loan_no) as total_loans_sold
from loan inner join cust_loan on loan.loan_no = cust_loan.loan_no
inner join customer on cust_loan.c_ssn = customer.c_ssn
group by customer.e_ssn;


4.5	add a new savings account for a customer.
INSERT INTO ACCOUNT (ACC_NO,ACC_BAL,TRANS_DATE,ACCOUNT_TYPE,BRANCH_NAME) VALUES ('9928867231','0','4/16/2022','Savings','HDFC Bank');
INSERT INTO SAVINGS (SV_DEPO,SV_WITH,INT_RATE,ACC_NO) VALUES ('100','0','2.3','9928867231');


4.6	Open a new branch for the bank.
INSERT INTO BRANCH (BRANCH_NAME,ASSETS,CITY) VALUES ('Chime','1000','Frisco');

5.
select LOAN.loan_no as ACC_LOAN_NO, sum(distinct(loan.loan_amt))-sum(distinct(loan_payment.amount))  as BALANCE, NULL as type
from loan full outer join loan_payment on loan.loan_no = loan_payment.loan_no
where loan.branch_name = 'Chase Bank' group by loan.loan_no
union select account.acc_no , account.acc_bal,account.account_type as type from
account where branch_name = 'Chase Bank';


6.1 Notify a customer that Hey recent transaction has exceeded his overdraft amount.
update checkings set ck_depo = '0', ck_with = '350' where acc_no = '8578277273';
UPDATE ACCOUNT SET TRANS_DATE = SYSDATE,ACC_BAL = ACC_BAL-350 WHERE ACC_NO = '8578277273'

6.2	Notify an employee that he has a 10 year work anniversary. 

select * from employee where E_length = '10';