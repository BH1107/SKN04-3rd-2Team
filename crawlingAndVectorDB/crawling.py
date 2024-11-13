import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


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

    return laptops


def data_to_csv(laptops: pd.DataFrame):
    df = pd.DataFrame(laptops)

    # 데이터프레임을 CSV 파일로 저장
    df.to_csv("laptops_data.csv", index=False)