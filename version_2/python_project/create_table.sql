DROP TABLE IF EXISTS Sessions;

DROP TABLE IF EXISTS Employee;


CREATE TABLE Employee(
    employee_id integer unique PRIMARY KEY auto_increment,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    manager_id int,
    type text not null,
    name text not null,
    department text not null,
    pay_rate float not null
);

-- Create Table Managers(
-- 	manager_id int unique primary key auto_increment,
--     name text not null,
--     department text not null,
--     employee_id int unique,
--     foreign key(manager_id) references employee(employee_id)
-- );

CREATE TABLE Sessions(
    session_id integer unique primary KEY auto_increment,
    employee_id int not null,
    date date not null,
    time_in time not null,
    time_out time not null,
    total_hours float not null,
    foreign key (employee_id) references Employee(employee_id)
);
