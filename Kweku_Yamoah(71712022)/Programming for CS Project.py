# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 13:24:18 2019

@author: Kweku Andoh Yamoah(71712022)
"""
import random 

class Patient:
    def __init__(self,f_name,l_name):
        self.Fname= f_name
        self.Lname= l_name
        
        
    def getFName(self):
        return self.Fname
    def getLName(self):
        return self.Lname
    #A method of the patient class that saves a patient name for future appointment booking   
    def patient_file(self):
        infile = open("patientApiontment.txt", "r")
        lines = infile.readlines()
        ist =[self.getFName,self.getLName]
        found = False
        new = open("patientApiontment.txt", "a")
        for line in lines:
            f_name,l_name =line.split(",")
            l_name = l_name.rstrip("\n")
            if ist[0] == f_name and ist[1] == l_name:
                print("This nigger has an appointment booked")
                found = True
                break
            
        if found == False:
             print("\n" + self.getFName() + " " + self.getLName() , file = new)
        
        infile.close()
        
      
class Doctor:
    def __init__(self,d_name,Patient,ava_times,ava_days):
        self.doc= d_name
        self.appPatient= Patient.patient_file
        self.schedule= ava_times
        self.appDays= ava_days
        
    def getDoc_name(self):
        return self.doc
    
    def getPatient(self):
        return self.appPatient
    
    def getSched(self):
        return self.schedule
    
    def getDoc_days(self):
        return self.appDays
    
    
class Interface:
    def __init__(self,Patient):
        self.patient= Patient
        self.file= self.patient.patient_file
        
    #A function that takes a random patient from the patient file and books an appointment for the person  
    def appointment(self):
        infile= open("patientApiontment.txt", "r")
        lines = infile.read().split()
        mypatient= random.choice(lines)
        
        newfile = open("Appointment.txt","a")
        
        f_name, l_name= mypatient.split(",")
        l_name = l_name.rstrip("\n")
        doc, day, time = self.doc_chosen()
        print(f_name + "," + l_name + "," + doc + "," + day + "," + time, file = newfile)
        
        return f_name,l_name,doc,day,time
        
    
    #A function that assigns a doctor to a day, reada from a file with doctor and days available   
    def doc_day(self):
        doctors = """ Mr. John Alhassan
            Mr. Kweku Yamoah
            Miss. Chinwe Igbebu
            Miss. Faith Akos
            Mrs. Leonette Dapaah
            Mr. Elvis Okoh"""
            
        print("Doctors available are:" + " " + 
              doctors)

        p_doc= input("Enter name of doctor:\n")
        p_day = input("Enter day:\n")
        infile = open("Doctor file.txt", "r")
        for line in infile:
            line = line.rstrip("\n")
            doc, l_days = line.split(",[")
            
            days = eval(l_days)
            if p_doc == doc:
                for check_day in days:
                    if check_day == p_day:
                        return doc, check_day
    #A simple function to display static time slots patients can choose                
    def display_slots(self):
        option = """ 1. 13:00  2. 13:30  3. 14:00  4. 14:30  5. 15:00  6. 15:30
                 7.  16:00  8. 16:30"""
        print(option)
    #A function that saves the doctor booked, the day and the time    
    def doc_chosen(self):
        doc, day = self.doc_day()
        self.display_slots()
        infile = open("Doc_chosen.txt","r")
        slot = ['13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30']
        option = int(input("Choose a slot:\n"))
        temp = infile.readlines()
        infile.close()
        newfile = open('Doc_chosen.txt', 'a')
        found = False
        for i in temp:
            i = i.rstrip()
            k = i.split(",")
            if k[0] == doc and k[1] == day and k[2] == slot[option - 1 ]:
                print("This nigger is already booked")
                found = True
                break
        if found == False:
            print(doc + "," + day + "," + slot[option - 1], file = newfile)
            return doc,day,slot[option -1]
            
        infile.close()
    #A function to dispaly doctors booked   
    def dis_docbookings(self):
        infile = open("Doc_chosen.txt","r")
        for line in infile:
            doc,day,time = line.split(",")
            time = time.rstrip("\n")
            print("{0:<25} {1:<15} {2:<10}".format(doc,day,time))
        infile.close()
        
    #A helper function that reads from a file and checks input to cancel an appointment
    def del_appointment(self):
        print("Time slots available to delete are....")
        self.display_slots()
        f_name = input("Enter first name:\n")
        l_name = input("Enter last name:\n")
        doc = input("Enter doctor booked:\n")
        day = input("Enter the appointment day:\n")
        time = input("Enter the time:\n")
        
        infile = open("Appointment.txt","r")
        lines = infile.readlines()
        outfile = open("Appointment","w")
        found = False
        for line in lines:
            file_fname,file_lname,f_doc,f_day,f_time= line.split(",")
            f_time = f_time.rstrip("\n")

            if not(f_name == file_fname and l_name== file_lname and doc == f_doc and day == f_day and time == f_time):
                #print(f_name,l_name,doc, day, time)
                outfile.write(line)
            
            else:
                found = True
                
                
      
        if found == False:
            print("Yo!, gee nor come book for here")
        infile.close()
        outfile.close()
        
class App:
    def __init__(self,interface):
        self.inter = interface
    intro= """======= Welcome to the patient/doctor appointment system =====
    Things you can do are:
        (1). Save the name of a patient for future appointment booking
        (2). Create an appointment for a patient
        (3). Delete a patient appointment
        (4). View doctors booked and the times"""
        
    print(intro)
    
    def activity(self):
        action = int(input("Enter what you want to do:\n"))
        if action == 1:
            print("Saving patient name for appointment booking")
            first = input("Enter first name:\n")
            last = input("Enter last name:\n")
            patient = Patient(first,last)
            patient.patient_file()
            print(first + " " + last + " " + "saved succesfully")
        
        if action == 2:
            print("Creating an appointment for a random patient in patient file")
            print(self.inter.appointment())
            print("Booked successfully")
        if action == 3:
            print("Deleting appointment of patient...")
            self.inter.del_appointment()
            print("Appointment deleted successfully")
        
        if action == 4:
            print("Viewing doctors booked")
            print(self.inter.dis_docbookings())
        
def main():
    program =Interface(Patient("Percy","Brown"))
    app = App(program)
    app.activity()
#main
program =Interface(Patient("Percy","Brown"))
program.del_appointment()
        