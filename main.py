import streamlit as st
from chains import Chain
from portfolio import Portfolio
from utils import clean_text
from langchain_community.document_loaders import WebBaseLoader
import time

st.set_page_config(
    page_title="Cold Email Generator",
    page_icon="📧",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-header {
        font-size: 42px;
        font-weight: 600;
        color: #1E88E5;
        margin-bottom: 20px;
    }
    .sub-header {
        font-size: 24px;
        font-weight: 500;
        color: #424242;
        margin-bottom: 20px;
    }
    .card {
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        background-color: #FFFFFF;
    }
    .job-title {
        font-size: 20px;
        font-weight: 600;
        color: #1E88E5;
        margin-bottom: 10px;
    }
    .job-detail {
        margin-bottom: 5px;
        color: #424242;
    }
    .email-container {
        background-color: #f8f9fa;
        border-left: 4px solid #1E88E5;
        padding: 15px;
        border-radius: 5px;
        margin-top: 15px;
    }
    .logo-text {
        font-weight: bold;
        color: #1E88E5;
    }
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background-color: #f8f9fa;
        padding: 10px 20px;
        text-align: center;
        border-top: 1px solid #e0e0e0;
        font-size: 12px;
        color: #616161;
    }
    .stButton button {
        background-color: #1E88E5;
        color: white;
        font-weight: 600;
        padding: 10px 25px;
        border-radius: 5px;
        border: none;
        transition: all 0.3s;
    }
    .stButton button:hover {
        background-color: #1565C0;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    .stProgress > div > div {
        background-color: #1E88E5;
    }
</style>
""", unsafe_allow_html=True)

def main():
    chain_instance = Chain()
    portfolio_instance = Portfolio()
    
    with st.sidebar:
        st.markdown('<div style="padding: 20px 10px;">', unsafe_allow_html=True)
        st.markdown("<h2 style='font-weight: bold; color: #1E88E5;'>Cold Email Generator</h2>", unsafe_allow_html=True)
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("""
        <p>Generate personalized cold emails for job opportunities by analyzing career pages.</p>
        <h3>How it works:</h3>
        <ol>
            <li>Enter the URL of a company's career page</li>
            <li>Our AI extracts job details</li>
            <li>Personalized emails are generated for each job</li>
        </ol>
        <h3>Tips:</h3>
        <ul>
            <li>Use complete URLs including 'https://'</li>
            <li>For best results, use direct career page URLs</li>
            <li>Copy the generated emails and customize as needed</li>
        </ul>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<h1 style='font-size: 42px; font-weight: 600; color: #1E88E5; margin-bottom: 20px;'>📧 Smart Cold Email Generator</h1>", unsafe_allow_html=True)
    st.markdown("<p>Generate targeted cold emails by analyzing job opportunities from company career pages</p>", unsafe_allow_html=True)
    
    st.markdown("<h2 style='font-size: 24px; font-weight: 500; color: #424242; margin-bottom: 20px;'>Enter Career Page URL</h2>", unsafe_allow_html=True)
    url_input = st.text_input("", placeholder="https://example.com/careers", help="Enter the complete URL of the company's career page")
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        submit_button = st.button("Generate Emails", use_container_width=True)
    
    if submit_button and url_input:
        with st.spinner("Processing website content..."):
            try:
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                status_text.markdown("<p style='font-style: italic; color: #616161;'>🔍 Extracting content from website...</p>", unsafe_allow_html=True)
                loader = WebBaseLoader([url_input])
                raw_content = loader.load()
                data = clean_text(raw_content[0].page_content)
                progress_bar.progress(30)
                time.sleep(0.5)
                
                status_text.markdown("<p style='font-style: italic; color: #616161;'>📂 Loading portfolio data...</p>", unsafe_allow_html=True)
                portfolio_instance.load_portfolio()
                progress_bar.progress(50)
                time.sleep(0.3)
                
                status_text.markdown("<p style='font-style: italic; color: #616161;'>🧠 Analyzing job opportunities...</p>", unsafe_allow_html=True)
                jobs = chain_instance.extract_jobs(data)
                progress_bar.progress(70)
                time.sleep(0.5)
                
                status_text.markdown("<p style='font-style: italic; color: #616161;'>✍️ Crafting personalized emails...</p>", unsafe_allow_html=True)
                progress_bar.progress(90)
                time.sleep(0.3)
                
                progress_bar.progress(100)
                time.sleep(0.5)
                progress_bar.empty()
                status_text.empty()
                
                st.markdown("<h2 style='font-size: 24px; font-weight: 500; color: #424242; margin-bottom: 20px;'>Generated Emails</h2>", unsafe_allow_html=True)
                
                if not jobs or len(jobs) == 0:
                    st.warning("No job opportunities detected on the provided page. Please check the URL and try again.")
                
                for i, job in enumerate(jobs):
                    st.markdown(f"<div style='padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); margin-bottom: 20px; background-color: #FFFFFF;'>", unsafe_allow_html=True)
                    
                    role = job.get('role', 'Unknown Position')
                    st.markdown(f"<div style='font-size: 20px; font-weight: 600; color: #1E88E5; margin-bottom: 10px;'>Job #{i+1}: {role}</div>", unsafe_allow_html=True)
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"<div style='margin-bottom: 5px; color: #424242;'><b>Experience:</b> {job.get('experience', 'Not specified')}</div>", unsafe_allow_html=True)
                    with col2:
                        skills = job.get('skills', [])
                        skills_str = ", ".join(skills) if isinstance(skills, list) else skills
                        st.markdown(f"<div style='margin-bottom: 5px; color: #424242;'><b>Skills:</b> {skills_str or 'Not specified'}</div>", unsafe_allow_html=True)
                    
                    links = portfolio_instance.query_link(skills)
                    
                    email = chain_instance.write_mail(job, links)
                    
                    st.markdown("<div style='background-color: #f8f9fa; border-left: 4px solid #1E88E5; padding: 15px; border-radius: 5px; margin-top: 15px;'>", unsafe_allow_html=True)
                    st.markdown("### 📧 Generated Email")
                    st.code(email, language="markdown")
                    st.markdown("</div>", unsafe_allow_html=True)
                    
                    st.markdown("</div>", unsafe_allow_html=True)
                    
            except Exception as e:
                st.error(f"An Error Occurred: {e}")
                st.markdown("""
                <div style='background-color: #ffebee; padding: 15px; border-radius: 5px; border-left: 4px solid #f44336;'>
                    <h3 style='color: #d32f2f;'>Troubleshooting Tips:</h3>
                    <ul>
                        <li>Make sure the URL is complete (includes https://)</li>
                        <li>Check if the website allows web scraping</li>
                        <li>Try a direct link to the careers/jobs page</li>
                        <li>Verify your API keys and internet connection</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
    elif submit_button and not url_input:
        st.warning("Please enter a valid URL to proceed.")
    
    st.markdown("""
    <div style='position: fixed; bottom: 0; left: 0; right: 0; background-color: #f8f9fa; padding: 10px 20px; text-align: center; border-top: 1px solid #e0e0e0; font-size: 12px; color: #616161;'>
        Cold Email Generator | AI Powered Business Development Tool | © 2025
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()