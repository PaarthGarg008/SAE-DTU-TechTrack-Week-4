import re
import sys


# Read file
def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

        if text.strip() == "":
            print(f"Error: {filename} is empty.")
            return None

        return text.lower()

    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None


# Extract skills from Resume
def extract_resume_skills(text):

    # Extract text between "Technical Skills" and "Projects"
    match = re.search(
        r'technical skills(.*?)projects',
        text,
        re.DOTALL
    )

    if not match:
        print("Technical Skills section not found in Resume.")
        return set()

    skills_section = match.group(1)

    # Extract words and phrases separated by commas/new lines
    skills = re.findall(r'[a-zA-Z+#\-. ]+', skills_section)

    return set(skill.strip() for skill in skills if skill.strip())


# Extract skills from JD
def extract_jd_skills(text):

    # Extract text between "Required Skills" and "Preferred Skills"
    match = re.search(
        r'required skills:(.*?)(preferred skills:|$)',
        text,
        re.DOTALL
    )

    if match:
        skills_section = match.group(1)
    else:
        print("Required Skills section not found in JD.")
        return set()

    skills = re.findall(r'[a-zA-Z+#\-. ]+', skills_section)

    return set(skill.strip() for skill in skills if skill.strip())


# Save report
def save_report(score, matched, missing):

    with open("report.txt", "w", encoding="utf-8") as file:

        file.write("RESUME ANALYSIS REPORT\n\n")
        file.write(f"Match Score: {score:.2f}%\n\n")

        file.write("Matched Skills:\n")
        for skill in sorted(matched):
            file.write(f"✓ {skill}\n")

        file.write("\nMissing Skills:\n")
        for skill in sorted(missing):
            file.write(f"✗ {skill}\n")


# Main Program
def main():

    print("\n===== RESUME KEYWORD CHECKER =====\n")

    if len(sys.argv) == 3:
        resume_file = sys.argv[1]
        jd_file = sys.argv[2]
    else:
        print("No command-line arguments provided.")
        print("Using default files...\n")

        resume_file = "Resume.txt"
        jd_file = "JD.txt"

    print("Reading files...")

    resume_text = read_file(resume_file)
    jd_text = read_file(jd_file)

    if resume_text is None or jd_text is None:
        return

    print("Files loaded successfully.")

    # Extract skills
    resume_skills = extract_resume_skills(resume_text)
    jd_skills = extract_jd_skills(jd_text)

    # Find matched and missing skills
    matched = resume_skills.intersection(jd_skills)
    missing = jd_skills.difference(resume_skills)

    # Calculate score
    if len(jd_skills) == 0:
        score = 0
    else:
        score = (len(matched) / len(jd_skills)) * 100

    # Display Results
    print("\n----- RESULTS -----")

    print("\nMatched Skills:")
    if matched:
        for skill in sorted(matched):
            print("✓", skill)
    else:
        print("No matching skills found.")

    print("\nMissing Skills:")
    if missing:
        for skill in sorted(missing):
            print("✗", skill)
    else:
        print("No missing skills.")

    print(f"\nMatch Score: {score:.2f}%")

    # Suggestion
    if score >= 70:
        print("Excellent Match!")
    elif score >= 40:
        print("Average Match.")
    else:
        print("Poor Match. Improve your resume.")

    # Save report
    save_report(score, matched, missing)

    print("\nReport saved as report.txt")


if __name__ == "__main__":
    main()