DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS payroll;

CREATE TABLE user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEST NOT NULL
);

CREATE TABLE payroll(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER NOT NULL,
    employee_name TEXT NOT NULL,
    client_name TEXT NOT NULL,
    session_time TIMESTAMP NOT NULL,
    payment INTEGER NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES user (id)
);
