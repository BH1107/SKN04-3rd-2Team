# 🤗 팀명 : 병헌이 구른다
 
### 🤭 팀원

<p align="center">
  <table>
    <tr>
      <td align="center">
        <img src="https://pbs.twimg.com/media/D07FPC9WwAYZ1k1.jpg" width="160" height="160"/><br>김정훈 [팀장]
      </td>
      <td align="center">
        <img src="https://upload3.inven.co.kr/upload/2020/04/15/bbs/i13843617916.jpg" width="160" height="160"/><br>김효은
      </td>
      <td align="center">
        <img src="https://i.namu.wiki/i/CFdrduUAhyuiXzPMZ-WKsUJtGCuWOvzYLcIAdrcjZ2D7x4q3W1TxkGIYmBKTohKEM1vUNtgeZtilVHwCe2q17g.webp" width="160" height="160"/><br>박병헌
      </td>
      <td align="center">
        <img src="https://opgg-static.akamaized.net/meta/images/profile_icons/profileIcon4895.jpg?image=e_upscale,q_auto:good,f_webp,w_auto&v=1729058249" width="160" height="160"/><br>오종수
      </td>
      <td align="center">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-N5LKksvNwRIUWWcxuqWD2s52XO84KSOtdg&s" width="160" height="160"/><br>이지수
      </td>
    </tr>
  </table>
</p>

### 💼 역할 분담

### 👨‍💻 김정훈
- **데이터 전처리**: 원본 데이터를 분석하고, 모델에 적합한 형태로 변환했습니다.
- **Retriever 구성**: FAISS 기반의 문서 검색기를 구성했습니다.
- **Prompt 작성**: 사용자의 질문에 대한 적절한 답변을 생성하기 위한 프롬프트를 설계했습니다.
- **Streamlit 페이지 구성 및 리드미 작성**: Streamlit을 활용한 웹 인터페이스 구현 및 프로젝트 리드미를 작성했습니다.

### 👨‍💻 박병헌
- **데이터 전처리**: 데이터를 정리하고, 분석에 필요한 형식으로 준비했습니다.
- **Retriever 구성**: 문서 검색을 위한 FAISS 기반 검색기를 구성했습니다.

### 👩‍💻 이지수
- **데이터 전처리**: 데이터 분석 및 클렌징 작업을 진행했습니다.
- **Retriever 구성**: FAISS로 데이터를 효과적으로 검색할 수 있도록 구현했습니다.
- **Prompt 작성**: 사용자의 질문에 적합한 응답을 도출하기 위한 프롬프트를 작성했습니다.

### 👨‍💻 오종수
- **Streamlit 페이지 구성**: 사용자와의 인터페이스 역할을 하는 웹 페이지를 구현했습니다.
- **리드미 작성**: 프로젝트 진행 방식, 각 구성 요소 설명 등을 포함한 리드미를 작성했습니다.

---

## 프로젝트 개요
**문제정의 : 할루시네이션 없는 컴퓨터 비교 챗봇을 만들고 싶다**
ChatGPT에게 노트북 추천을 요청하면 할루시네이션이 있는 내용을 계속 출력하여 사용자에게 필요한 정보를 제공 받지 못하는 점이 이 프로젝트의 주요 이슈였습니다.


이 프로젝트는 다나와 사이트에서 노트북 제품 정보를 **크롤링**하여, 사용자가 입력하는 질문에 대해 적절한 답변을 제공하는 **대화형 챗봇** 시스템을 구축하는 것입니다.
본 시스템은 **RAG(Retrieval-Augmented Generation)** 방법론을 기반으로 하여, 실시간으로 사용자가 원하는 제품 정보를 정확하게 제공할 수 있도록 설계되었습니다.

## Data

<p>
  <img src="Images/capture.png" alt="이미지 설명" width="200" height="30">
