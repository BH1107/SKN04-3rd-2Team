import streamlit as st
import openai
import toml

data = toml.load("./config.toml")

# OpenAI API 키 설정
openai.api_key = data["API"]["key"]

# 모델 설정
MODEL = "gpt-4o-mini"  # 사용하려는 모델 (gpt-3.5-turbo 또는 gpt-4)

# 대화 기록을 저장할 리스트
if 'conversation' not in st.session_state:
    st.session_state['conversation'] = []  # 빈 리스트로 초기화

# 사용자 입력 초기화
if 'user_input' not in st.session_state:
    st.session_state['user_input'] = ""  # 빈 문자열로 초기화

# OpenAI API 호출 함수
def chat_with_gpt(messages):
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=messages
    )
    return response['choices'][0]['message']['content']

# Streamlit 앱 디자인 설정
st.set_page_config(page_title="ChatGPT와 대화하기", page_icon="🤖", layout="wide")

# 페이지 헤더와 소개 텍스트
st.markdown("""
    <style>
        .header {
            font-size: 36px;
            font-weight: bold;
            color: #4CAF50;
            text-align: center;
        }
        .message {
            font-size: 16px;
            padding: 10px;
            border-radius: 15px;
            margin: 10px 0;
        }
        .user {
            background-color: #DCF8C6;
            color: #000;
            text-align: left;
        }
        .assistant {
            background-color: #f1f0f0;
            color: #000;
            text-align: right;
        }
    </style>
    <div class="header">ChatGPT와 대화하기 🤖</div>
""", unsafe_allow_html=True)

# 사용자 입력 받기
user_input = st.text_area("여기서 메시지를 입력하세요:", height=100, value=st.session_state['user_input'], placeholder="ChatGPT에게 질문을 해보세요...", label_visibility="collapsed")

# 'Send' 버튼 스타일 적용
send_button = st.button("Send", use_container_width=True)

# 버튼 클릭 시 처리
if send_button and user_input:
    # 사용자 메시지 추가
    st.session_state['conversation'].append({"role": "user", "content": user_input})
    
    # ChatGPT의 응답 생성
    response = chat_with_gpt(st.session_state['conversation'])
    
    # 응답 메시지 추가
    st.session_state['conversation'].append({"role": "assistant", "content": response})
    
    # 입력창 비우기 (세션 상태 업데이트)
    st.session_state['user_input'] = ""

# 대화 출력
for msg in st.session_state['conversation']:
    if msg['role'] == 'user':
        st.markdown(f'<div class="message user">{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="message assistant">{msg["content"]}</div>', unsafe_allow_html=True)
