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


# 메이플 랭킹 데이터 크롤링
def mapleserch():
    print("메이플 캐릭터 검색 시작")
    TTS.speak("검색하실 캐릭터 이름을 말씀해주세요")
    data = stt.listen_and_recognize()
    try:
        check, rank, job, level = maple.get_character_info(data)
        if check:
            TTS.speak(f"{data}님 {level}레벨이고, 직업은 {job} 입니다.")
        else:
            TTS.speak(f"{data} 이름을 가진 캐릭터를 찾지 못했어요. 처음부터 다시 시작해주세요.")
    except:
        TTS.speak("죄송합니다. 오류가 발생했습니다. 처음부터 다시 시작해주세요.")