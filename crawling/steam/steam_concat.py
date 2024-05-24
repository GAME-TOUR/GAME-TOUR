import pandas as pd
import time
from datetime import datetime

def steam_concat(gameList, infoList, platform): 
    
    gameList_df = pd.DataFrame(gameList)
    infoList_df = pd.DataFrame(infoList)

    now = datetime.now().strftime('%y.%m.%d %H-%M-%S')

    concatList = pd.concat([gameList_df, infoList_df], axis=1, join='inner')
    print(concatList)
    # concatList.to_csv('./backup/'+platform+'/'+now+'_backup'+'.csv', index=False, encoding='cp949')
    # print("csv saved to ./backup/" + platform + '/')

    return concatList

# test code 
# A = {'title': 'Lorelei and the Laser Eyes', 'url': 'https://store.nintendo.co.kr/70010000054301'}
# B = {'title': 'Lorelei and the Laser Eyes', 'date': '2024.04.21', 'company': 'Annapurna Interactive', 'tag': '어드벤쳐, 퍼즐', 'platform': 'nintendo'}
# A_Li = [A]
# B_LI = [B]
# A_DF = pd.DataFrame(A_Li)
# B_DF = pd.DataFrame(B_LI)

# CLi = pd.concat([A_DF, B_DF], axis=1, join='inner')
# print(CLi)

# steam_concat(A_Li, B_LI, "nintendo")