import requests
from bs4 import BeautifulSoup
# 메이플스토리 리부트2 상위랭킹 크롤링
# 크롤링할 웹 페이지 URL
url = 'https://maplestory.nexon.com/N23Ranking/World/Total?w=1'

# 웹 페이지 내용을 가져옴
response = requests.get(url)

# HTTP 요청이 성공적으로 이루어졌는지 확인
if response.status_code == 200:
    # BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 원하는 테이블을 찾음
    table = soup.find('table', class_='rank_table')
    
    if table:
        # 테이블 헤더의 순서대로 <th> 태그와 셀 내용을 가져와서 합침
        headers = table.find('thead').find_all('th')
        header_texts = [header.get_text(strip=True) for header in headers]
        
        # 영역별로 나눠서 출력
        rank_area = header_texts[0]
        character_info_area = header_texts[1]
        level_area = header_texts[2]
        experience_area = header_texts[3]
        popularity_area = header_texts[4]
        guild_order_area = header_texts[5]
        
        print(f"순위: {rank_area}")
        print(f"캐릭터 정보: {character_info_area}")
        print(f"레벨: {level_area}")
        print(f"경험치: {experience_area}")
        print(f"인기도: {popularity_area}")
        print(f"길드: {guild_order_area}")
        
        # 나머지 행을 추출
        rows = table.find_all('tr')[1:]  # 첫 번째 행(헤더)을 제외한 나머지 행들
        
        for row in rows:
            # 각 행의 셀을 추출
            cells = row.find_all('td')
            cell_texts = [cell.get_text(strip=True) for cell in cells]
            
            # 영역별로 나눠서 출력
            rank_data = cell_texts[0]
            character_info_data = cell_texts[1]
            level_data = cell_texts[2]
            experience_data = cell_texts[3]
            popularity_data = cell_texts[4]
            guild_order_data = cell_texts[5]
            
            print(f"순위 데이터: {rank_data}")
            print(f"캐릭터 정보 데이터: {character_info_data}")
            print(f"레벨 데이터: {level_data}")
            print(f"경험치 데이터: {experience_data}")
            print(f"인기도 데이터: {popularity_data}")
            print(f"길드 데이터: {guild_order_data}")
    else:
        print("테이블을 찾을 수 없습니다.")
else:
    print("HTTP 요청이 실패했습니다.")
