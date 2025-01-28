import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
import re
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    st.error("Google API Key is missing. Please add it to your .env file.")
else:
    genai.configure(api_key=API_KEY)

# Function to get Gemini API response
def get_gemini_response(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.0-pro")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating response: {e}"

# PDF to text conversion function
def input_pdf_text(uploaded_file):
    try:
        reader = pdf.PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:  # Directly iterate over the pages object
            raw_text = page.extract_text()
            if raw_text:
                text += raw_text + "\n"
        # Clean the extracted text
        clean_text = " ".join(text.split())
        return clean_text
    except Exception as e:
        return None

# Preprocess text for better comprehension
def preprocess_text(text):
    # Normalize and clean text
    text = text.lower()
    text = re.sub(r"[^\w\s.,-]", "", text)  # Remove special characters
    text = re.sub(r"\s+", " ", text)        # Replace multiple spaces with a single space
    return text

# Input prompt template for Gemini API
input_prompt = """
Act as an extremely advanced and skilled Application Tracking System (ATS) with expertise in analyzing resumes for technical roles. You should have a deep understanding of various technical fields, including software engineering, full-stack development, front-end and back-end development, data science, data analytics, big data engineering, artificial intelligence, business intelligence, machine learning, cybersecurity, blockchain, Web3, crypto, research engineering, database systems (SQL and NoSQL), data structures and algorithms, DevOps, advanced tools like Kali Linux, Docker, Kubernetes, Tableau, and much more.

Your role is to evaluate resumes against job descriptions (JD) in a highly competitive job market. Perform a comprehensive and detailed analysis by following these steps:

1. Skills and Profile Matching
> Carefully match the candidate skills, experiences, and projects listed in the resume with the requirements in the job description.
> Identify both hard skills (e.g., programming languages, frameworks, tools) and soft skills (e.g., leadership, collaboration, problem-solving) that align with the JD.

2. Keyword Analysis
> Extract critical keywords and phrases from the job description that represent required qualifications, skills, tools, or tasks.
> Check whether these keywords are present in the resume and identify any gaps or missing terms that are essential for ATS optimization.

3. Contextual Assessment
> Evaluate how well the achievements, job roles, and responsibilities described in the resume align with the specific duties and expectations outlined in the JD.
> Assess whether the candidate has adequately demonstrated proficiency in the required tools and technologies in real-world applications.

4. Competitiveness in the Job Market
> Consider that the tech job market is extremely competitive, and provide actionable recommendations to make the resume stand out.
> Ensure suggestions align with best practices for ATS optimization and human recruiter preferences.

5. JD Match Percentage
> Provide a percentage score indicating the resume's alignment with the JD based on skills, experiences, and relevance.

6. Feedback and Suggestions
> Offer actionable feedback to enhance the resume. For example, suggest adding missing skills, rephrasing bullet points, or emphasizing accomplishments to improve both ATS compatibility and recruiter impressions.

Your response must follow this exact format:
JD Match: [Percentage score]% '\n'
Missing Keywords: [List of keywords missing in the resume] '\n'
Experts' Opinion: [A clear, concise, and actionable evaluation of the candidate's profile, mentioning strengths, missing areas, and specific improvements that can be made.] '\n'

Each part should be on a new line, separated by `\n` for readability.

Input Details:
Resume Text: {text}
Job Description: {jd}

Example Response:
JD Match: 85%
Missing Keywords: Cloud Computing, AWS, Kubernetes
Experts' Opinion: The candidate demonstrates strong expertise in Python, data analytics, and software engineering. However, there is a lack of experience in cloud computing technologies like AWS and Kubernetes, which are crucial for this role. Overall, the profile aligns well with the JD but can be further optimized with targeted additions.

Ensure that you provide the response in plain text format similarly as shown in the example, without any JSON-style formatting. The response should be thorough, easy to read and contain clear feedback to help the candidate improve their resume.
"""

# Streamlit app
st.title("Smart Resume ATS Optimizer")
st.write("This app will help you optimize your resume for Applicant Tracking Systems (ATS).")
jd = st.text_area("Enter the job description here:")
uploaded_file = st.file_uploader("Upload your resume in PDF format:", type=["pdf"], help="Please upload your resume in PDF format.")

submit = st.button("Submit")

if submit:
    if not API_KEY:
        st.error("API Key not configured. Unable to proceed.")
    elif not uploaded_file:
        st.error("Please upload a PDF file to proceed.")
    elif not jd.strip():
        st.error("Please enter the job description to proceed.")
    else:
        with st.spinner("Processing your resume..."):
            # Extract text from the uploaded PDF file
            extracted_text = input_pdf_text(uploaded_file)
            if extracted_text:
                resume_text = preprocess_text(extracted_text)
                try:
                    # Format the prompt with an f-string for proper interpolation
                    prompt = input_prompt.format(text=resume_text, jd=jd)
                    
                    # Debug: Print the final prompt to verify the structure
                    # st.write("Generated Prompt:\n", prompt)
                    
                    response = get_gemini_response(prompt)
                    st.subheader("Resume Analysis and Feedback:")
                    st.write(response)
                except Exception as e:
                    st.error(f"Error generating response: {e}")
            else:
                st.error("Failed to extract text from the uploaded PDF file. Please try again with a different file.")
