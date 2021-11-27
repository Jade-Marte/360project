DROP TABLE IF EXISTS Employee;
DROP TABLE IF EXISTS Sessions;

CREATE TABLE Employee(
    employee_id integer unique PRIMARY KEY auto_increment,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    type text not null,
    employee_name char not null,
    department char not null,
    pay_rate float not null
);

CREATE TABLE Sessions(
    session_id integer unique primary KEY auto_increment,
    employee_id int not null,
    date time not null,
    time_in date not null,
    time_out date not null,
    total_hours time not null,
    foreign key (employee_id) references Employee(employee_id)
);
