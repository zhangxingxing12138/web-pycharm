create table booktest_areas(
id int primary key,
atitle varchar(20),
pid int,
foreign key(pid) references areas(id)
);