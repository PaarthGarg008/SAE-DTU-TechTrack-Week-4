# SAE-DTU-TechTrack-Week-4
# Resume Keyword Checker

## Project Overview

The Resume Keyword Checker is a Python-based automation tool that compares a candidate's resume with a job description (JD) and calculates how well the resume matches the required skills.

The project extracts skills from the **Technical Skills** section of the resume and the **Required Skills** section of the job description using **Regular Expressions (Regex)**. It then identifies matched and missing skills and generates a detailed report.

This project was developed as part of the **SAE-DTU FORGETRACK 2026 Tech Track - Week 4**.

---

## Features

* Reads Resume and Job Description text files.
* Extracts skills using Regular Expressions (Regex).
* Compares resume skills with job requirements.
* Displays matched skills.
* Displays missing skills.
* Calculates Resume Match Score.
* Generates a report file (`report.txt`).
* Handles common errors gracefully.
* Supports both terminal execution and default file execution.

---

## Technologies Used

* Python
* Regular Expressions (`re`)
* File Handling
* Command Line Arguments (`sys`)

---

## How It Works

1. The program reads the Resume and Job Description files.
2. It extracts the **Technical Skills** section from the resume.
3. It extracts the **Required Skills** section from the job description.
4. Skills from both files are compared.
5. The program displays:

   * Matched Skills
   * Missing Skills
   * Match Score
6. A report is automatically saved in `report.txt`.

---

## Resume Format

The resume should contain a section named:

```text
TECHNICAL SKILLS
Python
SQL
Pandas
NumPy
Machine Learning
Git

PROJECTS
...
```

---

## Job Description Format

The job description should contain a section named:

```text
Required Skills:
Python
SQL
Pandas
Machine Learning
Power BI
Tableau

Preferred Skills:
Communication
Teamwork
```

---

## Usage

### Method 1: Run using terminal arguments

```bash
python Resume_Keyword_Checker.py Resume.txt JD.txt
```

### Method 2: Click the Run button in VS Code

If no command-line arguments are provided, the program automatically uses:

```text
Resume.txt
JD.txt
```

---

## Error Handling

The project handles:

* Missing files
* Empty files
* Missing "Technical Skills" section in Resume
* Missing "Required Skills" section in Job Description

---

## Future Improvements

* Support PDF and DOCX resumes.
* Add Graphical User Interface (GUI).
* Improve ATS-style keyword matching.
* Visualize match score using charts.

---

## Author

**Paarth Garg**


