import requests
from bs4 import BeautifulSoup

def extract_data_from_table(table, nickname):
    rows = table.find_all('tr')[1:]  # 첫 번째 행(헤더)을 제외한 나머지 행들
    for row in rows:
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
    return False, None, None, None

def get_character_info(nickname: str):
    urls = [
        f"https://maplestory.nexon.com/N23Ranking/World/Total?c={nickname}&w=0",
        f"https://maplestory.nexon.com/N23Ranking/World/Total?c={nickname}&w=1"
    ]

    for url in urls:
        response = requests.get(url)
        
        # Check if HTTP request is successful
        if response.status_code != 200:
            print("Request failed")
            return False, None, None, None
        
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', class_='rank_table')
        
        if table:
            found, rank, char_info, level = extract_data_from_table(table, nickname)
            if found:
                return found, rank, char_info, level
        else:
            print("Table extraction failed")
    
    return False, None, None, None