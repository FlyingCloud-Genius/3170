drop database EAS;
create database EAS;
use EAS;

create table reg_info
(   reg_id varchar(30) not null,
    reg_password varchar(16),
    primary key (reg_id)
);

create table student
(   stu_id char(15) not null,
    stu_name varchar(40),
    stu_gender int,
    stu_major varchar(50),
    stu_email varchar(30),
    stu_c_uni varchar(50),
    reg_id varchar(30),
    PRIMARY key (stu_id),
    foreign key (reg_id) references reg_info(reg_id)
);

create table stu_phones
(   stu_phone varchar(20) not null,
    stu_id char(15) not null,
    primary key (stu_phone, stu_id),
    FOREIGN key (stu_id) references student(stu_id) 
);

create table stu_interests
(   stu_interest varchar(20),
    stu_id char(15) not null,
    primary key (stu_id),
    foreign key (stu_id) references student(stu_id)
);

create table university
(   uni_id char(15) not null,
    uni_email varchar(30),
    uni_name varchar(100),
    uni_phone varchar(20),
    required_score int,
    reg_id varchar(30),
    uni_web varchar(100),
    uni_photo varchar(100),
    primary key (uni_id),
    foreign key (reg_id) references reg_info(reg_id)
);

create table uni_open_major
(   open_major varchar(50) not null,
    enrollment int,
    uni_id char(15) not null,
    primary key (uni_id, open_major),
    foreign key (uni_id) references university(uni_id)
);

create table stu_application
(   stu_app_id char(15) not null,
    stu_resume varchar(100),
    transcript varchar(100),
    recommendation varchar(50),
    paper_title varchar(100),
    conference varchar(50),
    other_comments varchar(50),
    paper_url varchar(100),
    stu_id char(15) not null,
    apply_uni_id char(15) not null,
    primary key (stu_app_id),
    foreign key (stu_id) references student(stu_id),
    foreign key (apply_uni_id) references university(uni_id)
);

create table stu_dream_majors
(   stu_dream_major varchar(20),
    stu_app_id char(15) not null,
    primary key (stu_app_id, stu_dream_major),
    foreign key (stu_app_id) references stu_application(stu_app_id)
);

create table exam
(   exam_id char(15) not null,
    exam_location varchar(100),
    exam_time DATETIME,
    primary key (exam_id)
);

create table attendance
(   stu_id char(15) not null,
    exam_id char(15) not null,
    primary key (stu_id, exam_id),
    FOREIGN key (stu_id) references student(stu_id),
    foreign key (exam_id) references exam(exam_id)
);

create table guardian
(   guardian_id char(15) not null,
    guardian_email varchar(30),
    guard_name varchar(40),
    guardian_phone varchar(20),
    reg_id varchar(30),
    primary key (guardian_id),
    foreign key (reg_id) references reg_info(reg_id)
);

create table guard
(   guardian_id char(15) not null,
    exam_id char(15) not null,
    primary key (guardian_id, exam_id),
    foreign key (guardian_id) references guardian(guardian_id),
    foreign key (exam_id) references exam(exam_id)
);

create table question_base
(   que_id char(15) not null,
    que_analysis varchar(10000),
    difficulty_level int,
    que_content varchar(10000),
    answer varchar(500),
    que_type varchar(100),
    primary key (que_id)
);

CREATE TABLE answer_sheet (
    ans_id 		CHAR(15)   NOT NULL,
    ans_answer 	varCHAR(10000),
    ans_score 	varCHAR(4),
    examinee 	CHAR(15)   NOT NULL,
    PRIMARY KEY (ans_id),
    FOREIGN KEY (examinee)
        REFERENCES student (stu_id)
);

CREATE TABLE grade (
    ans_id 	CHAR(15) NOT NULL,
    guardian_id CHAR(15) NOT NULL,
    PRIMARY KEY (ans_id , guardian_id),
    FOREIGN KEY (ans_id)
        REFERENCES answer_sheet (ans_id),
    FOREIGN KEY (guardian_id)
        REFERENCES guardian (guardian_id)
);
