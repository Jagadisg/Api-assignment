import mysql.connector

cnx = None
cn  = None
def get_sql_conn():
    global cnx
    if cnx is None:
        cnx = mysql.connector.connect(user="root",password="",host="localhost",database="login_info")

    return cnx

def get_users_conn():
    global cn
    if cn is None:
        cn = mysql.connector.connect(user="root",password="",host="localhost",database="users")

    return cn


#login query 
# CREATE DATABASE login_info;
# USE login_info;
# CREATE TABLE user_info (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     username VARCHAR(12) UNIQUE NOT NULL,
#     password VARCHAR(255) NOT NULL
# );


#sql query for sql assignment 
# CREATE DATABASE users;
# use users;
# CREATE TABLE company(companyId INT AUTO_INCREMENT PRIMARY KEY,companyName varchar(255));
# CREATE TABLE user_detail (userId INT AUTO_INCREMENT PRIMARY KEY,userName varchar(255),email varchar(255), mobile int(15), password varchar(255), companyId int,FOREIGN KEY (companyId) REFERENCES company(companyId))