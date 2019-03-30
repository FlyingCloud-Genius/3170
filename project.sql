create database project;
use project;

create table register_information
(   register_id char(15) not null,
    register_password char(16) not null,
    register_name char(30) not null,
    primary key (register_id),
);

create table student
(   stu_id char(10) not null,
    stu_fname char(10) not NULL,
    stu_lname char(10) not null,
    stu_gender int not null,
    stu_birthday date not NULL,
    stu_major char(30) not null,
    stu_email char(30) not null,
    stu_c_uni char(50) not null,
    register_id char(15) not null,
    PRIMARY key (stu_id),
    foreign key (register_id) references register_information(register_id)
);

create table stu_phoone
(   stu_phonenumber char(20) not null,
    stu_id char(10) not null,
    primary key (stu_phonenumber, stu_id),
    FOREIGN key (stu_id) references student(stu_id) 
);

create table stu_interests
(   stu_interest char(20),
    stu_id char(10) not null,
    primary key (stu_id),
    foreign key (stu_id) references student(stu_id)
);

create table university
(   uni_id char(10) not null,
    uni_email char(30) not null,
    uni_name char(50) not null,
    uni_phone char(20) not null,
    required_GRE_score int not null,
    uni_address char(100) not null,
    register_id char(15) not null,
    primary key (uni_id),
    foreign key (register_id) references register_information(register_id)
);

create table uni_open_major
(   open_major char(20) not null,
    enrollment int,
    uni_id char(10) not null,
    primary key (uni_id, open_major),
    foreign key (uni_id) references university(uni_id)
);

create table stu_application
(   stu_application_id char(12) not null,
    stu_resume char(12) not null,
    recommendation char(12),
    paper_title char(30),
    conference char(15),
    other_comments char(30),
    paper_url char(50),
    stu_id char(10),
    primary key (stu_application_id),
    foreign key (stu_id) references student(stu_id)
);

create table stu_dream_majors
(   stu_dream_major char(20) not null,
    stu_application_id char(12) not null,
    primary key (stu_application_id, stu_dream_major),
    foreign key (stu_application_id) references stu_application(stu_application_id)
);

create table GRE_exam
(   exam_id char(8) not null,
    exam_location char(100) not null,
    exam_time DATETIME not null,
    primary key (exam_id),
);

create table attend
(   stu_id char(10) not null,
    exam_id char(8) not null,
    primary key (stu_id, exam_id),
    FOREIGN key (stu_id) references student(stu_id),
    foreign key (exam_id) references GRE_exam(exam_id)
);

create table guardian
(   guardian_id char(10) not null,
    guardian_email char(30) not null,
    guard_fname char(10) not null,
    guard_lname char(10) not null,
    guardian_phonenumber char(20) not null,
    primary key (guardian_id)
);

create table guard
(   guardian_id char(10) not null,
    exam_id char(10) not null,
    primary key (guardian_id, exam_id),
    foreign key (guadian_id) references guardian(guardian_id),
    foreign key (exam_id) references exam(exam_id),
);

create table question_base
(   question_id char(20) not null,
    question_analysis char(100) not null,
    difficulty_level int not null,
    quesiton_content char(200) not null,
    answer char(200) not null,
    question_type char(10) not null,
    primary key (question_id)
);

create table blank_sheet
(   

);