from streamlit import *

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from dotenv import load_dotenv
import pandas as pd

from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
import pandas as pd
import os
from langchain.llms import OpenAI
from langchain_openai import ChatOpenAI
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

from dotenv import load_dotenv
from operator import itemgetter
from langchain_openai import ChatOpenAI
from langchain_core.prompts import (
    PromptTemplate,
)
from langchain_core.output_parsers import (
    StrOutputParser,
)
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_transformers import LongContextReorder

def notebook_web_crawl(last_page_num=10):
    # Selenium WebDriver 초기화
    laptops = []
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))    # 4버전 이상
    driver.get("https://prod.danawa.com/list/?cate=11229515&15main_11_02=")
    # 페이지 순회 크롤링
    for page in range(1, last_page_num+1):  # 예시로 1~10페이지까지 순회
        try:
            # JavaScript 함수 호출하여 페이지 이동
            driver.execute_script(f"movePage({page});")
            
            # 페이지 로딩 시간 대기
            time.sleep(2)
            
            # 필요한 데이터 추출
            products = driver.find_elements(By.CSS_SELECTOR, "div.prod_main_info")
            for product in products:
                name = product.find_element(By.CSS_SELECTOR, "div.prod_info p.prod_name a").text.strip()
                content = product.find_element(By.CSS_SELECTOR, "div.prod_info div.spec_list").text.strip()
                try:
                    price = product.find_element(By.CSS_SELECTOR, "div.prod_pricelist span.text__number").text.strip()
                except:
                    try:
                        price = product.find_element(By.CSS_SELECTOR, "div.prod_pricelist ul li p.price_sect a strong").text.strip()
                    except:
                        price = "No"  # 가격 정보가 없을 때 'No'로 표시                
                laptops.append({'name': name, 'content': content, 'price': price})
        except Exception as e:
            print(f"Error on page {page}: {e}")
            break

    # 크롤링 완료 후 드라이버 종료
    driver.quit()

    # laptops = list(set(laptops))

    return laptops

def data_to_csv(laptops: pd.DataFrame):
    df = pd.DataFrame(laptops)

    # 데이터프레임을 CSV 파일로 저장
    df.to_csv("laptops_data.csv", index=False)

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

    

def prompting(retriever, question=''):
    if question == '':
        question = 'MSI노트북 두개의 노트북 비교해서 그 중 하나를 추천해줘'

    template = ''' 
    너는 노트북 사양을 분석해서 알려주는 봇이다.
    노트북에 관한 정보를 물어볼 때, 대답은 한글로 명확하고 자세히 알려줘.

    질문: {question}

    내용: {reference}

    언어: {language}
    '''

    prompt = PromptTemplate(
        template=template,
        input_variables=['question', 'reference', 'language'],
    )
    model = ChatOpenAI(model='gpt-4o-mini')
    parser = StrOutputParser()
    chain = (
        {
            'reference': itemgetter('question') | retriever,
            'question': itemgetter('question'),
            'language': itemgetter('language'),
        }
        | prompt
        | model
        | parser
    )

    # chain을 통해 question
    reference = chain.invoke(
        {
            'question': f'{question}',
            'language': '한국어',
        }
    )
    print(reference)

load_dotenv()

# laptops = notebook_web_crawl()
# data_to_csv(laptops)


csv_read_path = os.getenv("csv_read_path")
faiss_save_path = os.getenv("faiss_save_path")
laptop_data_to_faiss(csv_read_path,faiss_save_path)
retriever = retrieve_and_answer()
prompting(retriever)