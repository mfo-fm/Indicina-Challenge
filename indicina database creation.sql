CREATE DATABASE CreditRiskDataWarehouse;
USE CreditRiskDataWarehouse;
-- Loan Application Dimensions Table
CREATE TABLE Loan_Application_Dim (
    Application_ID VARCHAR(50) PRIMARY KEY,
    Customer_ID VARCHAR(50),
    Loan_Amount DECIMAL(10, 2),
    Loan_Application_Date DATE,
    Credit_Score INT,
    Employment_Status VARCHAR(50),
    Annual_Income DECIMAL(10, 2),
    INDEX (Customer_ID)
);

-- Customer Bank Statement Dimensions Table
CREATE TABLE Customer_Bank_Statement_Dim (
    Transaction_ID VARCHAR(50) PRIMARY KEY,
    Customer_ID VARCHAR(50),
    Transaction_Date DATE,
    Transaction_Amount DECIMAL(10, 2),
    Narration VARCHAR(255),
    Balance DECIMAL(10, 2)
);

-- Fact Table
CREATE TABLE Loan_Fact (
    Loan_Fact_ID INT AUTO_INCREMENT PRIMARY KEY,
    Customer_ID VARCHAR(50),
    Application_ID VARCHAR(50),
    Transaction_ID VARCHAR(50),
    Loan_Amount DECIMAL(10, 2),
    Loan_Application_Date DATE,
    Credit_Score INT,
    Employment_Status VARCHAR(50),
    Annual_Income DECIMAL(10, 2),
    Transaction_Date DATE,
    Transaction_Amount DECIMAL(10, 2),
    Narration VARCHAR(255),
    Balance DECIMAL(10, 2),
    FOREIGN KEY (Customer_ID) REFERENCES Loan_Application_Dim(Customer_ID),
    FOREIGN KEY (Application_ID) REFERENCES Loan_Application_Dim(Application_ID),
    FOREIGN KEY (Transaction_ID) REFERENCES Customer_Bank_Statement_Dim(Transaction_ID),
    INDEX (Customer_ID)  
);