</p>
셀레니움을 통해 크롤링한 데이터를 브랜드별로 수집한 다음, 모든 데이터를 하나의 csv파일로 합쳤습니다.
<br>
<p>
  <img src="Images/faiss.png" alt="이미지 설명" width="500" height="100">
</p>
document 데이터 embedding

## Preprocess
수집한 데이터의 전처리 과정 정리

<p>
  <img src="Images/eda.png" alt="이미지 설명" width="1000" height="100">
</p>
document 페이지 컨텐츠 정제, 메타 데이터 추가

---



## 기술 스텍

| Data Modeling | Front-End |
|--------------------|---------------------|
| ![BeautifulSoup](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white) ![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) <img src="https://img.shields.io/badge/langchain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white"><img src="https://img.shields.io/badge/openai-412991?style=for-the-badge&logo=openai&logoColor=white">| ![streamlit](https://img.shields.io/badge/streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

## Prerequisites



cmd
```
pip install -r requirements.txt
```
---

<p>
  <img src="Images/env.png" alt="이미지 설명" width="1000" height="100">
</p>
.env 환경변수 파일 필요


## Usage

```cmd
streamilt run streamlit.py 
```

임베딩된 데이터는 data/db 파일아래 존재, 임베딩이 필요하다면
streamlit.py 에서 아래와 같은 코드의 주석을 제거하면 csv 파일을 임베딩 

```python
# laptop_data_to_faiss(csv_path, faiss_path)
```

## System Architecture

### 프로그램의 전체적인 구성 도표 삽입 및 설명

<p>
  <img src="Images/architecture.png" alt="이미지 설명" width="500" height="350">
</p>

저희 시스템은 Selenium을 통해 크롤링한 데이터를 FAISS(Vector DB)에 임베딩하여 벡터 기반 검색을 수행합니다.   
사용자가 Streamlit에 입력한 질문은 retriever와 체인 모델을 거쳐, 저희가 개발한 모델로 응답이 생성됩니다.   
최종 결과는 Streamlit을 통해 사용자에게 직관적으로 제공됩니다.  
 
---

## 수행 결과

<p>
  <img src="Images/gpt.png" alt="이미지 설명" width="500" height="350">
</p>
<p>사진 1</p>

<p>
  <img src="Images/hallusination_evidence.png" alt="이미지 설명" width="500" height="350">
</p>
<p>사진 2</p>

사진 1과 사진 2는 다른 모델에게 노트북 추천을 부탁했을 때 할루시네이션이 발생한 사례입니다.

<p>
  <img src="Images/our_model.png" alt="이미지 설명" width="500" height="350">
</p>

저희가 만든 모델은 노트북에 대한 질문에 대해 할루시네이션 없이 정확한 정보를 제공하는 것을 확인할 수 있습니다.

## 한 줄 소감


### 👨‍💻 김정훈
- LangChain을 활용한 작업은 정말 흥미로웠습니다. 다양한 기능들이 유기적으로 연결되어, 복잡한 자연어 처리 작업을 효율적으로 처리할 수 있는 강력한 도구라는 생각이 들었습니다. 특히, LLM을 활용한 파이프라인 구축과 데이터 연결 작업이 매우 직관적이고 유연하게 처리되어 작업의 생산성을 크게 높일 수 있었습니다.

### 👨‍💻 박병헌
- 처음에 데이터 처리가 완료되면 금방 끝날 것 같은 작업이라고 생각했지만, 생각보다 pormpt 작업이 어렵고 생각대로 답변이 나오지 않아 많은 시간이 소요되었다. 하지만 결국 결과를 볼 수 있었고, 좋은 경험이였다.

### 👩‍💻 이지수
- LLM에 관련된 주제의 프로젝트를 경험한 것이 색다른 느낌이 들었습니다.   
시간이 촉박하여 프로젝트를 완성도 있게 만들지 못한 점이 매우 아쉬웠습니다.

### 👨‍💻 오종수
- 새로운 도전 속에서 많은 것을 배우고 성장할 수 있었던 프로젝트였습니다