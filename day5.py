import uuid
import json
from datetime import datetime

def get_number(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        return None

def run_audit():
    print("Clinical Data Audit System")
    print("-" * 40)

    audit_id = str(uuid.uuid4())
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    errors = []
    warnings = []

    patient_name = input("Enter patient name: ").strip()
    if patient_name == "":
        errors.append("Patient name cannot be empty")

    age = get_number("Enter age: ")
    heart_rate = get_number("Enter heart rate (bpm): ")
    systolic = get_number("Enter systolic BP: ")
    diastolic = get_number("Enter diastolic BP: ")
    allergy = input("Any allergies? (yes/no): ").strip().lower()

    if age is None or not (0 <= age <= 120):
        errors.append("Invalid age")

    if heart_rate is None:
        errors.append("Invalid heart rate")

    if systolic is None or diastolic is None:
        errors.append("Invalid blood pressure values")
    elif systolic <= diastolic:
        errors.append("Systolic BP must be greater than diastolic BP")

    if allergy not in ("yes", "no"):
        errors.append("Invalid allergy input")

    if heart_rate is not None and not (40 <= heart_rate <= 180):
        warnings.append("Heart rate outside safe range")

    if systolic is not None and not (70 <= systolic <= 200):
        warnings.append("Systolic BP outside safe range")

    if diastolic is not None and not (40 <= diastolic <= 130):
        warnings.append("Diastolic BP outside safe range")

    if errors:
        status = "FAIL"
    elif warnings:
        status = "REVIEW"
    else:
        status = "PASS"

    print("\nAudit Report")
    print("-" * 40)
    print("Audit ID:", audit_id)
    print("Timestamp:", timestamp)
    print("Patient Name:", patient_name)
    print("Audit Status:", status)

    if errors:
        print("\nFlags:")
        for e in errors:
            print("-", e)
    else:
        print("\nFlags: None")

    if warnings:
        print("\nWarnings:")
        for w in warnings:
            print("-", w)
    else:
        print("\nWarnings: None")

    print("\nDisclaimer: This is a non-diagnostic audit report only. Not medically certified.")

    audit_record = {
        "audit_id": audit_id,
        "timestamp": timestamp,
        "patient_name": patient_name,
        "status": status,
        "flags": errors,
        "warnings": warnings
    }

    with open("audit_log.json", "a") as file:
        file.write(json.dumps(audit_record))
        file.write("\n")

    print("\nAudit record appended to audit_log.json")

if __name__ == "__main__":
    run_audit()
