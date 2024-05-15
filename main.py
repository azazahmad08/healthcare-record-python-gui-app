import csv
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox 
import os

class HealthRecord:
    def __init__(self, date, symptom, diagnosis, prescription):
        self.date = date
        self.symptom = symptom
        self.diagnosis = diagnosis
        self.prescription = prescription

class MedicalHistory:
    def __init__(self, name):
        self.name = name
        self.records = []

    def add_health_record(self, health_record):
        self.records.append(health_record)

class Appointment:
    def __init__(self, date, time, doctor):
        self.date = date
        self.time = time
        self.doctor = doctor

class CSVHandler:
    @staticmethod
    def write_health_record(filename, health_record):
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([health_record.date, health_record.symptom, health_record.diagnosis, health_record.prescription])

    @staticmethod
    def read_health_records(filename):
        records = []
        with open(filename, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                records.append(HealthRecord(*row))
        return records

    @staticmethod
    def write_appointment(filename, appointment):
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([appointment.date, appointment.time, appointment.doctor])

    @staticmethod
    def read_appointments(filename):
        appointments = []
        with open(filename, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                appointments.append(Appointment(*row))
        return appointments

class HealthRecordSystem:
    def __init__(self, health_record_file, appointment_file):
        self.health_record_file = health_record_file
        self.appointment_file = appointment_file

        # Check if files exist, if not, create them
        self.create_csv_files()

    def create_csv_files(self):
        if not os.path.exists(self.health_record_file):
            with open(self.health_record_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Date', 'Symptom', 'Diagnosis', 'Prescription'])

        if not os.path.exists(self.appointment_file):
            with open(self.appointment_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Date', 'Time', 'Doctor'])

    def add_health_record(self, health_record):
        CSVHandler.write_health_record(self.health_record_file, health_record)

    def get_medical_history(self):
        return CSVHandler.read_health_records(self.health_record_file)

    def schedule_appointment(self, appointment):
        CSVHandler.write_appointment(self.appointment_file, appointment)

    def get_appointments(self):
        return CSVHandler.read_appointments(self.appointment_file)

class HealthRecordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Health Record Management System")
        self.root.geometry("600x400")

        self.health_record_system = HealthRecordSystem('health_records.csv', 'appointments.csv')

        self.tab_control = ttk.Notebook(self.root)
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab3 = ttk.Frame(self.tab_control)
        self.tab4 = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab1, text='Add Health Record')
        self.tab_control.add(self.tab2, text='Schedule Appointment')
        self.tab_control.add(self.tab3, text='View Medical History')
        self.tab_control.add(self.tab4, text='View Appointments')

        self.tab_control.pack(expand=1, fill='both')

        self.create_add_health_record_tab()
        self.create_schedule_appointment_tab()
        self.create_view_medical_history_tab()
        self.create_view_appointments_tab()

    def create_add_health_record_tab(self):
        lbl_date = tk.Label(self.tab1, text="Date (YYYY-MM-DD):")
        lbl_date.grid(column=0, row=0, padx=10, pady=10)
        self.entry_date = tk.Entry(self.tab1, width=20)
        self.entry_date.grid(column=1, row=0, padx=10, pady=10)

        lbl_symptom = tk.Label(self.tab1, text="Symptom:")
        lbl_symptom.grid(column=0, row=1, padx=10, pady=10)
        self.entry_symptom = tk.Entry(self.tab1, width=20)
        self.entry_symptom.grid(column=1, row=1, padx=10, pady=10)

        lbl_diagnosis = tk.Label(self.tab1, text="Diagnosis:")
        lbl_diagnosis.grid(column=0, row=2, padx=10, pady=10)
        self.entry_diagnosis = tk.Entry(self.tab1, width=20)
        self.entry_diagnosis.grid(column=1, row=2, padx=10, pady=10)

        lbl_prescription = tk.Label(self.tab1, text="Prescription:")
        lbl_prescription.grid(column=0, row=3, padx=10, pady=10)
        self.entry_prescription = tk.Entry(self.tab1, width=20)
        self.entry_prescription.grid(column=1, row=3, padx=10, pady=10)

        btn_add_record = tk.Button(self.tab1, text="Add Health Record", command=self.add_health_record)
        btn_add_record.grid(column=1, row=4, padx=10, pady=10)

    def add_health_record(self):
        date = self.entry_date.get()
        symptom = self.entry_symptom.get()
        diagnosis = self.entry_diagnosis.get()
        prescription = self.entry_prescription.get()
        health_record = HealthRecord(date, symptom, diagnosis, prescription)
        self.health_record_system.add_health_record(health_record)
        messagebox.showinfo(title="Success", message="Health record added successfully!")


    def create_schedule_appointment_tab(self):
        lbl_date = tk.Label(self.tab2, text="Date (YYYY-MM-DD):")
        lbl_date.grid(column=0, row=0, padx=10, pady=10)
        self.entry_app_date = tk.Entry(self.tab2, width=20)
        self.entry_app_date.grid(column=1, row=0, padx=10, pady=10)

        lbl_time = tk.Label(self.tab2, text="Time:")
        lbl_time.grid(column=0, row=1, padx=10, pady=10)
        self.entry_time = tk.Entry(self.tab2, width=20)
        self.entry_time.grid(column=1, row=1, padx=10, pady=10)

        lbl_doctor = tk.Label(self.tab2, text="Doctor:")
        lbl_doctor.grid(column=0, row=2, padx=10, pady=10)
        self.entry_doctor = tk.Entry(self.tab2, width=20)
        self.entry_doctor.grid(column=1, row=2, padx=10, pady=10)

        btn_schedule_appointment = tk.Button(self.tab2, text="Schedule Appointment", command=self.schedule_appointment)
        btn_schedule_appointment.grid(column=1, row=3, padx=10, pady=10)

    def schedule_appointment(self):
        date = self.entry_app_date.get()
        time = self.entry_time.get()
        doctor = self.entry_doctor.get()
        appointment = Appointment(date, time, doctor)
        self.health_record_system.schedule_appointment(appointment)
        tk.messagebox.showinfo("Success", "Appointment scheduled successfully!")

    def create_view_medical_history_tab(self):
        tree = ttk.Treeview(self.tab3, columns=('Date', 'Symptom', 'Diagnosis', 'Prescription'), show='headings')
        tree.heading('Date', text='Date')
        tree.heading('Symptom', text='Symptom')
        tree.heading('Diagnosis', text='Diagnosis')
        tree.heading('Prescription', text='Prescription')
        tree.grid(row=0, column=0, padx=10, pady=10)

        for record in self.health_record_system.get_medical_history():
            tree.insert('', 'end', values=(record.date, record.symptom, record.diagnosis, record.prescription))

    def create_view_appointments_tab(self):
        tree = ttk.Treeview(self.tab4, columns=('Date', 'Time', 'Doctor'), show='headings')
        tree.heading('Date', text='Date')
        tree.heading('Time', text='Time')
        tree.heading('Doctor', text='Doctor')
        tree.grid(row=0, column=0, padx=10, pady=10)

        for appointment in self.health_record_system.get_appointments():
            tree.insert('', 'end', values=(appointment.date, appointment.time, appointment.doctor))

if __name__ == "__main__":
    root = tk.Tk()
    app = HealthRecordApp(root)
    root.mainloop()
