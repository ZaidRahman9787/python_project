# =========================
# CORE UTILITIES
# =========================

def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "F"


def performance_tag(avg):
    if avg >= 85:
        return "Top Performer"
    elif avg >= 65:
        return "Stable"
    else:
        return "Needs Improvement"


# =========================
# STUDENT OPERATIONS
# =========================

def add_student(students):
    print("\n--- Add New Student ---")

    name = input("Full Name: ").strip().title()
    roll = input("Roll Number: ").strip()
    branch = input("Branch: ").strip().upper()

    fav_subjects = input("Enter 3 subjects (comma separated): ").split(',')
    fav_subjects = [s.strip().title() for s in fav_subjects if s.strip()]

    if len(fav_subjects) != 3:
        print("Exactly 3 subjects required.")
        return

    marks = {}
    for sub in fav_subjects:
        while True:
            try:
                score = float(input(f"Marks in {sub}: "))
                if 0 <= score <= 100:
                    marks[sub] = score
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Invalid numeric value.")

    skills = set(
        s.strip().title()
        for s in input("Technical skills (comma separated): ").split(',')
        if s.strip()
    )

    total = sum(marks.values())
    avg = total / len(marks)
    grade = calculate_grade(avg)
    tag = performance_tag(avg)

    student = {
        "id": str(uuid.uuid4())[:8],
        "name": name,
        "roll": roll,
        "branch": branch,
        "subjects": sorted(fav_subjects),
        "marks": marks,
        "skills": list(skills),
        "total": total,
        "average": round(avg, 2),
        "grade": grade,
        "tag": tag
    }

    students.append(student)
    print(f"\n{name} added successfully with ID {student['id']}.")


# =========================
# VIEW & SEARCH
# =========================

def view_all_students(students):
    if not students:
        print("\nNo student data available.")
        return

    print("\n===== STUDENT RECORDS =====")
    for s in students:
        print("\n---------------------------")
        print(f"ID        : {s['id']}")
        print(f"Name      : {s['name']}")
        print(f"Roll      : {s['roll']}")
        print(f"Branch    : {s['branch']}")
        print(f"Subjects  : {s['subjects']}")
        print(f"Marks     : {s['marks']}")
        print(f"Total     : {s['total']}")
        print(f"Average   : {s['average']}")
        print(f"Grade     : {s['grade']}")
        print(f"Tag       : {s['tag']}")
        print(f"Skills    : {s['skills']}")

        if s['average'] < 50:
            print("⚠ Academic Risk Detected")


def search_student(students):
    key = input("Enter Roll or Name to search: ").strip().lower()

    found = False
    for s in students:
        if key in s['roll'].lower() or key in s['name'].lower():
            found = True
            print("\n--- Student Found ---")
            print(f"{s['name']} | Roll: {s['roll']} | Avg: {s['average']} | Grade: {s['grade']}")

    if not found:
        print("No matching student found.")


# =========================
# ANALYTICS ENGINE
# =========================

def run_analytics(students):
    if not students:
        print("\nNo data available.")
        return

    print("\n===== ANALYTICS DASHBOARD =====")

    # Ranking
    ranked = sorted(students, key=lambda x: x['total'], reverse=True)
    print("\n--- Overall Ranking ---")
    for i, s in enumerate(ranked, 1):
        print(f"{i}. {s['name']} ({s['total']})")

    # Subject toppers
    print("\n--- Subject-wise Toppers ---")
    subjects = set()
    for s in students:
        subjects.update(s['marks'].keys())

    for sub in subjects:
        topper = max(
            (s for s in students if sub in s['marks']),
            key=lambda x: x['marks'][sub]
        )
        print(f"{sub}: {topper['name']} ({topper['marks'][sub]})")

    # Skill leaderboard
    print("\n--- Skill Leaderboard ---")
    skill_count = {}
    for s in students:
        for sk in s['skills']:
            skill_count[sk] = skill_count.get(sk, 0) + 1

    for sk, cnt in sorted(skill_count.items(), key=lambda x: x[1], reverse=True):
        print(f"{sk}: {cnt}")

    # Branch-wise average
    print("\n--- Branch Performance ---")
    branch_map = {}
    for s in students:
        branch_map.setdefault(s['branch'], []).append(s['average'])

    for b, avgs in branch_map.items():
        print(f"{b}: {sum(avgs)/len(avgs):.2f}")


# =========================
# MAIN LOOP
# =========================

def main():
    students = []

    while True:
        print("\n===== SIPAS MENU =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Analytics")
        print("5. Exit")

        choice = input("Select option: ").strip()

        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_all_students(students)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            run_analytics(students)
        elif choice == '5':
            print("System shutting down.")
            break
        else:
            print("Invalid option.")


if _name_ == "_main_":
    main()