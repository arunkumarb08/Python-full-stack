use college1;
drop  table students;

create table students(
student_id int primary key,
name varchar(50)
);


create table course(
student_id int primary key,
course varchar(50)
);


insert into students values(101,"json"),
(102,"ravi"),
(103,"arun"),
(104,"chandra");



insert into course values(101,"c"),
(102,"python"),
(103,"c++"),
(104,"java");

select * from course;


select * from students
inner join course
on students.student_id = course.student_id;


SELECT
    students.student_id,
    students.name,
    course.course
FROM students
INNER JOIN course
ON students.student_id = course.student_id;


select 
students.name,
course.course
from students
cross join course;

