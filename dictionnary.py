# Define a template for a student
student_template = {
    "name": "AZOULA Arthur",
    "academic_year": "3rd year",
    "units": [
        {
            "name": "Web Development",
            "credits": 12,
            "grade": "A"
        },
        {
            "name": "Database Management",
            "credits": 9,
            "grade": "B"
        },
        {
            "name": "Computer Networks",
            "credits": 8,
            "grade": "C"
        }
    ]
}

# Define the grade weight mapping
grade_weight_mapping = {
    "A": 4,
    "B": 3,
    "C": 2,
    "D": 1,
    "E": 0
}

# Additional students for comparisons
student2 = {
    "name": "Emma Johnson",
    "academic_year": "2nd year",
    "units": [  
        {
            "name": "Data Science",
            "credits": 10,
            "grade": "A"
        },
        {
            "name": "Statistics",
            "credits": 8,
            "grade": "B"
        },
        {
            "name": "Machine Learning",
            "credits": 9,
            "grade": "A"
        }
    ]
}

student3 = {
    "name": "Michael Smith",
    "academic_year": "4th year",
    "units": [
        {
            "name": "Advanced Programming",
            "credits": 11,
            "grade": "A"
        },
        {
            "name": "Software Engineering",
            "credits": 10,
            "grade": "A"
        },
        {
            "name": "Database Design",
            "credits": 8,
            "grade": "B"
        }
    ]
}

student4 = {
    "name": "Olivia Brown",
    "academic_year": "1st year",
    "units": [
        {
            "name": "Intro to Computer Science",
            "credits": 9,
            "grade": "B"
        },
        {
            "name": "Mathematics Fundamentals",
            "credits": 7,
            "grade": "C"
        },
        {
            "name": "English Composition",
            "credits": 6,
            "grade": "A"
        }
    ]
}

# Calculate GPA and total credits for the template
total_credits = sum(unit["credits"] for unit in student_template["units"])
student_template['total_credits'] = total_credits

total_weighted_points = sum(grade_weight_mapping[unit["grade"]] * unit["credits"] for unit in student_template["units"])
gpa = total_weighted_points // total_credits if total_credits > 0 else 0
student_template['GPA'] = gpa

print(student_template)

students = []

# Add the additional students to the list
students = [student2, student3, student4, student_template]

# sortby name
students.sort(key=lambda x: x["name"])

print(f"\n --------- {students} -------- \n")

# sort by GPA

students.sort(key=lambda x: x["GPA"])

print(f"\n --------- {students} -------- \n")

# Sort by GPA

students.sort(key=lambda x: x['GPA'], reverse=True)




