import sys
import json
import numpy as np
import pandas as pd
sys.path.append('../')
from FCPython import createPitch
import matplotlib.pyplot as plt

pitchLengthX = 120
pitchWidthY = 80

def readMatchData(match_id):

    with open('../Statsbomb/data/events/'+str(match_id)+'.json') as f:
      data = json.load(f)

    df = pd.json_normalize(data, sep = "_").assign(match_id = match_id)

    return df, df['team_name'].unique()


def plotShots(df, team1_name, team2_name):

    shots = df.loc[df['type_name'] == 'Shot'].set_index('id')

    (fig,ax) = createPitch(pitchLengthX,pitchWidthY,'yards','gray')

    for i,shot in shots.iterrows():

        x = shot['location'][0]
        y = shot['location'][1]

        goal=shot['shot_outcome_name']=='Goal'
        team_name=shot['team_name']

        circleSize = 2
        #circleSize=np.sqrt(shot['shot_statsbomb_xg'])*12

        if (team_name == team1_name):
            if goal:
                shotCircle = plt.Circle((x,pitchWidthY-y),circleSize,color="red")
                plt.text((x+1),pitchWidthY-y+1,shot['player_name'])
            else:
                shotCircle = plt.Circle((x,pitchWidthY-y),circleSize,color="red")
                shotCircle.set_alpha(.2)
        elif (team_name==team2_name):
            if goal:
                shotCircle = plt.Circle((pitchLengthX-x,y),circleSize,color="blue")
                plt.text((pitchLengthX-x+1),y+1,shot['player_name'])
            else:
                shotCircle = plt.Circle((pitchLengthX-x,y),circleSize,color="blue")
                shotCircle.set_alpha(.2)

        ax.add_patch(shotCircle)

    plt.text(5,75,team2_name + ' shots')
    plt.text(80,75,team1_name + ' shots')

    plt.show()


def plotPlayerPasses(df, player_name):

    passes = df.loc[(df['type_name'] == 'Pass') & (df['player_name'] == player_name)].set_index('id')

    (fig,ax) = createPitch(pitchLengthX,pitchWidthY,'yards','gray')

    for i, p in passes.iterrows():

        x = p['location'][0]
        y = p['location'][1]

        passCircle = plt.Circle((x, pitchWidthY-y), 2, color='blue')
        passCircle.set_alpha(.2)

        ax.add_patch(passCircle)

        dx = p['pass_end_location'][0]-x
        dy = p['pass_end_location'][1]-y
        
        passArrow = plt.Arrow(x, pitchWidthY-y,dx,dy,width=3,color='blue')
        ax.add_patch(passArrow)

    plt.text(0, 80, player_name + ' passes')

    plt.show()

def main():

    match_id = 69301
    match_df, teams = readMatchData(match_id)
    plotShots(match_df, teams[0], teams[1])
    plotPlayerPasses(match_df, 'Sara Caroline Seger')