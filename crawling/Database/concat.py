import pandas as pd
import time
import datetime

def concat_data(gameList, infoList, platform): 
    
    gameList_df = pd.DataFrame(gameList)
    infoList_df = pd.DataFrame(infoList)
    
    now = datetime.datetime.now()

    concatList = pd.concat([gameList_df, infoList_df], axis=1, join='inner')
    concatList.to_csv('/backup/'+now+'_backup'+'.csv', index=False)

    return concatList