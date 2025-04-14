# playwrightmoodle


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


2. Set up .env file
In the root folder, create a file named .env and add your credentials:


PASSWORD=your_moodle_password
GEMINI_API_KEY=your_gemini_api_key
Make sure your Gemini API key is valid and has access to the model.

3. Update Username in the Script
In the Python script, change this line to your actual Moodle username:


USERNAME = "your_account"

4. Run the Script

python main.py
If your filename is different from main.py, make sure to run the correct filename.

📂 Output Files
homework.html
Contains both the extracted Moodle announcement and the Gemini-generated draft in a styled HTML format.

generated_code.py
Contains only the generated Python code for easy testing or editing.

💡 Notes
This tool is designed for academic support and learning enhancement.

It is ideal for:

Quickly extracting assignment instructions

Getting an AI-generated code draft with explanation

Saving time during early-stage development or documentation

⚠ Please use responsibly: Do not submit AI-generated content without personal review or editing. Make sure your submission reflects your own understanding.

🧠 Tech Stack
Playwright – Headless browser automation

Google Generative AI (Gemini) – Text and code generation

Python – Scripting and control flow

dotenv – Environment variable management

📸 Screenshots & Demo (Optional)
Add screenshots of the HTML output and Gemini reply here for visual demo.


