import pandas as pd
import time
from datetime import datetime

def steam_concat(gameList, infoList, platform): 
    
    gameList_df = pd.DataFrame(gameList)
    infoList_df = pd.DataFrame(infoList)

    now = datetime.datetime.now().strftime('%y.%m.%d %H-%M-%S')

    concatList = pd.concat([gameList_df, infoList_df], axis=1, join='inner')
    concatList.to_csv('./backup/'+platform+'/'+now+'_backup'+'.csv', index=False, encoding='cp949')
    print("csv saved to ./backup/" + platform + '/')

    return concatList