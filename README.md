# Bank-Enterprise

It is a simple bank enterprise application.
It allows the customer’s data to be added into the bank database using Oracle.
The data of a customer can be updated or deleted in the database based on the requirements.

Technologies - Python, Oracle, SQL

Extended Entitiy Relationship Diagram - 

<img width="620" alt="Screenshot 2023-02-19 at 11 23 15 PM" src="https://user-images.githubusercontent.com/89614144/220016345-87d87b15-2626-4c1d-b29c-b4c3a4e65544.png">

EER To Relational Schema Mapping - 

<img width="878" alt="Screenshot 2023-02-19 at 11 22 15 PM" src="https://user-images.githubusercontent.com/89614144/220016370-4a2bc296-1bde-4afa-9657-e2dd8b163e8c.png">

Design Of Choices - 
1) Branch is the initial relation of the Bank Enterprise database.  
2) Branch entity has attributes like Branch_Name as primary key, Assets, and City.  
3) Branch offers Account which is another entity having Acc_No as the primary key and other 
attributes like Acc_Bal, Trans_Date.  
4) These Accounts are divided into two types which are Savings and Checkings. Savings and checkings 
are overlapping with each other. It has Acc_No as the referential key. Savings has the following 
attributes - Sv_Depo, Sv_With, and Int_Rate. Checkings has Sv_Depo, Sv_With, and Over_draft as 
its attributes.  
5) Employee and Branch entities are related with many to one relation respectively. Employee has 
attributes E_Ssn (primary key), E_Telno, E_Name, E_Stdate, E_Length, Mgr_Ssn. Mgr_Ssn is taken 
as multivalued attributes since several employees can have one manager.   
6) Dependent is a weak entity of Employee entity since Dependent table does not have a primary 
key. E_Ssn is the foreign key for Dependent entity referring from Employee.  
7) Employee can act as loan officer or personal banker for a particular customer.  
8) Customer can have accounts or can borrow loans from the branch.  
9) Customer has many to many relationships with Account and Loan entity.  
10) Customer entity provides the data related to the customer's Name, City, Street, and SSN where 
SSN is the primary key and is referenced by Account and Loan entities.  
11) Loan is originated from the branches. Loan entity has Loan_No as its primary key and Loan_amt. 
Loan_No is referenced by Loan_Payments is a weak entity.   
12) Loan_Payment  keeps  the  track  of  the  payments done  by  every  customer  by  storing  the 
payment_date, payment_no, and amount.

Assumptions - 

1) Instead of using Bank as an entity, we have used Branch as an initial entity to create the 
database since there were no significant attributes mentioned for creating Bank. 
2) Considering the fact that each branch is located in a particular city, the City attribute cannot be 
multivalued. 
3) Every manager is an employee of the bank. 
4) A separate entity for Dependent is created considering that an employee can have more than 
one dependent and cannot be entered into the Employee entity. 
5) D_name is considered a partial key in the Dependent entity to avoid key constraints.  
6) As per the given information Bank customers are identified by their SSN but to satisfy the 
condition of customer having more than one account C_SSN is not considered as primary key. 
7) Savings and checkings accounts are overlapping since a customer can have both savings and 
checking accounts.

Limitations - 
Only relation specified between Customer and Employee is Banker however nothing other than 
type of banker is mentioned. Hence an attribute “Type” is associated with the Banker relation. 
