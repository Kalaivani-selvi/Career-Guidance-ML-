import pandas as pd
import random

# Define the list of UG Courses and their respective specializations
ug_courses = {
    "BA": ["English Literature", "History", "Economics", "Psychology"],
    "BSc": ["Physics", "Chemistry", "Mathematics", "Biology"],
    "BCom": ["Accounting", "Finance", "Marketing", "Management"],
    "BE or BTech": ["Computer Science", "Electrical Engineering", "Mechanical Engineering", "Civil Engineering"],
    "BFA": ["Fine Arts", "Sculpture", "Painting", "Graphic Design"],
    "BBA": ["Business Administration", "Entrepreneurship", "International Business", "Human Resource Management"],
    "BArch": ["Architecture", "Urban Planning", "Interior Design", "Landscape Architecture"],
    "BCA": ["Computer Applications", "Information Technology", "Software Engineering", "Web Development"],
    "BEd": ["Elementary Education", "Secondary Education", "Special Education", "Early Childhood Education"],
    "BSA": ["Astronomy", "Astrophysics", "Space Engineering", "Space Technology"]
}

# Define job roles according to UG courses
job_roles = {
    "BA": ["Content Writer", "Social Media Manager", "Marketing Coordinator",
           "Human Resources Assistant", "Public Relations Specialist", "Event Planner",
           "Copywriter", "Customer Service Representative", "Journalist", "Fundraiser"],
    "BSc": ["Research Scientist", "Lab Technician", "Data Analyst",
            "Environmental Scientist", "Pharmaceutical Sales Representative",
            "Biomedical Engineer", "Statistician", "Quality Control Analyst",
            "Forensic Scientist", "Epidemiologist"],
    "BCom": ["Accountant", "Financial Analyst", "Sales Executive",
             "Business Consultant", "Investment Analyst", "Risk Analyst",
             "Tax Consultant", "Auditor", "Retail Manager", "E-commerce Manager"],
    "BE or BTech": ["Software Engineer", "Mechanical Engineer",
                    "Electrical Engineer", "Civil Engineer",
                    "Aerospace Engineer", "Biomedical Engineer",
                    "Robotics Engineer", "Chemical Engineer",
                    "Automotive Engineer", "Network Engineer"],
    "BFA": ["Graphic Designer", "Illustrator", "Art Director",
            "Animator", "Multimedia Artist", "Film and Video Editor",
            "Photographer", "Interior Designer", "Art Teacher",
            "Gallery Curator"],
    "BBA": ["Marketing Manager", "Financial Analyst", "Operations Manager",
            "Human Resources Manager", "Business Development Manager",
            "Sales Manager", "Project Manager", "Management Consultant",
            "Entrepreneur", "Supply Chain Manager"],
    "BArch": ["Architect", "Urban Planner", "Interior Designer",
              "Landscape Architect", "Construction Manager", "Sustainability Consultant",
              "Historic Preservationist", "Building Inspector", "CAD Technician",
              "Real Estate Developer"],
    "BCA": ["Software Developer", "Database Administrator", "Web Developer",
            "Network Administrator", "Systems Analyst", "IT Consultant",
            "Game Developer", "Computer Programmer", "UI/UX Designer",
            "Cybersecurity Analyst"],
    "BEd": ["Teacher", "School Counselor", "Education Administrator",
            "Curriculum Developer", "Instructional Designer", "Education Consultant",
            "Special Education Teacher", "ESL Teacher", "School Librarian",
            "Tutor"],
    "BSA": ["Space Artist", "Spacecraft Designer", "Space Musician",
            "Astrobiologist", "Galactic Historian", "Cosmic Philosopher",
            "Exoplanetary Geologist", "Intergalactic Diplomat", "Astro-Ethnographer",
            "Interstellar Photographer"]
}

# Define the range for each rating
rating_ranges = {
    "cgpa": (1, 10),
    "historyofBacklogs": (0, 15),
    "computerLiteracy": (0, 10),
    "problemSolving": (0, 10),
    "TechnicalSkill": (0, 10),
    "ResearchSkill": (0, 10),
    "communicationSkill": (0, 10),
    "interpersonalSkill": (0, 10),
    "teamwork": (0, 10),
    "adaptability": (0, 10),
    "timeManagement": (0, 10),
    "emotionalIntelligence": (0, 10),
    "continousLearning": (0, 10),
    "leadership": (0, 10)
}

# Function to generate synthetic data
def generate_data(num_samples):
    data = []
    for _ in range(num_samples):
        sample = {}
        # Randomly select a UG Course and Specialization
        ug_course = random.choice(list(ug_courses.keys()))
        ug_specialization = random.choice(ug_courses[ug_course])
        sample["ugCourse"] = ug_course
        sample["ugSpecialization"] = ug_specialization
        
        # Assign job role based on UG course
        sample["jobRole"] = random.choice(job_roles[ug_course])
        
        # Generate random ratings for each rating field
        for field, (min_val, max_val) in rating_ranges.items():
            sample[field] = round(random.uniform(min_val, max_val), 1)
        
        data.append(sample)
    return data

# Generate synthetic dataset with 100 samples
synthetic_data = generate_data(10000)

# Convert the data to a pandas DataFrame
df = pd.DataFrame(synthetic_data)

# Save the DataFrame to a CSV file
df.to_csv("bharani.csv", index=False)

# Display the DataFrame
print(df)
