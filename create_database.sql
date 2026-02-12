-- Create Database
CREATE DATABASE DigitalTwinDB;
GO

USE DigitalTwinDB;

DROP TABLE IF EXISTS Academic;

CREATE TABLE Academic (
    ID INT IDENTITY(1,1) PRIMARY KEY,
    Subject VARCHAR(50),
    Hours_Studied FLOAT,
    Attendance FLOAT,
    Internal_Score FLOAT,
    Exam_Score FLOAT
);

INSERT INTO Academic VALUES
('Machine Learning', 2.5, 85, 78, 82),
('Mathematics', 3.0, 90, 80, 88),
('Linux', 1.5, 70, 65, 72);

DROP TABLE IF EXISTS Wellness;

CREATE TABLE Wellness (
    ID INT IDENTITY(1,1) PRIMARY KEY,
    Sleep_Hours FLOAT,
    Exercise_Hours FLOAT,
    Mood INT,
    Stress_Level INT,
    Wellness_Index FLOAT
);

INSERT INTO Wellness VALUES
(7, 1, 8, 3, 80),
(6, 0.5, 6, 6, 65),
(8, 1.5, 9, 2, 90);

DROP TABLE IF EXISTS Career;

CREATE TABLE Career (
    ID INT IDENTITY(1,1) PRIMARY KEY,
    Skill VARCHAR(50),
    Skills INT,
    Experience INT,
    Projects INT,
    Projects_Completed INT,
    Job_Applications INT,
    Performance_Score FLOAT
);

INSERT INTO Career VALUES
('Data Science', 8, 2, 5, 4, 3, 85),
('Web Dev', 7, 1, 4, 3, 5, 78),
('AI Engineer', 9, 3, 6, 5, 2, 90);


DROP TABLE IF EXISTS Behavior;

CREATE TABLE Behavior (
    ID INT IDENTITY(1,1) PRIMARY KEY,
    Productivity_Score FLOAT,
    Social_Interactions INT,
    Habits INT,
    Focus INT,
    Consistency INT,
    Motivation INT,
    Emotional_Score FLOAT
);

INSERT INTO Behavior VALUES
(85, 10, 7, 8, 9, 8, 88),
(70, 8, 5, 6, 6, 7, 72),
(90, 12, 8, 9, 9, 9, 95);
