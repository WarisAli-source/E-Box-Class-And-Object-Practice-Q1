# E-Box-Class-And-Object-Practice-Q1
Solution for E-Box Python Internship Practice Problem Q1
OOPS-EQUALS()
OOPs-equals() method
 
 Praveen works as a Reservation manager, he keeps the record of all the booking details and reservations of the convention halls. But he wants to automate it since manually maintaining all the files consume a lot of time. So, he asks help from the Development team to automate the process which takes the details of 'n' number of entries of the halls along with the hall details which includes the name of Hall, Contact, and Address of the user, Booking Date, Cost, and owner of the Hall. Now it needs to find whether the hall is available for registration or not by comparing the name, Phone number, and the booking date of the booking details with available Hall details. Print the details. 
 
Create Hall class with the following attributes.

DataType	Variable
String	Name
Integer	Phone number
String	Address
Date	 bookingDate
Float	Cost
String	Owner
Initialize the attributes using "__init__()" method. 
Use the following methods in Hall class. 

 

Method	Description
equals(self , obj)	
To check whether all the details of the hall match or not.

'obj' is an object of newly entered hall details.

display(self)	Display all the details of the hall
 

 
Input Format:
Input consists of an integer 'n' indicating the number of entries followed by the details of 'n' number of halls. Next, the user needs to enter the hall details to be booked.

Output format:
The output should display "Already registered" if the halls are booked followed by the booked hall details. 
The output should display "Registration Available" if the hall to be booked is available followed by the booked hall details.

Refer sample input and output for formatting specifications.

All text in bold corresponds to the input and the rest corresponds to output.
 
Input-Output Sample:
Enter the number of Entries
1
Enter details of Hall 1
Enter Hall name
chandan palace
Enter Phone
9876540321
Enter Address
Chandan Palce,RamakrishnaNagar,Mysore
Enter Date of booking
Dec 12 2017
Enter cost
1243
Enter owner name
Chandan

Enter the Hall details for booking
Enter Hall name
chandan palace
Enter Phone
9876540321
Enter Address
Chandan Palce,RamakrishnaNagar,Mysore
Enter Date of booking
Dec 12 2017
Enter cost
1243
Enter owner name
Chandan

Already Registered

Display the Booked Hall details
Hall name :chandan palace
Phone No : 9876540321
Address :Chandan Palce,RamakrishnaNagar,Mysore
Cost :1243.00
Owner name :Chandan
 
