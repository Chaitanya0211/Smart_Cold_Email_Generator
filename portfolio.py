import pandas as pd
import chromadb
import uuid

# Renamed class to follow Python naming convention (CamelCase for classes)
class Portfolio:
    def __init__(self, file_path="my_portfolio.csv"):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.chroma_client = chromadb.PersistentClient('vectorestore')
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")
    
    def load_portfolio(self):
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(
                    documents=[row["Techstack"]],  # Fixed: needs to be a list
                    metadatas=[{"links": row["Links"]}],  # Fixed: needs to be a list of dicts
                    ids=[str(uuid.uuid4())]
                )
    
    def query_link(self, skills):
        if not skills:
            return []
        # Convert skills to a list if it's not already
        if isinstance(skills, str):
            skills = [skills]
        # Make sure we have at least one skill to query
        if not skills:
            return []
        # Query the collection
        results = self.collection.query(query_texts=skills, n_results=2)
        # Extract and return the links
        metadatas = results.get('metadatas', [])
        if metadatas and isinstance(metadatas, list) and len(metadatas) > 0:
            return [item.get('links', '') for sublist in metadatas for item in sublist]
        return []

# For backward compatibility
portfolio = Portfolio