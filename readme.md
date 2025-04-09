# Cold Email Generator

<div align="center">
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/streamlit-1.20+-red.svg" alt="Streamlit 1.20+">
  <img src="https://img.shields.io/badge/langchain-0.1.0+-green.svg" alt="LangChain 0.1.0+">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT">
</div>

<p align="center">
  <strong>AI-powered application that automates cold email outreach for business development by analyzing company career pages.</strong>
</p>

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Technical Architecture](#technical-architecture)
- [Installation](#installation)
- [Usage Guide](#usage-guide)
- [Demo](#demo)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [API Dependencies](#api-dependencies)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## 🔍 Overview

The Cold Email Generator is a sophisticated AI-driven tool designed for business development executives to streamline the process of creating personalized outreach emails. By leveraging large language models and advanced text extraction techniques, this application:

1. Scrapes company career pages to identify potential business opportunities
2. Extracts detailed job listings and requirements
3. Analyzes the skills and experience needed for each position
4. Generates highly personalized cold emails that match your company's portfolio with the prospect's needs
5. Provides a clean, user-friendly interface to manage the entire process

This tool significantly reduces the time and effort required for researching prospects and drafting personalized outreach emails, allowing business development teams to focus on relationship building and closing deals.

## ✨ Key Features

### 🔄 Automated Job Extraction
- **Web Scraping Integration**: Seamlessly extracts content from company career pages
- **AI-Powered Analysis**: Uses Groq's LLama 3.3 70B model to identify and parse job listings
- **Structured Data Processing**: Converts unstructured web content into organized job information

### 📝 Intelligent Email Generation
- **Personalized Content**: Creates customized emails addressing specific job requirements
- **Portfolio Matching**: Automatically includes relevant portfolio links based on required skills
- **Professional Tone**: Maintains a business-appropriate tone with compelling value propositions

### 🔎 Portfolio Management
- **Vector Database Integration**: Utilizes ChromaDB for efficient portfolio searching
- **Semantic Matching**: Finds the most relevant portfolio items based on semantic similarity
- **Easy Portfolio Maintenance**: Simple CSV-based portfolio management

### 🖥️ User Experience
- **Clean Interface**: Modern, intuitive Streamlit interface with responsive design
- **Real-time Processing**: Visual feedback during the generation process
- **Easy Customization**: Generated emails can be easily copied and further customized

## 🏗️ Technical Architecture

The application is built on a modern tech stack with several key components:

1. **Frontend**: Streamlit web application with custom CSS styling for enhanced user experience
2. **Job Extraction Engine**: LangChain + Groq integration with custom prompt templates
3. **Vector Database**: ChromaDB for efficient portfolio searching and matching
4. **Email Generation System**: Template-based generation with AI-powered customization
5. **Utility Layer**: Text cleaning and processing utilities

### Data Flow

```
User Input (URL) → Web Scraping → Text Cleaning → LLM Processing → 
Job Extraction → Portfolio Matching → Email Generation → User Interface
```

## 🚀 Installation

### Prerequisites
- Python 3.8+
- Groq API key
- Internet connection for web scraping and API access

### Step-by-Step Setup

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/cold-email-generator.git
cd cold-email-generator
```

2. **Create and activate a virtual environment** (optional but recommended):
```bash
python -m venv env
source env/bin/activate  # On Windows, use: env\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**:
- Copy `.env.sample` to `.env`
- Add your Groq API key to the `.env` file:
```
GROQ_API_KEY=your_groq_api_key_here
```

5. **Prepare your portfolio data**:
- Copy `my_portfolio.csv.sample` to `my_portfolio.csv`
- Fill in your actual portfolio data following the sample format

## 📘 Usage Guide

### Basic Usage

1. **Start the application**:
```bash
streamlit run main.py
```

2. **Navigate to the application** (typically http://localhost:8501)

3. **Enter a career page URL** in the provided input field

4. **Click "Generate Emails"** to start the process

5. **Review the generated emails** for each identified job opportunity

6. **Copy and customize** the emails as needed for your outreach

### Best Practices

- Use direct links to career/jobs pages rather than company homepages
- Ensure your portfolio CSV includes comprehensive tech stack descriptions
- Review and personalize the generated emails before sending
- Update your portfolio regularly with new projects and capabilities

## 🎬 Demo

![Application Demo](demo_screenshot.png)

*Add a screenshot or GIF of your application in action here*

## 📁 Project Structure

```
cold-email-generator/
├── main.py               # Streamlit application and UI components
├── chains.py             # LLM chain implementation for extraction and generation
├── portfolio.py          # Portfolio management and vector search
├── utils.py              # Text cleaning and utility functions
├── requirements.txt      # Project dependencies
├── .env.sample           # Sample environment variables file
├── my_portfolio.csv.sample  # Sample portfolio data structure
├── .gitignore            # Git ignore rules
└── README.md             # Project documentation
```

## ⚙️ Configuration

### Environment Variables

- `GROQ_API_KEY`: Your Groq API key for accessing their LLM services
- `PORTFOLIO_FILE`: (Optional) Custom path to your portfolio CSV file

### Portfolio Configuration

The `my_portfolio.csv` file should contain the following columns:
- `Techstack`: Comma-separated list of technologies, skills, or capabilities
- `Links`: Comma-separated list of portfolio links showcasing these capabilities

## 🔌 API Dependencies

- **Groq API**: Used for AI-powered text processing and generation
- **ChromaDB**: Vector database for semantic searching of portfolio items
- **Streamlit**: Web application framework
- **LangChain**: Framework for LLM application development

## 🌐 Deployment

### Local Deployment
Follow the installation instructions above to run locally.

### Cloud Deployment

#### Streamlit Cloud
1. Push your code to GitHub
2. Create a new app on Streamlit Cloud pointing to your repository
3. Add your secrets (API keys) in the Streamlit Cloud dashboard
4. Deploy the application

#### Alternative Platforms
The application can also be deployed on:
- Heroku
- AWS
- Azure
- Google Cloud

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

<p align="center">
  Developed with ❤️ by [Your Name/Company]
</p>