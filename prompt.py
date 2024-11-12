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
prompting()