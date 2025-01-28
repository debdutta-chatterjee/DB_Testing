import sqlite3

## connect to sqllite
connection=sqlite3.connect("patients.db")

##create a cursor object to insert record,create table
cursor=connection.cursor()

## create the table
patients_table_info="""
CREATE TABLE Patients (
    patient_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender VARCHAR(10),
    birth_date DATE,
    weight DECIMAL(5,2),
    height DECIMAL(5,2),
    allergies TEXT,
    city VARCHAR(50),
    province_id INT,
    last_update TIMESTAMP
);"""

#### Admissions Table
admissions_table_info="""
CREATE TABLE Admissions (
    admission_id INT PRIMARY KEY,
    patient_id INT,
    diagnosis TEXT,
    admission_date DATE,
    discharge_date DATE,
    attending_doctor_id INT,
    last_update TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
); """

#### Doctors Table
doctors_table_info="""
CREATE TABLE Doctors (
    doctor_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    specialty VARCHAR(50),
    last_update TIMESTAMP
);"""

#### ProvinceNames Table
province_names_table_info="""
CREATE TABLE ProvinceNames (
    province_id INT PRIMARY KEY,
    province_name VARCHAR(50),
    last_update TIMESTAMP
);"""

#Create tables
cursor.execute(patients_table_info)
cursor.execute(admissions_table_info)
cursor.execute(doctors_table_info)
cursor.execute(province_names_table_info)


### Populate Tables with Records

#### Insert Records into Patients Table
cursor.execute('''
INSERT INTO Patients (patient_id, first_name, last_name, gender, birth_date, weight, height, allergies, city, province_id, last_update)
VALUES
    (1, 'John', 'Doe', 'M', '1980-01-01', 75.5, 180.4, NULL, 'Toronto', 1, '2025-01-28 10:00:00'),
    (2, 'Jane', 'Smith', 'F', '1992-05-14', 68.2, 170.1, 'Hay fever', 'Hamilton', 2, '2025-01-28 10:00:00');
''')
#### Insert Records into Admissions Table
cursor.execute('''
INSERT INTO Admissions (admission_id, patient_id, diagnosis, admission_date, discharge_date, attending_doctor_id, last_update)
VALUES
    (1, 1, 'Flu', '2025-01-01', '2025-01-03', 101, '2025-01-28 10:00:00'),
    (2, 2, 'Asthma', '2025-01-10', '2025-01-12', 102, '2025-01-28 10:00:00');
''')
#### Insert Records into Doctors Table
cursor.execute('''
INSERT INTO Doctors (doctor_id, first_name, last_name, specialty, last_update)
VALUES
    (101, 'Lisa', 'Chang', 'Pediatrician', '2025-01-28 10:00:00'),
    (102, 'Mike', 'Johnson', 'Dermatologist', '2025-01-28 10:00:00');
''')
#### Insert Records into ProvinceNames Table
cursor.execute('''
INSERT INTO ProvinceNames (province_id, province_name, last_update)
VALUES
    (1, 'Ontario', '2025-01-28 10:00:00'),
               (2, 'Quebec', '2025-01-28 10:00:00');
''')

## Display all the records
print("The inserted records are")
data=cursor.execute('''Select * from Admissions''')
for row in data:
    print(row)

## Commit your changes in the database
connection.commit()
connection.close()
