# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 12:53:29 2022

@author: denis
"""
#https://www.youtube.com/watch?v=KJvJ20GP65o
# Hi Denis, please read about these different libraries and what they offer.
import pandas as pd
import numpy as np
import requests
pd.set_option('display.max_columns',15)

#This is the official api fantasy premier league have made. What is an API?
#(3 minutes of YouTube later) Well instead of searching for the information you want in a dataset e.g. FindAll, APIs are a predifned menu for you to chooses parts of data to save you time.

url = "https://fantasy.premierleague.com/api/bootstrap-static/"

#Using this .get function from the requests library.
r = requests.get(url)

#transfrom requests in json object. Whats is json? Not sure man.
json = r.json()

#see how the data is stored in the API.
json.keys()
 
#build a dataframe using a pandas function.#view by using elementsdf.columns
elementsdf = pd.DataFrame(json['elements'])

#but we don't need all of this data so let's reduce this and pick the data we want. Use red_elementsdf.head() to get the first5 and check.
red_elementsdf = elementsdf [['element_type','team','id','web_name','form','value_form','now_cost','selected_by_percent','total_points','points_per_game']]


#map team to position names e.g. 4 = Forward
red_elementsdf['element_type'] = red_elementsdf['element_type'].map({4:'Forward',3:'Midfield',2:'Defence',1:'Goalkeeper'})

#have to assign the number columns as numeric otherwise it counts 10 as 1 or something.
red_elementsdf[['form','value_form','now_cost','selected_by_percent','total_points','points_per_game']] = red_elementsdf[['form','value_form','now_cost','selected_by_percent','total_points','points_per_game']].apply(pd.to_numeric)

#Sorted Tables
inform = red_elementsdf.sort_values(by = ['form'],ascending = False)
valinform = red_elementsdf.sort_values(by = ['value_form'],ascending = False)
picked = red_elementsdf.sort_values(by = ['selected_by_percent'],ascending = False)
#use e.g. inform.head(10) to get top 10.


#Trying to get a team out
#form_team_gk = inform[(inform.element_type == 'Goalkeeper')].head(1)
#form_team_df = inform[(inform.element_type == 'Defence')].head(5)
#form_team_md = inform[(inform.element_type == 'Midfield')].head(5)
#form_team_fw = inform[(inform.element_type == 'Forward')].head(3)
#topteam = pd.concat([form_team_gk,form_team_df,form_team_md,form_team_fw])

#Succeeding define one of the sorted tables e.g. inform, valinform or picked to get a squad out.
def formteam(sortby):
        
    form_team_gk = sortby[(sortby.element_type == 'Goalkeeper')].head(2)
    form_team_df = sortby[(sortby.element_type == 'Defence')].head(5)
    form_team_md = sortby[(sortby.element_type == 'Midfield')].head(5)
    form_team_fw = sortby[(sortby.element_type == 'Forward')].head(3)
    theteam = pd.concat([form_team_gk,form_team_df,form_team_md,form_team_fw])
    return theteam



if __name__ == '__formteam__':
    formteam()