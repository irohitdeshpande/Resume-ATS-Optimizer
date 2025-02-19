# Smart Resume ATS Optimizer

## Overview
The **Smart Resume ATS Optimizer** is a web application built using **Streamlit**, **Google Gemini API**, and **PyPDF2**. It analyzes resumes against job descriptions to provide detailed feedback on how well the resume aligns with the requirements specified in the job description. This tool helps optimize resumes for **Applicant Tracking Systems (ATS)** by identifying missing keywords, matching skills, and providing suggestions for improvement.

## Features
- **Resume Upload**: Upload your resume in PDF format, and the app will extract the text.
- **Job Description Input**: Enter the job description to compare your resume with the job requirements.
- **ATS Analysis**: The app uses the **Google Gemini API** to analyze the alignment between your resume and the job description.
- **Feedback and Suggestions**: Get actionable feedback on matching skills, missing keywords, and suggestions to improve your resume for both ATS and human recruiters.

## Setup Instructions

### 1. Create and activate a virtual environment:

For MacOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

For Windows:
```bash
python3 -m venv venv
venv\Scripts\activate
```

### 2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

### 3. Set up your Google Gemini API key:
Create a `.env` file in the root directory of the project. Add your API key to the `.env` file:
```makefile
GOOGLE_API_KEY=your-api-key-here
```

### 4. Run the Streamlit app:
```bash
streamlit run app.py
```
This will start the Streamlit server, and you can access the app by visiting [http://localhost:8501](http://localhost:8501) in your browser.

## How It Works

1. **Upload a Resume**:
    Upload your resume as a PDF file. The app uses PyPDF2 to extract the text from the document.

2. **Enter Job Description**:
    Paste the job description into the text box. The app compares your resume's content against the job description to check for alignment.

3. **ATS Analysis**:
    The extracted text and job description are sent to the Google Gemini API for analysis. The API evaluates how well your resume matches the job description, focusing on keywords, skills, and overall relevance.

4. **Get Feedback**:
    Once the analysis is complete, you will receive detailed feedback, including:
    - **Matching skills and keywords**: Highlights the skills and tools that match the job description.
    - **Missing keywords**: Identifies essential skills or technologies missing from your resume.
    - **Suggestions**: Provides recommendations for improving your resume's ATS optimization and overall presentation.

## Example Output
Here is an example of what the resume analysis output might look like:
```json
{
  "JD Match": "85%", 
  "Missing Keywords": ["Cloud Computing", "AWS", "Kubernetes"],
  "Profile Summary": "The candidate demonstrates strong expertise in Python, data analytics, and software engineering. However, there is a lack of experience in cloud computing technologies like AWS and Kubernetes, which are crucial for this role. Overall, the profile aligns well with the JD but can be further optimized with targeted additions."
}
```

## Technologies Used
- **Streamlit**: For creating the interactive web app interface.
- **Google Gemini API**: For processing and analyzing the resume against the job description.
- **PyPDF2**: For extracting text from PDF resumes.
- **dotenv**: For securely managing environment variables like the API key.

## Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Please make sure to follow the project's coding style and include tests for any new features or bug fixes.

## Example
![image](https://github.com/user-attachments/assets/47d2bd40-13ab-4c98-8af5-533033435c5a)


This `README.md` provides a detailed and structured guide on setting up, using, and understanding the project. It includes sections for installation, usage, and example output, making it clear for anyone new to the project to get started.
