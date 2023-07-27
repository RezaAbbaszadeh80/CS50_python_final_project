import pandas as pd
import os
import threading
from project import upload, save_informations, create_csv_file, create_pdf_from_csv
from tkinter import filedialog

# Test upload function
def test_upload_picture(monkeypatch):
    # Mock the filedialog.askopenfilename function to return a test file path
    def mock_askopenfilename(*args, **kwargs):
        return "test_image.jpg"

    # Apply the mock function to the filedialog.askopenfilename during the test
    monkeypatch.setattr(filedialog, "askopenfilename", mock_askopenfilename)

    # Call the upload function
    upload()

    # Check if the "pictures" folder is created and the test file is copied to it
    assert os.path.exists("pictures")
    assert os.path.exists(os.path.join("pictures", "test_image.jpg"))


def test_save_informations(monkeypatch, capsys):
    # Define a dummy success message to check against the captured output
    success_message = "Information saved successfully. The PDF file will be created shortly."

    # Mock the pd.DataFrame.to_csv function to do nothing during the test
    def mock_to_csv(*args, **kwargs):
        pass

    # Mock the threading.Thread.start function to do nothing during the test
    def mock_thread_start(*args, **kwargs):
        pass

    # Apply the mock functions to pd.DataFrame.to_csv and threading.Thread.start during the test
    monkeypatch.setattr(pd.DataFrame, "to_csv", mock_to_csv)
    monkeypatch.setattr(threading.Thread, "start", mock_thread_start)

    # Use monkeypatch to override the messagebox.showinfo function and set the captured output to the success_message
    def mock_showinfo(*args):
        print(success_message)
    monkeypatch.setattr("tkinter.messagebox.showinfo", mock_showinfo)

    # Call the save_informations function
    save_informations()

    # Capture the output from the print statement in the mock_showinfo function
    captured = capsys.readouterr()

    # Check if the success message is present in the captured output
    assert success_message in captured.out

def test_create_csv():
    csv_filename = "test_data.csv"  # Create a test CSV file
    with open(csv_filename, "w") as file:
        file.write("Name,Family\nJohn,Doe\n")
    data = create_csv_file(csv_filename)
    assert data.equals(pd.DataFrame({"Name": ["John"], "Family": ["Doe"]}))

def test_create_pdf():
    csv_filename = "test_data.csv"  # Create a test CSV file
    pdf_filename = "test_data.pdf"  # PDF filename
    with open(csv_filename, "w") as file:
        file.write("Name,Family\nJohn,Doe\n")
    create_pdf_from_csv(csv_filename, pdf_filename)
    assert os.path.exists(pdf_filename)

    # Clean up after the test
    os.remove(csv_filename)
    os.remove(pdf_filename)
