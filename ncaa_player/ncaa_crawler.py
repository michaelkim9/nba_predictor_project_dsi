import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re


#class ncaa_crawler(object):

def __init__(self):
	self
	
def SoupFromURL(url, suppressOutput=True):

    if not suppressOutput:
        print(url)
    try:
        r = requests.get(url)
    except:
        return None

    return BeautifulSoup(r.text, "html5lib")

def remove_values_from_list(the_list, val):
    return [value for value in the_list if value != val]



def ncaa_stats_dict(url):
    player_page = SoupFromURL(str(url))
    
    #player profile info
    a = player_page.find_all('div', attrs={'class':'nothumb'})[0]
    a_soup = BeautifulSoup(str(a),"html5lib")
    n = a_soup.text.split('\n')
    n = remove_values_from_list(n,'')
    n = remove_values_from_list(n,'  ')
    removal = ['(','  Hometown','  High School', '  More','  Position']
    for remove in removal:
        n = [x for x in n if not x.startswith(remove)]

    try:
        name = n[0]
        name = name.replace('\t','')
    except:
        name = None

    try:
        position = n[2]
        position = position.replace('  ','')
    except:
        position=None
    
    try:
        college = n[4]
        college = college.replace('  School: ','')
    except:
        college = None
    
    try:
        ft = n[3][:3]
        ft = int(ft.replace(' ',''))*12
        inch = n[3][3:6]
        inch = int(re.sub('[^0-9]','',inch))
        height = ft + inch
    except:
        height = None
    
    try:
        weight = n[3][7:11]
        weight = int(re.sub('[^0-9]','',weight))
    except:
        weight=None
    
    #player stats
    stat_list = []
    try:
        p = player_page.find_all('div', attrs={'class':'stats_pullout'})[0]
        p_soup = BeautifulSoup(str(p),"html5lib")
        stat = p_soup.text.split('\n')[1::4][2:]
    
        #stat_list = []
        for s in stat:
            try:
                if s == str(""):
                    stat_list.append(None)
                else:
                    stat_list.append(float(s))
            except:
                stat_list.append(None)
    except:
        stat_list.extend([None,None,None,None,None,None,None,None,None,None])
    
    #season count and draft year
    season_count = player_page.find_all('div', attrs={'class':'overthrow table_container'})[0]
    season_count_soup = BeautifulSoup(str(season_count),"html5lib")
    season_count = season_count_soup.text.split('\n')
    season_count = season_count[20:37]
    season_count = [x for x in season_count if not 'Career' in x]
    season_count = [x for x in season_count if not '  ' in x]
    final_season_count = len(list(filter(None, season_count)))
    
    draft_year_list = list(filter(None, season_count))
    if len(draft_year_list) == 4:
        final_year = str(draft_year_list[3])[5:7]
    elif len(draft_year_list) == 3:
        final_year = str(draft_year_list[2])[5:7]
    elif len(draft_year_list) == 2:
        final_year = str(draft_year_list[1])[5:7]
    elif len(draft_year_list) == 1:
        final_year = str(draft_year_list[0])[5:7]

    if int(final_year[0]) in [0,1]:
        final_draft_year = int(final_year) + 2000
    elif int(final_year[0]) in [9,8,7,6,5,4,3,2]:
        final_draft_year = int(final_year) + 1900
    
    #steals, rebounds, turnovers and mins played per game
    additional_stats = player_page.find_all('td', attrs={'class':'right'})
    additional_soup = BeautifulSoup(str(additional_stats),"html5lib")
    try:
        steal_stat = additional_soup.text.split(',')[-5]
        steals = float(steal_stat)
    except:
        steals = None
    
    try:
        block_stat = additional_soup.text.split(',')[-4]
        blocks = float(block_stat)
    except:
        blocks = None
    
    try:
        turnover_stat = additional_soup.text.split(',')[-3]
        turnovers = float(turnover_stat)
    except:
        turnovers = None
        
    try:
        minutes_stat = additional_soup.text.split(',')[-20]
        minutes = float(minutes_stat)
    except:
        minutes=None
    
    #creating player dictionary
    player_dict = {
        'player_name':name,
        'position':position,
        'height_inches':height,
        'weight_lbs':weight,
        'college':college,
        'draft_year':final_draft_year,
        'years_in_college':final_season_count,
        'games':stat_list[0],
        'minutes_per_game':minutes,
        'points':stat_list[1],
        'rebounds':stat_list[2],
        'assists':stat_list[3],
        'steals':steals,
        'blocks':blocks,
        'turnovers':turnovers,
        'fg_percent':stat_list[4],
        '3_fg_percent':stat_list[5],
        'free_throw_percent':stat_list[6],
        'effective_fg_percent':stat_list[7],
        'player_efficiency_rating':stat_list[8],
        'win_shares':stat_list[9]
    }
    return player_dict


def generate_player_df(first_letter):
    
    index_url_link = 'https://www.sports-reference.com/cbb/players/{}-index.html'.format(first_letter)
    
    player_urls = []
    index_page = SoupFromURL(index_url_link)
    index_names = index_page.find_all('p')
    index_soup = BeautifulSoup(str(index_names),"html5lib")
    links = index_soup('a', href=True)
    
    for l in links:
        try:
            player_urls.append('https://www.sports-reference.com' + l.attrs['href'])
        except:
            pass
    
    player_urls = [x for x in player_urls if not 'schools' in x]
    player_urls.pop()
    player_urls.pop()
    player_urls.pop()
    player_urls.pop()
    
    player_stats_list=[]
    for url in player_urls:
        try:
            player_stats_list.append(ncaa_stats_dict(url))
            print(url)
        except:
            pass
    
    df = pd.DataFrame(player_stats_list)
    df = df[[
        'player_name',
        'position',
        'height_inches',
        'weight_lbs',
        'college',
        'draft_year',
        'years_in_college',
        'games',
        'minutes_per_game',
        'points',
        'rebounds',
        'assists',
        'steals',
        'blocks',
        'turnovers',
        'fg_percent',
        '3_fg_percent',
        'free_throw_percent',
        'effective_fg_percent',
        'player_efficiency_rating',
        'win_shares'
    ]]
    
    
    return df