# playwrightmoodle

[korean]()

# 📘  Auto Extractor & Gemini Draft Generator

This Python tool combines **Playwright automation** with **Google's Gemini API** to help you:

- Automatically log in to NTNU's Moodle
- Extract assignment instructions
- Generate a complete code draft with explanation
- Output a structured HTML page and `.py` script

---

## 🚀 Features

- ✅ Auto-login to NTNU Moodle
- ✅ Navigate to the "1132 Programming Language" course
- ✅ Locate and open the announcement titled **"Assignment 4 Requirements"**
- ✅ Extract the assignment content from Moodle
- ✅ Send content to **Gemini** for AI-based code and draft generation
- ✅ Format everything into a clean HTML output
- ✅ Save the generated Python code to a separate `.py` file

---

## 🛠 How to Use

### 1. Install Dependencies

```bash
pip install python-dotenv playwright google-generativeai
playwright install
```

### 2. Set up `.env` File
Create a .env file in the root folder and add your credentials:

```
PASSWORD=your_moodle_password
GEMINI_API_KEY=your_gemini_api_key
```
### 3. Update Username in the Script
Open the Python script and replace the default username with your actual Moodle account:
```
USERNAME = "your_account"
```

### 4. Run the Script
```
python main.py
```
### 📂 Output Files
```
homework.html
```
A styled HTML file containing:

-The extracted Moodle assignment content

-Gemini-generated code and explanation
```
generated_code.py
```
A standalone Python file with the AI-generated code, ready for testing or editing.
### 💡 Notes
his tool is intended for educational support and code prototyping.

It is best used for:

✏️ Rapid assignment content extraction

🤖 AI-generated code with clear explanations

💼 Saving time during early-stage development
### 🧠 Tech Stack

Playwright – Headless browser automation

Google Generative AI (Gemini) – Text and code generation

Python – Scripting and automation

dotenv – Secure environment variable management
