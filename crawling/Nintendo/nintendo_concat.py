import pandas as pd
import time
from datetime import datetime

def nintendo_concat(gameList, infoList, platform): 
    
    gameList_df = pd.DataFrame(gameList)
    infoList_df = pd.DataFrame(infoList)

    concatList = pd.concat([gameList_df, infoList_df], axis=1, join='inner')
    
    now = datetime.now().strftime('%y.%m.%d %H-%M-%S')
    concatList.to_csv('./backup/'+platform+'/'+now+'_backup'+'.csv', index=False)

    return concatList

# test code
# --------------------------------------------------------------------------------------------------------------------
# A = {
#     'title': "스텔라리스",
#     'url': "https://store.steampowered.com/app/281990/Stellaris/",
#     'date': "2016년 5월 10일"
# }
# ALi = list()
# ALi.append(A)

# tagLi = ['Space', 'Grand Strategy']
# titleLi = ['스텔라리스', 'Stellaris']
# B = {
#     'tag': ",".join(tagLi),
#     'KOR-ENG': ",".join(titleLi),
#     'description': "항성간 여행을 통해ー우주-를 탐험하며 수많은 종족들도 만나보세요. 과학선을 보내 우주를 조사하고 탐험하면서 은하 제국을 건설하고, 건축선을 보내 새로 발견한 행성에 기지를 건설하세요. 소속 사회를 위한 탐험에 나서 매장된 보물과 은하계의 경이를 발견하고, 탐험가의 한계치와 진화 범위를 설정하세요",
#     'company': "Paradox Development Studio",
#     'publisher': "Paradox Interactive",
#     'platform': "steam"
# }
# BLi = list()
# BLi.append(B)

# nintendo_concat(ALi, BLi, 'nintendo')