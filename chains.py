import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv
load_dotenv()


class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile", 
            temperature=0, 
            groq_api_key=os.getenv("GROQ_API_KEY")
        )

    def extract_jobs(self, cleaned_text):
        # The key issue is likely here - we need to use keyword arguments for template_format
        # Let's make this compatible with both Pydantic v1 and v2
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke({"page_data": cleaned_text})
        
        try:
            json_parser = JsonOutputParser()  # Fixed typo: josn_parser -> json_parser
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Content too big. Unable to parse jobs")
            
        return res if isinstance(res, list) else [res]
    
    def write_mail(self, job, links):
        # Same issue here - let's use from_template
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are Chaitanya, a business development executive at ABC. ABC is an AI & Software Consulting company dedicated to facilitating
            the seamless integration of business processes through automated tools. 
            Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability, 
            process optimization, cost reduction, and heightened overall efficiency. 
            Your job is to write a cold email to the client regarding the job mentioned above describing the capability of ABC 
            in fulfilling their needs.
            Also add the most relevant ones from the following links to showcase ABC's portfolio: {link_list}
            Remember you are Mohan, BDE at ABC. 
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):
            """
        )
        
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        
        return res.content
    
if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))