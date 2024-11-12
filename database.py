from dotenv import load_dotenv
import pandas as pd

from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

data_csv=pd.read_csv(r'C:\Users\USER\Desktop\MyCode_BH\SkAiCampMyData\3rdproject\laptops_data.csv', encoding='utf-8')

loader = CSVLoader(r'C:\Users\USER\Desktop\MyCode_BH\SkAiCampMyData\3rdproject\laptops_data.csv', encoding='utf-8')
documents = loader.load()

for i, document in enumerate(documents):
    document.page_content = document.page_content.replace('\ufeffname:', '').replace('\n','').replace('content:','')
    document.metadata.update({'source': data_csv.name.iloc[i]})
    document.metadata.update({'price': data_csv.price.iloc[i]})

db = FAISS.from_documents(
    documents=documents,
    embedding=OpenAIEmbeddings(model='text-embedding-3-small')
)

db.save_local(
    folder_path='./data/db',
    index_name='faiss_index'
)
