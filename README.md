# My_Family
#### Video Demo: <https://youtu.be/64IvG_ZyB_s>
#### Description:

The My Family Information Manager is a simple Python program that allows users to manage information about their family members. It provides a user-friendly interface to enter and save family information in text and CSV formats. Additionally, it can generate a PDF document with the entered information.

The program first creates the user interface. The user interface consists of a label for each piece of information that is to be entered, and an entry box for each label. The labels are: Name, Family, Birthday, National code, Father Name, Mother Name, Postal code, Cell phone Number, Home telephone, Home Address, and Note.

When the user clicks the "Save informations" button, the program saves the information entered by the user in a text file. The text file is called "My_Family.txt". The information is saved in the following format:

Name,Family,Birthday,National code,Father Name,Mother Name,Postal code,Cell phone Number,Home telephone,Home Address,Note

The program then converts the information in the text file to a DataFrame using the pandas library. The DataFrame is saved in a CSV file called "My_Family.csv".

The program then creates a thread to generate the PDF file. The PDF file is created using the fpdf library. The PDF file contains the information from the CSV file.

The program displays a message box indicating that the information has been saved successfully. The PDF file will be created shortly.

# Installation

To use the My Family Information Manager, you need to have Python installed on your system. If you don't have Python installed, you can download it from the official website: Python Official Website

The program uses the following libraries:

* tkinter: This library is used to create the user interface.
* filedialog: This library is used to select a file to upload.
* os: This library is used to create and manage directories.
* shutil: This library is used to copy files.
* pandas: This library is used to create and save CSV files.
* fpdf: This library is used to create PDF files.
* threading: This library is used to create a thread to generate the PDF file.

Next, follow these steps:

Clone or download this repository.

Open a terminal or command prompt and navigate to the project directory : https://github.com/RezaAbbaszadeh80/CS50_final_project

Install the required dependencies using the following command:

     pip install fpdf
     pip install pandas
     

# How to Use

1.  Open the My_Family.py file in a text editor or Python IDE.
2. Run the program to launch the My Family Information Manager application.
3. The application will open a window with labeled fields for entering family information.
4. Enter the required details for each family member, such as name, family, birthday, etc.
5. Click on the "Upload Picture" button to upload an image of your family.
6. After entering the information for all family members, click on the "Save Informations" button to save the data.
7. The information will be saved in two files:
    My_Family.txt: Contains the information in text format.
    My_Family.csv: Contains the information in CSV format.

# Example

Let's say we want to enter the following information for a family member:

     Name: John Doe 
     Family: Doe
     Birthday: 1985-07-10
     National Code: 1234567890
     Father Name: Michael Doe
     Mother Name: Mary Doe
     Postal Code: 12345
     Cell Phone Number: 123-456-7890
     Home Telephone: 987-654-3210
     Home Address: 123 Main Street, City
     Note: This is a test entry.

We will enter this information into the My Family Information Manager application and save it. The program will save the data in My_Family.txt and My_Family.csv files and generate a PDF document with the entered information.

Note: The program uses threading to generate the PDF document, so it will not interfere with the user interface.

Enjoy managing your family information with ease using the My Family Information Manager! 🏡👨‍👩‍👧‍👦
