import streamlit as st
import requests
import json
import PyPDF2
from openai import OpenAI
from calling import generate_latex_from_json


# GitHub ---------------------------------------------------
def get_all_repos(username):
    url = f"https://api.github.com/users/{username}/repos?per_page=100"
    response = requests.get(url)

    if response.status_code != 200:
        return []

    return response.json()


def process_selected_repos(repos, selected_indices):
    selected_data = []

    for i in selected_indices[:5]:
        repo = repos[i]

        selected_data.append({
            "name": repo.get("name"),
            "description": (repo.get("description") or "")[:100],
            "language": repo.get("language")
        })

    return selected_data


# PDF --------------------------------------------------------
def extract_text_from_pdf(uploaded_file):
    text = ""
    reader = PyPDF2.PdfReader(uploaded_file)

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text


# Save JSON --------------------------------------------------
def save_data(github_data, linkedin_data, job_description):
    data = {
        "github_projects": github_data,
        "linkedin_profile": linkedin_data,
        "job_description": job_description[:1000]
    }

    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    return data


# -------- UI ------------------------
st.title("Resume Data Builder")

username = st.text_input("Enter GitHub Username")

repos = []
selected_indices = []

if username:
    repos = get_all_repos(username)

    if repos:
        repo_options = [
            f"{i}: {repo['name']} ({repo['language']})"
            for i, repo in enumerate(repos)
        ]

        selected = st.multiselect(
            "Select up to 5 repositories",
            options=repo_options
        )

        selected_indices = [int(s.split(":")[0]) for s in selected]


uploaded_pdf = st.file_uploader("Upload LinkedIn PDF", type=["pdf"])

linkedin_data = ""
if uploaded_pdf:
    linkedin_data = extract_text_from_pdf(uploaded_pdf)
    st.success("PDF processed")


job_description = st.text_area("Paste Job Description")


#------------ -------- Submit ------------------------
if st.button("Generate Resume (LaTeX)"):

    if not username or not uploaded_pdf or not job_description:
        st.error("Please fill all inputs")
    else:
        github_data = process_selected_repos(repos, selected_indices)

        data = save_data(github_data, linkedin_data, job_description)

        st.success("Data prepared")

#--------- ----- Generate LaTeX --------
        json_path = "output.json"
        latex_output = generate_latex_from_json(json_path)

# ------------- Save .tex file --------
        with open("resume.tex", "w", encoding="utf-8") as f:
            f.write(latex_output)

        st.success("LaTeX generated")

# ----------------------- Download Button --------------------------
        st.download_button(
            label="Download LaTeX File",
            data=latex_output,
            file_name="resume.tex",
            mime="text/plain"
        )
        st.link_button("Copy Latex code, Click to go Latex compiler", "https://prism.openai.com/")

        st.link_button("Free online compiler for Latex :", "https://prism.openai.com/")

    #---------------------- Preview (optional) -------------------
        st.subheader("Preview (LaTeX)")
        st.code(latex_output, language="latex")
