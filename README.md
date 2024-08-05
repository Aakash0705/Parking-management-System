Parking Management System
Overview
This Parking Management System is designed to streamline the process of managing vehicle parking in a facility. The system collects vehicle details, notes the time of entry, calculates parking charges, displays the record of parked vehicles, and generates a bill at the time of exit. The frontend is developed in Python, and the backend uses MySQL, interfaced through the MySQL Connector.

Features
Vehicle Details Collection: Captures essential details such as vehicle number, type (car, bike, etc.), and owner information.
Timestamp Logging: Records the exact time of entry for each vehicle.
Database Storage: Stores all vehicle details and timestamps in a MySQL database for easy retrieval and management.
Parking Charges Calculation: Automatically calculates parking charges based on the duration of the stay.
Display Records: Provides a user-friendly interface to display the record of all currently parked vehicles.
Bill Generation: Generates an itemized bill at the time of vehicle exit, detailing the parking charges.
Technologies Used
Frontend: Python with a graphical user interface (GUI) library (such as Tkinter or PyQt).
Backend: MySQL database for storing and managing vehicle information.
Interface: MySQL Connector for Python to interact with the MySQL database.
Installation
Clone the repository:


Install dependencies:

sh
Copy code
pip install mysql-connector-python
Set up the MySQL database:

Create a MySQL database named parking_system.
Run the provided SQL script to create the necessary tables:
sql
Copy code
CREATE DATABASE parking_system;
USE parking_system;

CREATE TABLE vehicles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_number VARCHAR(50) NOT NULL,
    vehicle_type VARCHAR(20) NOT NULL,
    owner_name VARCHAR(100),
    entry_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    exit_time TIMESTAMP NULL,
);
Configure database connection:

Update the database connection settings in the config.py file:
python
Copy code
db_config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'database': 'parking_system',
}
Usage
Run the application:

sh
Copy code
python main.py
Enter vehicle details:

Input the vehicle number, type, and owner information upon entry.
The system will automatically record the entry time and store the information in the database.
View parked vehicles:

The interface provides an option to view the list of all currently parked vehicles along with their entry times.
Generate bill at exit:

When a vehicle exits, select the vehicle from the list and confirm exit.
The system calculates the parking charges based on the duration of the stay and generates a bill.
Contributing
We welcome contributions to enhance this Parking Management System. If you have any ideas or find any issues, please feel free to open an issue or submit a pull request.
