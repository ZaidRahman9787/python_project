import uuid
import json
from datetime import datetime

def get_numeric_input(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        return None

def generate_audit_id():
    return str(uuid.uuid4())

def run_audit():
    print("\nClinical Data Audit System")
    print("-" * 35)

    audit_id = generate_audit_id()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    errors = []
    warnings = []

    patient_name = input("Enter patient name: ").strip()
    if patient_name == "":
        errors.append("Patient name cannot be empty")

    age = get_numeric_input("Enter age: ")
    heart_rate = get_numeric_input("Enter heart rate (bpm): ")
    systolic = get_numeric_input("Enter systolic BP: ")
    diastolic = get_numeric_input("Enter diastolic BP: ")

    allergy = input("Any allergies? (yes/no): ").strip().lower()

    if age is None or not (0 <= age <= 120):
        errors.append("Age must be a number between 0 and 120")

    if heart_rate is None:
        errors.append("Heart rate must be numeric")

    if systolic is None or diastolic is None:
        errors.append("Blood pressure values must be numeric")
    elif systolic <= diastolic:
        errors.append("Systolic BP must be greater than diastolic BP")

    if allergy not in ("yes", "no"):
        errors.append("Allergy field must be either 'yes' or 'no'")

    if heart_rate is not None and not (40 <= heart_rate <= 180):
        warnings.append("Heart rate outside safe range (40–180 bpm)")

    if systolic is not None and not (70 <= systolic <= 200):
        warnings.append("Systolic BP outside safe range (70–200)")

    if diastolic is not None and not (40 <= diastolic <= 130):
        warnings.append("Diastolic BP outside safe range (40–130)")

    if errors:
        status = "FAIL"
    elif warnings:
        status = "REVIEW"
    else:
        status = "PASS"

    print("\nAudit Summary")
    print("-" * 35)
    print(f"Audit ID   : {audit_id}")
    print(f"Timestamp  : {timestamp}")
    print(f"Status     : {status}")

    if errors:
        print("\nValidation Errors:")
        for err in errors:
            print(f"- {err}")

    if warnings:
        print("\nSafety Warnings:")
        for warn in warnings:
            print(f"- {warn}")

    if status == "PASS":
        print("\nNo issues detected. Data is clean.")

    audit_record = {
        "audit_id": audit_id,
        "timestamp": timestamp,
        "patient_name": patient_name,
        "age": age,
        "heart_rate": heart_rate,
        "blood_pressure": {
            "systolic": systolic,
            "diastolic": diastolic
        },
        "allergy": allergy,
        "status": status,
        "errors": errors,
        "warnings": warnings
    }

    with open("audit_log.json", "a") as file:
        file.write(json.dumps(audit_record, indent=4))
        file.write("\n")

    print("\nAudit record saved to audit_log.json")

if __name__ == "__main__":
    run_audit()
