import sys
import os
import ezdxf
import shutil
import tkinter as tk
from tkinter import messagebox
MainPath = "W:\Customer Master Folders"
DefaultsPath = "C:\M\FileGenerator\Defaults"

def main():
    initGUI()

#Console input verification
# def verifyInputs():
#     customerName = sys.argv[1]  
#     jobName = sys.argv[2]
    
#     print(f"You entered \nCustomer Name:{customerName}\nJob Name:{jobName}")
#     response = input("Is this correct? (y,n)")
#     if (response == "y"):
#         print("Inputs verified")
#     elif (response == "n"):
#         print("Correct your responses\n If current input is valid leave blank")

#         customerNameInput  = input(f"Current Customer Name: {customerName} \n->")
#         if (customerNameInput == ""):
#             print("Customer Name Correct")
#         else:
#             print(f"Customer Name corrected to: {customerNameInput}")
#             customerName = customerNameInput

#         jobNameInput = input(f"Current Job Name: {jobName} \n->")
#         if (jobNameInput == ""):
#             print("Job Name Correct")
#         else:
#             print(f"Job Name corrected to: {jobNameInput}")
#             jobName = jobNameInput
        
#     elif (response != "y" & response != "n"):
#         print("Invalid response (y for yes, n for no)")
#     return [customerName, jobName]

def generateJob(userInputs):
    print(userInputs)
    for input in userInputs:

        if input == "":
            messagebox.showerror(title="Empty Input", message="Please fill out both a Customer and Job Name")
            return 
        else:
            continue 
    createFolders(userInputs)
    generateDXFFile(userInputs)
    generateDIGfile(userInputs)
    return 1

def createFolders(userInputs):
    doesCustomerFolderExist = os.path.exists(f"{MainPath}\{userInputs[0]}")
    if (doesCustomerFolderExist):
        print("Customer folder found")
        pass
    else:
        print(f'Customer folder not found creating customer folder: {userInputs[0]}')
        os.mkdir(f"{MainPath}\{userInputs[0]}")
        print("Folder created")
    
    doesJobFolderExist = os.path.exists(f"{MainPath}\{userInputs[0]}\{userInputs[1]}")
    if (doesJobFolderExist):
        print("Job folder found")
        pass
    else:
        print(f"Job folder not found creating job folder: {userInputs[1]}")
        os.mkdir(f"{MainPath}\{userInputs[0]}\{userInputs[1]}")
        print("Folder created")

def generateDXFFile(userInputs):
    doesJobDXFFileExist = os.path.exists(f"{MainPath}\{userInputs[0]}\{userInputs[1]}\{userInputs[1]}.dxf")
    print(f"{MainPath}\{userInputs[0]}\{userInputs[1]}.dxf")

    if(doesJobDXFFileExist == False):
        print('DXF file not found')
        print("Generating DXF File")
        DXFFile = ezdxf.new(dxfversion="R2010")
        print("Saving DXF file")
        DXFFile.saveas(f"{MainPath}\{userInputs[0]}\{userInputs[1]}\{userInputs[1]}.dxf")

    else:
        print("DXF file found.")
    

    print("Opening DXF...")
    os.startfile(f"{MainPath}\{userInputs[0]}\{userInputs[1]}\{userInputs[1]}.dxf")

    
def generateDIGfile(userInputs):
    doesJobDIGFileExist = os.path.exists(f"{MainPath}\{userInputs[0]}\{userInputs[1]}\{userInputs[1]}.dig")
    if(doesJobDIGFileExist == False):
        print("DIG File Not Found")
        print("Generating DIG file")
        shutil.copy(f"{DefaultsPath}\\blank.dig", f"{MainPath}\{userInputs[0]}\{userInputs[1]}\{userInputs[1]}.dig")
        print("DIG file generated")
    else:
        print("Dig File Found")
    print('Opening IGEMS')
    os.startfile(f"{MainPath}\{userInputs[0]}\{userInputs[1]}\{userInputs[1]}.dig")

    
#---- TKinter setup

def initGUI():
    window = tk.Tk()
    window.title("Job File Generator")

    customerLabel = tk.Label(text="Enter Customer Name")
    jobNameLabel = tk.Label(text="Enter Job Name")
    jobNameFormat = tk.Label(text="Job Name format: CustomerName_JobNumber_PartNumber")
    
    customerNameInputEntry = tk.Entry()
    jobNameInputEntry = tk.Entry()
    submitButton = tk.Button(window, text="Submit", command=lambda: handleSubmit(customerNameInputEntry, jobNameInputEntry))
    packTK([customerLabel, customerNameInputEntry, jobNameLabel, jobNameFormat, jobNameInputEntry, submitButton])

    window.mainloop()
    #Send Widgets in order to be packed (top to bottom) saves lines of code.

    
def clearEntry(widgetArr):
    for widget in widgetArr:
        widget.delete(0, "end")

def packTK(widgetArr):
    for widget in widgetArr:
        widget.pack()
    return

def handleSubmit(customerNameInputEntry, jobNameInputEntry):

    response = generateJob([customerNameInputEntry.get(), jobNameInputEntry.get()])
    if response == 1:
        messagebox.showinfo(title="Files created", message=f"Job: {jobNameInputEntry.get()}\n created in {MainPath}\{customerNameInputEntry.get()}\{jobNameInputEntry.get()}\{jobNameInputEntry.get()}")
    
    clearEntry([customerNameInputEntry, jobNameInputEntry])

main()