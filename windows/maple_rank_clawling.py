import requests
from bs4 import BeautifulSoup

def get_info(nick : str):
    nickname = nick
    url = f"https://maplestory.nexon.com/N23Ranking/World/Total?c={nickname}&w=0"
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
            
            # 나머지 행을 추출
            rows = table.find_all('tr')[1:]  # 첫 번째 행(헤더)을 제외한 나머지 행들
            
            for row in rows:
                # 각 행의 셀을 추출
                cells = row.find_all('td')
                cell_texts = [cell.get_text(strip=True) for cell in cells]
                
                rank_data = cell_texts[0]
                character_info_data = cell_texts[1]
                level_data = cell_texts[2]

                if nickname in character_info_data:
                    rank_data = rank_data.split('-')[0]
                    character_info_data = character_info_data.split('/')[-1].strip()
                    level_data = level_data.split('.')[-1]
                    return True, rank_data, character_info_data, level_data

        else:
            return False, None, None, None
    else:
        return False, None, None, None

print(get_info("해줘돈줘"))