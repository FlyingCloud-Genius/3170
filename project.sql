create database AES;
use AES;

create table reg_info
(   reg_id char(10) not null,
    reg_password varchar(16) not null,
    primary key (reg_id)
);

create table student
(   stu_id char(10) not null,
    stu_fname varchar(10) not NULL,
    stu_lname varchar(10) not null,
    stu_gender int not null,
    stu_birthday date not NULL,
    stu_major varchar(30) not null,
    stu_email varchar(30) not null,
    stu_c_uni varchar(50) not null,
    reg_id char(10) not null,
    PRIMARY key (stu_id),
    foreign key (reg_id) references reg_info(reg_id)
);

create table stu_phones
(   stu_phone varchar(20) not null,
    stu_id char(10) not null,
    primary key (stu_phone, stu_id),
    FOREIGN key (stu_id) references student(stu_id) 
);

create table stu_interests
(   stu_interest varchar(20),
    stu_id char(10) not null,
    primary key (stu_id),
    foreign key (stu_id) references student(stu_id)
);

create table university
(   uni_id char(10) not null,
    uni_email varchar(30) not null,
    uni_name varchar(50) not null,
    uni_phone varchar(20) not null,
    required_GRE_score int not null,
    uni_address varchar(100) not null,
    reg_id char(10) not null,
    primary key (uni_id),
    foreign key (reg_id) references reg_info(reg_id)
);

create table uni_open_major
(   open_major varchar(50) not null,
    enrollment int,
    uni_id char(10) not null,
    primary key (uni_id, open_major),
    foreign key (uni_id) references university(uni_id)
);

create table stu_application
(   stu_app_id char(10) not null,
    stu_resume varchar(12) not null,
    transcript varchar(4) not null,
    recommendation varchar(12),
    paper_title varchar(30),
    conference varchar(15),
    other_comments varchar(30),
    paper_url varchar(50),
    stu_id char(10) not null,
    apply_uni_id char(10) not null,
    primary key (stu_app_id),
    foreign key (stu_id) references student(stu_id),
    foreign key (apply_uni_id) references university(uni_id)
);

create table stu_dream_majors
(   stu_dream_major varchar(20) not null,
    stu_app_id char(10) not null,
    primary key (stu_app_id, stu_dream_major),
    foreign key (stu_app_id) references stu_application(stu_app_id)
);

create table GRE_exam
(   exam_id char(10) not null,
    exam_location varchar(100) not null,
    exam_time DATETIME not null,
    primary key (exam_id)
);

create table attendance
(   stu_id char(10) not null,
    exam_id char(10) not null,
    primary key (stu_id, exam_id),
    FOREIGN key (stu_id) references student(stu_id),
    foreign key (exam_id) references GRE_exam(exam_id)
);

create table guardian
(   guardian_id char(10) not null,
    guardian_email varchar(30) not null,
    guard_fname varchar(10) not null,
    guard_lname varchar(10) not null,
    guardian_phone varchar(20) not null,
    primary key (guardian_id)
);

create table guard
(   guardian_id char(10) not null,
    exam_id char(10) not null,
    primary key (guardian_id, exam_id),
    foreign key (guardian_id) references guardian(guardian_id),
    foreign key (exam_id) references GRE_exam(exam_id)
);

create table question_base
(   que_id char(10) not null,
    que_analysis varchar(10000) not null,
    difficulty_level int not null,
    que_content varchar(10000) not null,
    answer varchar(500) not null,
    que_type varchar(100) not null,
    primary key (que_id)
);

CREATE TABLE adjudicator (
    adju_id 	CHAR(10) NOT NULL,
    adju_email  varCHAR(30) NOT NULL,
    adju_phone  varCHAR(20) NOT NULL,
    adju_fname  varCHAR(10) NOT NULL,
    adju_lname  varCHAR(10) NOT NULL,
    PRIMARY KEY (adju_id)
);

CREATE TABLE blank_sheet (
    sheet_id CHAR(10) NOT NULL,
    PRIMARY KEY (sheet_id)
);

CREATE TABLE answer_sheet (
    ans_id 		CHAR(10)   NOT NULL,
    ans_answer 	varCHAR(10000)  NOT NULL,
    ans_score 	varCHAR(4),
    source_paper CHAR(10) NOT NULL,
    examinee 	CHAR(10)   NOT NULL,
    PRIMARY KEY (ans_id),
    FOREIGN KEY (source_paper)
        REFERENCES blank_sheet (sheet_id),
    FOREIGN KEY (examinee)
        REFERENCES student (stu_id)
);

CREATE TABLE grade (
    ans_id 	CHAR(10) NOT NULL,
    adju_id CHAR(10) NOT NULL,
    PRIMARY KEY (ans_id , adju_id),
    FOREIGN KEY (ans_id)
        REFERENCES answer_sheet (ans_id),
    FOREIGN KEY (adju_id)
        REFERENCES adjudicator (adju_id)
);

CREATE TABLE derive (
    sheet_id CHAR(10) NOT NULL,
    que_id 	 CHAR(10) NOT NULL,
    PRIMARY KEY (sheet_id , que_id),
    FOREIGN KEY (sheet_id)
        REFERENCES blank_sheet (sheet_id),
    FOREIGN KEY (sheet_id)
        REFERENCES question_base (que_id)
);

