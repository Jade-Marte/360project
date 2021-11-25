DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS payroll;

CREATE TABLE user(
    id int IDENTITY(1,1) PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEST NOT NULL
);

CREATE TABLE payroll(
    id int IDENTITY(1,1) PRIMARY KEY,
    employee_id int NOT NULL,
    employee_name TEXT NOT NULL,
    client_name TEXT NOT NULL,
    session_time TIMESTAMP NOT NULL,
    payment int NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES user (id)
);
