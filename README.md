# AI Resume Builder (LaTeX Template-Based)

A structured resume generation system that converts user data (GitHub, LinkedIn PDF, job description) into a professional LaTeX resume using a fixed template.

---

## Overview

This project separates concerns into three layers:

1. **Data Collection** → GitHub + LinkedIn PDF + Job Description
2. **AI Processing** → Converts raw data into structured resume content
3. **Template Rendering** → Injects content into a fixed LaTeX template

This avoids unreliable AI-generated formatting and ensures consistent, professional output.

---

## Key Features

* GitHub repository selection and extraction
* LinkedIn PDF parsing
* Job description integration
* AI-based structured resume generation
* Fixed LaTeX template for consistent formatting
* Downloadable `.tex` resume file

---

## Project Structure

```
project/
│
├── app.py              # Streamlit frontend
├── calling.py          # AI API interaction (structured JSON output)
├── formatter.py        # Converts structured data → LaTeX
├── template.tex        # Resume layout (fixed structure)
├── output.json         # Intermediate data file
├── scrap.py            # Data collection (GitHub + PDF)
├── .env                # API keys (not committed)
```

---

## How It Works

```
User Input (UI)
   ↓
output.json (raw structured data)
   ↓
AI (calling.py)
   ↓
Structured Resume JSON
   ↓
formatter.py
   ↓
template.tex
   ↓
Final resume.tex
```

---

## Setup

### 1. Install dependencies

```
pip install streamlit requests PyPDF2 python-dotenv openai
```

---

### 2. Add API Key

Create a `.env` file:

```
NVIDIA_API_KEY=your_api_key_here
```

---

### 3. Run the app

```
streamlit run app.py
```

---

## Usage

1. Enter GitHub username
2. Select relevant repositories
3. Upload LinkedIn PDF
4. Paste job description
5. Click **Generate Resume**
6. Download `.tex` file

---

## Important Design Decisions

### 1. Template-based LaTeX

AI does NOT generate LaTeX directly.
Instead:

* AI → structured JSON
* Formatter → injects into template

This ensures:

* consistent formatting
* fewer errors
* easier debugging

---

### 2. Separation of Concerns

| Component    | Responsibility    |
| ------------ | ----------------- |
| app.py       | UI + flow control |
| calling.py   | AI interaction    |
| formatter.py | LaTeX generation  |
| template.tex | layout            |

---

## Current Limitations

* Output quality depends on input data quality
* LinkedIn PDF extraction is noisy
* AI may produce generic or weak bullet points
* No built-in PDF generation (LaTeX only)
* No ranking of GitHub projects

---

## Future Improvements

### High Priority

* Improve prompt for better bullet points
* Extract skills from job description
* Rank projects based on relevance

### Medium Priority

* Multiple resume templates
* Better LinkedIn parsing
* Section-wise AI processing

### Advanced

* PDF generation via LaTeX engine or service
* Docker-based deployment with LaTeX support
* Fine-tuned model for resume writing

---

## Notes

* This project focuses on **structure and reliability**, not creative formatting
* Resume quality depends more on **prompt design and input filtering** than code
* Template control is intentional to match industry-standard resumes

---

## License

Open for personal use and modification.
But just let me know, i love to see development in this.
