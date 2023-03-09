import pydicom
import os
import csv
import pandas as pd
data= pd.read_csv("DETAILS.csv")
PatientID = data.MRNo
Age = data.Age
path = os.listdir(r"D:\Slosh AI\SLOSH XRAYS\Ali Medical Data\2000 X-RAY\Data")
for dicoms in path:
    counter = 0
    Dicom_Image = pydicom.read_file(r"D:\Slosh AI\SLOSH XRAYS\Ali Medical Data\2000 X-RAY\Data/"+dicoms)
    ID =Dicom_Image.get(0x00100020).value
    for id in PatientID:
        counter+=1
        if ID == id:
            print("Counter",counter)
            print(Age[counter])
            data = [dicoms,Age[counter]]
            with open('Ali Medical Images.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow(data)
            file.close()


    



