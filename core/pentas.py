import pandas as pd
import numpy as np
import plot



class Pentas:
    
    def __init__(self, event_data = None, tracking_data = None,
                 home = 'Home', away = 'Away', event_map = {}, 
                 circle_colors = ('blue','red'), arrow_colors = ('blue','red'), 
                 field_color = ('green', 'white')):
        
        self.event_data = event_data
        self.tracking_data = tracking_data
        self.home = home
        self.away = away
        self.circle_colors = circle_colors
        self.arrow_colors = arrow_colors
        self.field_color = field_color
        self.em = event_map
        
        if event_map == {}:
            self.event_map = {'Team':'Team', 'Type':'Type', 'Period':'Period', 
                 'SFrame':'SFrame', 'EFrame':'EFrame', 'From':'From','STime':'STime',
                 'ETime':'ETime','To':'To', 'SX':'SX', 'EX':'EX', 'SY':'SY', 'EY':'EY'}
        
    def getEventData(self):
        return self.event_data

    
    def getTrackingData(self):        
        return self.event_data
    
    def plotPass(self, players, names=False, plot_players=False, time_range = None, frame_range = None, period = 0):
        
        self._plotEvent('PASS', players, names, plot_players, time_range, frame_range, period)
        
    def plotShot(self, players, names=False, plot_players=False, time_range = None, frame_range = None, period = 0):
        
        self._plotEvent('SHOT', players, names, plot_players, time_range, frame_range, period)
        
    def plotFaultReceived(self, players, names=False, plot_players=False, time_range = None, frame_range = None, period = 0):
        
        self._plotEvent('FAULT RECEIVED', players, names, plot_players, time_range, frame_range, period)
        
    
    def _plotEvent(self, event, players, names=False, plot_players=False, time_range = None, frame_range = None, period = 0):
        
        event_data_f = self.event_data[self.event_data[self.em['Type']] == event]
        
        if time_range is not None:
            event_data_f = self.event_data[
                self.event_data[(self.em['STime'] > time_range[0])
                                & (self.em['ETime'] <= time_range[1])]]
            
        elif frame_range is not None:
            event_data_f = self.event_data[
                self.event_data[(self.em['SFrame'] > frame_range[0])
                                & (self.em['EFrame'] <= frame_range[1])]]
            
        if period != 0:
            event_data_f = event_data_f[event_data_f[self.em['Period']] == period]
            
        event_data_f = event_data_f[event_data_f[self.em['From']].isin(players)]
        
        plot.plotEvents(event_data_f, self.tracking_data, self.em, names, plot_players)