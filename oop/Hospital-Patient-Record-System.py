# Hospital Patient Record System.

class Patient:
    def __init__(self, patient_id, name, disease):
        self.patient_id = patient_id
        self.name = name
        self.disease = disease
    def display_info(self):
        print(f"Patient ID: {self.patient_id}, Name: {self.name}, Disease: {self.disease}")
        
patient1 = Patient("P001", "John Doe", "Flu")
patient1.display_info()
