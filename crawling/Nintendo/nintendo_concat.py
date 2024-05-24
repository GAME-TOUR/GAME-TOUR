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


A = [{ 'tset': "test"}]
B = { 'dddd': "dddd"}
df = pd.DataFrame(A)
df.to_csv('./backup/nintendo'+'/'+'_backup'+'.csv', index=False)