import pandas as pd
import time
from datetime import datetime

def steam_data(gameList, infoList, platform): 
    
    gameList_df = pd.DataFrame(gameList)
    infoList_df = pd.DataFrame(infoList)

    concatList = pd.concat([gameList_df, infoList_df], axis=1, join='inner')
    print(concatList)
    concatList.to_csv(platform+'/backup'+'_backup'+'.csv', index=False)

    return concatList
  
GL = {}
IL = {}

steam_data(GL, IL, "STEAM") 