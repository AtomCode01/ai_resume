import requests
import json
import PyPDF2


# -------- GitHub --------
def get_all_repos(username):
    url = f"https://api.github.com/users/{username}/repos?per_page=100"

    response = requests.get(url)

    if response.status_code != 200:
        print("GitHub API failed")
        return []

    return response.json()


def select_repositories(repos):
    print("\nAvailable Repositories:\n")

    for i, repo in enumerate(repos):
        print(f"{i}: {repo['name']} ({repo['language']})")

    selected = input("\nEnter indices (comma-separated): ")

    indices = []
    for i in selected.split(","):
        if i.strip().isdigit():
            idx = int(i.strip())
            if 0 <= idx < len(repos):
                indices.append(idx)

    selected_data = []

    for i in indices[:5]:
        repo = repos[i]

        selected_data.append({
            "name": repo.get("name"),
            "description": (repo.get("description") or "")[:100],
            "language": repo.get("language")
        })

    return selected_data


# -------- LinkedIn PDF --------
def extract_text_from_pdf(pdf_path):
    text = ""

    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text


# -------- Save --------
def save_data(github_data, linkedin_data, job_description, filename="output.json"):

    data = {
        "github_projects": github_data,
        "linkedin_profile": linkedin_data,
        "job_description": job_description
    }

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print("Data saved successfully")


# -------- Run (Correct Flow) --------
username = input("Enter GitHub username: ")
pdf_path = input("Enter PDF path: ")

repos = get_all_repos(username)
github_data = select_repositories(repos)

linkedin_data = extract_text_from_pdf(pdf_path)

# -------- Job Description Input --------
print("\nPaste Job Description (type 'END' on a new line to finish):")

lines = []
while True:
    line = input()
    if line.strip().upper() == "END":
        break
    lines.append(line)

job_description = "\n".join(lines)

# -------- Debug --------
print("GitHub sample:", github_data)
print("LinkedIn text length:", len(linkedin_data))
print("Job description length:", len(job_description))

save_data(github_data, linkedin_data, job_description)
