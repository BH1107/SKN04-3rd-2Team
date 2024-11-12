from langchain_openai import ChatOpenAI
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA


def retrieve_and_answer(fetch_k=20, k=1, lambda_mult=0.3, query=''):
    if query == '':
        query='UX5406SA-ABCDFSD 한글로 사양알려줘'

    db = FAISS.load_local(
        folder_path='./data/db',
        index_name='faiss_index',
        embeddings=OpenAIEmbeddings(model='text-embedding-3-small'),
        allow_dangerous_deserialization=True
    )

    retriever = db.as_retriever(
        search_type = 'mmr',
        search_kwargs={
            'fetch_k':fetch_k,
            'k': k,
            'lambda_mult': lambda_mult,
        }
    )

    return retriever