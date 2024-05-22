import pandas as pd
import time
from datetime import datetime

def xbox_concat(gameList, infoList, platform): 
    
    gameList_df = pd.DataFrame(gameList)
    infoList_df = pd.DataFrame(infoList)

    concatList = pd.concat([gameList_df, infoList_df], axis=1, join='inner')
    
    print(concatList)
    
    now = datetime.now().strftime('%y.%m.%d %H-%M-%S')
    concatList.to_csv('./backup/'+platform+'/'+now+'_backup'+'.csv', index=False, encoding='UTF-16')

    return concatList