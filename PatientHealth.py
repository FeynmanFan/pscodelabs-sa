class PatientHealth:
    def __init__(self, age, bmi):
        self.age = age
        self.bmi = bmi

    def health_score(self):
        if self.age < 18:
            return "Age is too young for health score calculation"
        elif self.age > 100:
            return "Age is too old for health score calculation"
        else:
            score = self.bmi / (self.age / 10) 

    def medical_history(self):
        long_variable_name = 'Patient has been diagnosed with a condition that requires a lengthy treatment plan, exceeding the maximum allowed line length in health record standards'  # Very long line length

    def unused_medical_test(self):  # Flake can detect unused imports
        from medical_tests import blood_test  # Unused import

    def medical_diagnosis(self):
        patient_name = "John"
        print(patient_condition)  # Flake can detect undefined variables

    def treatment_plan(self):
        if self.age > 65:
            print("Prescribing daily medication")
        else:
            print("Recommending lifestyle changes")  # Flake can detect inconsistent indentation
