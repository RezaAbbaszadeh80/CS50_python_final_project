from tkinter import *
from tkinter import filedialog 
import os
import shutil
import pandas as pd 
from fpdf import FPDF
import threading
from tkinter import messagebox

entries = {}

def main():
    # Create the root(window)
    root = Tk()
    color = 'gold'
    root.title('My_family')
    root.geometry('800x600')
    root.config(background=color)

    # Writing labels and placing entries
    label_names = ['Name', 'Family', 'Birthday', 'National code', 'Father Name',
                   'Mother Name', 'Postal code', 'Cell phone Number', 'Home telephone', 'Home Address', 'Note']

    global entries
    

    lbl_1 = Label(root, text='<< In the name of God >>', font=('Arial', 20), bg=color)
    lbl_1.grid(row=0, columnspan=2, padx=5, pady=5)

    for idx, label_name in enumerate(label_names):
        label = Label(root, text=f"{label_name} :", font=("None", 15))
        label.grid(row=idx + 2, column=0, sticky='e', padx=5, pady=5)

        entry = Entry(root, width=50, font=("None", 15))
        entry.grid(row=idx + 2, column=1, sticky='w', padx=5, pady=5)
        entries[label_name] = entry

    if not os.path.exists("My_Family.txt"):
        with open("My_Family.txt", "a") as file:
            header = ",".join(str(x) for x in label_names) + "\n"  # Adding label names as the first row of the file
            file.write(header)

    btn_13 = Button(root, text='upload picture', command=upload)
    btn_13.grid(row=len(label_names) + 3, column=1, sticky='w', padx=5, pady=5)

    btn_Save_informations = Button(root, text='Save informations', command=save_informations)
    btn_Save_informations.grid(row=len(label_names) + 4, column=1, sticky='w', padx=5, pady=5)

    root.mainloop()


def upload():
    """
    This function performs the image upload by the user.
    Using filedialog.askopenfilename, the user can select an image, and after selection, the chosen image will be copied to the "pictures" folder.
    """
    try:
        global my_dict
        path = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png"), ("all files", "*.*")))

        if not os.path.exists("pictures"):
            os.makedirs("pictures")

        shutil.copy(path, "pictures")

    except:
        pass


def create_csv_file(csv_filename):
    """
    This function reads data from a CSV file and returns a DataFrame.

    Parameters:
        csv_filename (str): The filename of the CSV file containing the data.

    Returns:
        pandas.DataFrame: The DataFrame containing the data from the CSV file.
    """
    # Read the CSV file using pandas
    data = pd.read_csv(csv_filename)

    # Replace NaN values with a space
    data.fillna(" ", inplace=True)

    return data


def create_pdf_from_csv(csv_filename, pdf_filename):
    """
    This function reads data from a CSV file and creates a PDF file with the information.

    Parameters:
        csv_filename (str): The filename of the CSV file containing the data.
        pdf_filename (str): The filename of the PDF file to be created.
    """
    # Get data from CSV file
    data = create_csv_file(csv_filename)

    # Create a PDF object
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Set font
    pdf.set_font("Arial", size=12)

    # Write data to the PDF
    for _, row in data.iterrows():
        pdf.add_page()  # Add a new page for each row

        for column in data.columns:
            pdf.cell(40, 10, str(column), border=1)
            pdf.cell(0, 10, str(row[column]), ln=True, align="L")

    # Save the PDF file
    pdf.output(pdf_filename)


def save_informations():
    """
    This function saves the information entered by the user.
    The entered information from various inputs (Entry) is collected and saved in the My_Family.txt file in text format.
    Additionally, using the pandas library, the information is also saved in CSV format.
    """
    global entries

    my_dict = {}
    for label_name, entry in entries.items():
        my_dict[label_name] = entry.get()

    with open("My_Family.txt", "a") as file:
        for item in my_dict.values():
            file.write(f'{item},')
        file.write('\n')

    # Convert the dictionary to a DataFrame
    data = pd.DataFrame([my_dict])

    # Check if the CSV file exists, if not, write the header row
    if not os.path.exists("My_Family.csv"):
        data.to_csv("My_Family.csv", index=False, mode='a', header=True)
    else:
        data.to_csv("My_Family.csv", index=False, mode='a', header=False)

    # Create a thread to generate the PDF
    csv_file = "My_Family.csv"
    pdf_file = "My_Family_Info.pdf"
    pdf_thread = threading.Thread(target=create_pdf_from_csv, args=(csv_file, pdf_file))
    pdf_thread.start()

    # Display a message box indicating successful saving
    messagebox.showinfo("Success", "Information saved successfully. The PDF file will be created shortly.")

if __name__ == "__main__":
    main()
