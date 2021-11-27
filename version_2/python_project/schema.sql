DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS sessions;

CREATE TABLE employee(
    employee_id integer unique PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    type text not null,
    employee_name char not null,
    department char not null,
    pay_rate int not null
);

CREATE TABLE sessions(
    session_id integer unique primary KEY,
    employee_id int NOT NULL,
    date time not null,
    time_in date not null,
    time_out date not null,
    total_hours time not null
    -- FOREIGN KEY (employee_id) REFERENCES employee (session_id)
);
