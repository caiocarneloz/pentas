import sys
sys.path.append('../')
import pandas as pd
from core.pentas import Pentas
    
events = pd.read_csv('../../../DATA/Metricasports/data/Sample_Game_1/Sample_Game_1_RawEventsData.csv')

print(events.columns)

event_map = {'Team':'Team', 'Type':'Type', 'Period':'Period', 
                 'SFrame':'Start Frame', 'EFrame':'End Frame', 
                 'STime':'Start Time [s]', 'ETime':'End Time [s]',
                 'From':'From','To':'To', 'SX':'Start X', 'EX':'End X', 'SY':'Start Y', 'EY':'End Y'}


pn = Pentas(event_data=events, event_map=event_map)


pn.event_data['Subtype'].unique()

pn.plotPass(['Player10', 'Player9', 'Player11'], period = 1)