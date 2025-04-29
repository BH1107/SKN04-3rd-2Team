# 🤗 Team Name : BH is working
 
### 🤭 팀원

<p align="center">
  <table>
    <tr>
      <td align="center">
        <img src="https://pbs.twimg.com/media/D07FPC9WwAYZ1k1.jpg" width="160" height="160"/><br>김정훈 Kim Jeong Hun[Team Leader]
      </td>
      <td align="center">
        <img src="https://upload3.inven.co.kr/upload/2020/04/15/bbs/i13843617916.jpg" width="160" height="160"/><br>김효은 Kim Hyo Eun
      </td>
      <td align="center">
        <img src="https://i.namu.wiki/i/CFdrduUAhyuiXzPMZ-WKsUJtGCuWOvzYLcIAdrcjZ2D7x4q3W1TxkGIYmBKTohKEM1vUNtgeZtilVHwCe2q17g.webp" width="160" height="160"/><br>박병헌 Park Byung Hun
      </td>
      <td align="center">
        <img src="https://opgg-static.akamaized.net/meta/images/profile_icons/profileIcon4895.jpg?image=e_upscale,q_auto:good,f_webp,w_auto&v=1729058249" width="160" height="160"/><br>오종수 Oh Jong Su
      </td>
      <td align="center">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-N5LKksvNwRIUWWcxuqWD2s52XO84KSOtdg&s" width="160" height="160"/><br>이지수 Lee Ji Su
      </td>
    </tr>
  </table>
</p>

### 💼 역할 분담

### 👨‍💻 김정훈 Kim Jeong Hun
- **Data Preprocessing**: Data Preprocessing: Analyzed raw data and transformed it into a suitable format for modeling.
- **Retriever Setup**: Built a FAISS-based document retriever.
- **Prompt Engineering**: Designed prompts to generate appropriate answers to user queries.
- **Streamlit UI & README**: Developed the web interface using Streamlit and wrote the project’s README.

### 👨‍💻 박병헌 Park Byung Hun
- **Data Preprocessing**: Cleaned and prepared data for analysis.
- **Retriever Setup**: Implemented FAISS-based search functionality for document retrieval.

### 👩‍💻 이지수 Lee Ji Su
- **데이터 전처리**: Conducted data analysis and cleansing.
- **Retriever Setup**: Built an efficient FAISS-based document search system.
- **Prompt 작성**: Created prompts to generate accurate responses to user input.

### 👨‍💻 오종수 Oh Jong Su
- **Streamlit UI**: Developed the front-end interface using Streamlit.
- **README Writing**: Documented the project structure and components in the README.

---

## Project Overview
**Problem Definition : We wanted to build a hallucination-free laptop recommendation chatbot.**
When users asked ChatGPT for laptop recommendations, it often returned hallucinated information that was not based on real data. This made it hard for users to get accurate product insights.


Our solution was to **crawl real product data from Danawa (a Korean e-commerce site)** and build an interactive **chatbot** that could provide reliable answers based on factual data.
The system is built on the **RAG (Retrieval-Augmented Generation)** architecture to ensure that users receive up-to-date and accurate information in real time.

## Data

<p>
  <img src="Images/capture.png" alt="이미지 설명" width="200" height="30">
</p>
We used Selenium to crawl laptop data by brand and then merged all the collected data into a single CSV file.
<br>
<p>
  <img src="Images/faiss.png" alt="이미지 설명" width="500" height="100">
</p>
The document data was embedded and indexed using FAISS for efficient retrieval.

## Preprocess

<p>
  <img src="Images/eda.png" alt="이미지 설명" width="1000" height="100">
</p>
We cleaned and structured the document content, added metadata, and prepared it for embedding.

---



## Tech Stack

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
Make sure to create a .env file for environment variables.


## Usage

```cmd
streamilt run streamlit.py 
```

Embedded data is stored under the data/db directory.
To re-embed the CSV file, uncomment the following line in streamlit.py:

```python
# laptop_data_to_faiss(csv_path, faiss_path)
```

## System Architecture

<p>
  <img src="Images/architecture.png" alt="이미지 설명" width="500" height="350">
</p>

Our system crawls data using Selenium, embeds it with FAISS (Vector DB), and enables vector-based document retrieval.
User input on Streamlit is passed through a retriever and a chain model, then processed by our customized LLM pipeline to generate final responses—delivered directly through the UI.
 
---

## Results

<p>
  <img src="Images/gpt.png" alt="이미지 설명" width="500" height="350">
</p>
<p>Images 1</p>

<p>
  <img src="Images/hallusination_evidence.png" alt="이미지 설명" width="500" height="350">
</p>
<p>Images 2</p>

Images 1 and 2 show examples of hallucinated answers given by other models when asked for laptop recommendations.

<p>
  <img src="Images/our_model.png" alt="이미지 설명" width="500" height="350">
</p>

Our model successfully returns factual and accurate answers to laptop-related questions.

## Final Thoughts


### 👨‍💻 김정훈 Kim Jeong Hun
- Using LangChain was truly interesting. It’s a powerful tool that allowed us to seamlessly integrate various LLM components. The pipeline design was intuitive and significantly boosted productivity.

### 👨‍💻 박병헌 Park Byung Hun
- Initially, I thought the project would be easy once the data was prepared. But prompt tuning was unexpectedly challenging and took a lot of time. Still, it was a rewarding experience.

### 👩‍💻 이지수 Lee Ji Su
- It was a refreshing experience to work on a project related to LLMs. It's unfortunate that we had limited time to polish the final product.

### 👨‍💻 오종수 Oh Jong Su
- I learned and grew a lot during this project through new challenges.