import pandas as pd
import time

def concat_data(gameList, infoList, platform): 
    
    gameList.df = pd.DataFrame(gameList)
    infoList.df = pd.DataFrame(infoList)

