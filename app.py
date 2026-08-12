import sqlite3

def initialize_database():

    conn = sqlite3.connect("projects.db")
    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    client TEXT,
    location TEXT,
    total_devices INTEGER,
    completed_devices INTEGER,
    open_issues INTEGER,
    completion_percentage REAL,
    status TEXT,
    health TEXT
    )
    """)

    conn.commit()
    return conn, cursor

conn, cursor = initialize_database()

print("IT Deployment Tracker")
projects = []

def display_title():
    print("\n=== IT DEPLOYMENT TRACKER ===")

def save_project(project):
    cursor.execute("""
        INSERT INTO PROJECTS (
         name,
         client, 
         location,
         total_devices,
         completed_devices,
         open_issues,
         completion_percentage,
         status,
         health
     )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            project["name"],
            project["client"],
            project["location"],
            project["total_devices"],
            project["completed_devices"],
            project["open_issues"],
            project["completion_percentage"],
            project["status"],
            project["health"]
    ))
    
    conn.commit()

def load_projects():
    cursor.execute("SELECT * FROM projects")
    return cursor.fetchall()
 
def create_project():

    project_name = input("Enter project name: ")
    client_name = input("Enter client name: ")
    location = input("Enter project location: ")
    total_devices = int(input("Enter total number of devices: "))
    completed_devices = int(input("Enter number of completed devices: "))

    open_issues = int(input("Enter number of open issues: "))

    project = {
        "name": project_name,
        "client": client_name,
        "location": location,
        "total_devices": total_devices,
        "completed_devices": completed_devices,
        "open_issues": open_issues
    }

    if open_issues == 0:
        project_health = "Good"
    elif open_issues <= 3:
        project_health = "Needs Attention"
    else:
        project_health = "At Risk"

    completion_percentage = round((completed_devices / total_devices) * 100, 1)
    if completion_percentage == 0:
        project_status = "Not Started"
    elif completion_percentage < 100:
        project_status = "In Progress"
    else:
        project_status = "Completed"

    remaining_devices = total_devices - completed_devices

    project["remaining_devices"] = remaining_devices
    project["completion_percentage"] = completion_percentage
    project["status"] = project_status
    project["health"] = project_health

    projects.append(project)
    save_project(project)
    return project 

display_title()
number_of_projects = int(input("How many projects would you like to create? "))

for i in range(number_of_projects):
    print("\n--- Project", i + 1, "---")
    create_project()
print("\nTotal projects:", len(projects))

for project in projects:
    print("\nProject:", project["name"])
    print("Client:", project["client"])
    print("Location:", project["location"])
    print("Progress:", project["completion_percentage"], "%")
    print("Status:", project["status"])
    print("Health:", project["health"])

saved_projects = load_projects()
print("\nProjects saved in database:", len(saved_projects))
