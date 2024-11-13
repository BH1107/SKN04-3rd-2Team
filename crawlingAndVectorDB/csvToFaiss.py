import pandas as pd

from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS


def laptop_data_to_faiss(csv_read_path, faiss_save_path):

    data_csv=pd.read_csv(csv_read_path, encoding='utf-8')

    loader = CSVLoader(csv_read_path, encoding='utf-8')
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
        folder_path=faiss_save_path,
        index_name='faiss_index'
    )