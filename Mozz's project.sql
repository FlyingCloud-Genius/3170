create database project;
use project;

CREATE TABLE register_information (
    reg_id 			CHAR(10) NOT NULL,
    reg_password 	CHAR(16) NOT NULL,
    reg_name 		CHAR(30) NOT NULL,
    PRIMARY KEY (reg_id)
);

CREATE TABLE student (
    stu_id 		CHAR(10) NOT NULL,
    stu_fname 	CHAR(10) NOT NULL,
    stu_lname 	CHAR(10) NOT NULL,
    stu_gender 	INT 	 NOT NULL,
    stu_birthday DATE 	 NOT NULL,
    stu_major 	CHAR(30) NOT NULL,
    stu_email 	CHAR(30) NOT NULL,
    stu_c_uni 	CHAR(50) NOT NULL,
    reg_id 		CHAR(10) NOT NULL,
    PRIMARY KEY (stu_id),
    FOREIGN KEY (reg_id) 
		REFERENCES register_information (reg_id)
);

CREATE TABLE stu_phone (
    stu_phone		CHAR(20) NOT NULL,
    stu_id 			CHAR(10) NOT NULL,
    PRIMARY KEY (stu_phone , stu_id),
    FOREIGN KEY (stu_id) 
		REFERENCES student (stu_id)
);

CREATE TABLE stu_interests (
    stu_interest 	CHAR(20) NOT NULL,
    stu_id 			CHAR(10) NOT NULL,
    PRIMARY KEY (stu_id , stu_interest),
    FOREIGN KEY (stu_id) 
		REFERENCES student (stu_id)
);

CREATE TABLE university (
    uni_id 		CHAR(10) 	NOT NULL,
    uni_email 	CHAR(30) 	NOT NULL,
    uni_name 	CHAR(50) 	NOT NULL,
    uni_phone 	CHAR(20) 	NOT NULL,
    uni_address CHAR(100) 	NOT NULL,
    reg_id 		CHAR(10) 	NOT NULL,
    required_GRE_score INT 	NOT NULL,
    PRIMARY KEY (uni_id),
    FOREIGN KEY (reg_id)
        REFERENCES register_information (reg_id)
);

CREATE TABLE uni_open_major (
    open_major CHAR(20) NOT NULL,
    university CHAR(10) NOT NULL,
    enrollment INT		NOT NULL,
    PRIMARY KEY (uni_id , open_major),
    FOREIGN KEY (university)
        REFERENCES university (uni_id)
);

CREATE TABLE application (
    app_id 			CHAR(10) NOT NULL,
    resume 			CHAR(12) NOT NULL,
    transcript		CHAR(4)	 NOT NULL,
    recommendation 	CHAR(12),
    paper_title 	CHAR(30),
    conference 		CHAR(15),
    paper_url 		CHAR(50),
    other_comments 	CHAR(30),
    applicant 		CHAR(10) NOT NULL,
    apply_uni		CHAR(10) NOT NULL,
    PRIMARY KEY (app_id),
    FOREIGN KEY (applicant)
        REFERENCES student (stu_id),
	FOREIGN KEY (apply_uni)
        REFERENCES univeristy (uni_id)
);

CREATE TABLE stu_dream_majors (
    major 		CHAR(20) NOT NULL,
    application CHAR(10) NOT NULL,
    PRIMARY KEY (application , major),
    FOREIGN KEY (application)
        REFERENCES application (app_id)
);

CREATE TABLE GRE_exam (
    exam_id 		CHAR(10)  NOT NULL,
    exam_location 	CHAR(100) NOT NULL,
    exam_time 		DATETIME  NOT NULL,
    PRIMARY KEY (exam_id)
);

CREATE TABLE attendance (
    stu_id 	CHAR(10) NOT NULL,
    exam_id CHAR(10) NOT NULL,
    PRIMARY KEY (stu_id , exam_id),
    FOREIGN KEY (stu_id)
        REFERENCES student (stu_id),
    FOREIGN KEY (exam_id)
        REFERENCES GRE_exam (exam_id)
);

CREATE TABLE guardian (
    guard_id 	CHAR(10) NOT NULL,
    guard_email CHAR(30) NOT NULL,
    guard_fname CHAR(10) NOT NULL,
    guard_lname CHAR(10) NOT NULL,
    guard_phone CHAR(20) NOT NULL,
    PRIMARY KEY (guard_id)
);

CREATE TABLE guard (
    guard_id CHAR(10) NOT NULL,
    exam_id  CHAR(10) NOT NULL,
    PRIMARY KEY (guard_id , exam_id),
    FOREIGN KEY (guard_id)
        REFERENCES guardian (guard_id),
    FOREIGN KEY (exam_id)
        REFERENCES exam (exam_id)
);

CREATE TABLE question_base (
    que_id 			 CHAR(10)  NOT NULL,
    que_analysis 	 CHAR(100) NOT NULL,
	que_type 		 CHAR(10)  NOT NULL,
    que_content 	 CHAR(200) NOT NULL,
    difficulty_level INT 	   NOT NULL,
    answer 			 CHAR(200) NOT NULL,
    PRIMARY KEY (que_id)
);

CREATE TABLE adjudicator (
    adju_id 	CHAR(10) NOT NULL,
    adju_email  CHAR(30) NOT NULL,
    adju_phone  CHAR(20) NOT NULL,
    adju_fname  CHAR(10) NOT NULL,
    adju_lname  CHAR(10) NOT NULL,
    PRIMARY KEY (adju_id)
);

CREATE TABLE blank_sheet (
    sheet_id CHAR(10) NOT NULL,
    PRIMARY KEY (sheet_id)
);

CREATE TABLE answer_sheet (
    ans_id 		CHAR(10)   NOT NULL,
    ans_answer 	CHAR(300)  NOT NULL,
    ans_score 	CHAR(4),
    source_papaer CHAR(10) NOT NULL,
    examinee 	CHAR(10)   NOT NULL,
    PRIMARY KEY (ans_id),
    FOREIGN KEY (source_paper)
        REFERENCES blank_sheet (sheet_id),
    FOREIGN KEY (examinee)
        REFERENCES stuent (stu_id)
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

    
    