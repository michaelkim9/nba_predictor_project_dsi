import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re

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

def nba_2016_player_dict(url):
    player_page = SoupFromURL(str(url))
    player_dict = {}
    stat_list = []
    new = []
    try:
        p = player_page.find_all('div',attrs={'class':'stats_pullout'})
        p_soup = BeautifulSoup(str(p),"html5lib")
        stat_career = p_soup.text.split('\n')[0::4][2:] #change this to 0::4
        for item in stat_career:
            new.append(float(''.join(i for i in item if i in '1234567890.')))
        for s in new:
            try:
                if s== str(""):
                    stat_list.append(None)
                else:
                    stat_list.append(float(s))
            except:
                stat_list.append(None)
    except:
        stat_list.extend([None,None,None,None,None,None,None,None,None,None])    

    if stat_list == [None, None, None, None, None, None, None, None, None, None]:
        return stat_list[100]
    
    else:
        try:
            player_dict['per'] = stat_list[-2]
        except:
            player_dict['per'] = None
        
        try:
            player_dict['ws'] = stat_list[-1]
        except:
            player_dict['ws'] = None
            
        a = player_page.find_all('div', attrs={'itemtype':'https://schema.org/Person'})[0]
        try:
            b_soup = BeautifulSoup(str(a),"html5lib")
            b = b_soup.text.split('\n')
            b = list(filter(None, b))
            age_index = b.index('  Born:')
            age_born = b[age_index:]
            age_year = age_born[3]
            age_year = int(age_year.replace('            ', ''))
            age = 2017 - age_year
            player_dict['age'] = age
        except:
            player_dict['age'] = None
        
        a_soup = BeautifulSoup(str(a),"html5lib")
        a = a_soup.text.split('\n')
        a = list(filter(None, a))
        to_remove = ['  ','    ','  ▪','\t','  Position:','  Shoots:','  Born:','  us','  in']
        for remove in to_remove:
            a=remove_values_from_list(a,remove)
        
        starts_with_removal = ['(','      ','            ','    in','    More bio','  NBA Debut','  ABA Debut','Relatives:','  Pronunciation:']
        for removal in starts_with_removal:
            a=[x for x in a if not x.startswith(removal)]
        
        if a[2] == '  Twitter:':
            del a[2:4]
        else:
            a
        
        if a[-2] == '  Experience:':
            a.pop()
            a.pop()
        else:
            a
        
        if a[5] == '  Died:':
            del a[5:7]
        else:
            a
            
        try:
            name = a[0]
            player_dict['player_name'] = name.replace("\t","")
        except:
            player_dict['player_name'] = None
            
        try:
            position = a[2]
            player_dict['position'] = position.replace('  ','')
        except:
            player_dict['position'] = None
            
        try:
            shooting_hand = a[3]
            player_dict['shooting_hand'] = shooting_hand.replace('  ','')
        except:
            player_dict['shooting_hand'] = None
        
        try:
            body = a[4].split(',')
            ft = int(body[0][0])*12
            if len(body[0]) == 3:
                inch = int(body[0][-1])
            elif len(body[0]) == 4:
                inch = int(body[0][2:4])
            player_dict['height_inches'] = ft+inch
        
            w = body[1].replace(u'\xa0', u'')
            player_dict['weight_lbs'] = int(w[0:3])
        except:
            player_dict['height_inches']=None
            player_dict['weight_lbs']=None
        
        if a[5] == '  College:':
            college = a[6]
            player_dict['college'] = college.replace('  ','')
        elif a[6] == '  College:':
            college = a[7]
            player_dict['college'] = college.replace('  ','')
        else:
            player_dict['college'] = 'no_college'
        
        if a[5].startswith('  Team'):
            player_dict['current_team'] = a[5][8:]
        else:
            player_dict['current_team'] = 'no_current_team'
        
        if a[-2] == '  Draft:':
            draft = a[-1].split(',')
            player_dict['draft_year'] = int(draft[-1][1:5])
            player_dict['draft_position'] = int(re.sub('\D','',draft[2]))
        elif a[-3] == '  Draft:':
            draft = a[-2].split(',')
            player_dict['draft_year'] = int(draft[-1][1:5])
            draft_position = int(re.sub('\D','',draft[2]))
        else:
            draft='not_drafted'
            player_dict['draft_year']='not_drafted'
            player_dict['draft_position']='not_drafted'
        
        try:
            all_s = player_page.find_all('ul', attrs={'id':'bling'})
            all_soup = BeautifulSoup(str(all_s),"html5lib")
            all_s = all_soup.text.split('\n')
        
            if any('All Star' in s for s in all_s):
                player_dict['all_star']=1
            else:
                player_dict['all_star']=0
        except:
            player_dict['all_star']=0
        
            
        additional_stats = player_page.find_all('td', attrs={'class':'right'})
        additional_soup = BeautifulSoup(str(additional_stats),'html5lib')
        additional_soup = additional_soup.text.split(',')
        new_add_soup = [additional_soup[i:i+25] for i in range(0, len(additional_soup), 25)]
        
        try:
            empty_list = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
            target_index = new_add_soup.index(empty_list)
            stats_lists = new_add_soup[:target_index]
        except:
            stats_lists = new_add_soup
        
        career_per_game = stats_lists[-2]
        career_per_game = [item.replace(']', '') for item in career_per_game]
        
        stats_columns = [
            'g',
            'gs',
            'mp',
            'fg',
            'fga',
            'fg_perc',
            '3p',
            '3pa',
            '3p_perc',
            '2p',
            '2pa',
            '2p_perc',
            'efg_perc',
            'ft',
            'fta',
            'ft_perc',
            'orb',
            'drb',
            'trb',
            'ast',
            'stl',
            'blk',
            'tov',
            'pf',
            'pts'
        ]
        
        number_list = list(range(25))
        zipped = zip(stats_columns,number_list)
        
        for column,number in zipped:
            try:
                player_dict[column]=float(career_per_game[number])
            except:
                player_dict[column]=None
        
        additional_stats_2 = player_page.find_all('td', attrs={'class':'left'})
        additional_soup_2 = BeautifulSoup(str(additional_stats_2),'html5lib')
        additional_soup_2 = additional_soup_2.text.split(',')

        additional_soup_2 = remove_values_from_list(additional_soup_2,' NBA')
        try:
            target_ind = additional_soup_2.index(' ')
            team_id = additional_soup_2[:target_ind]
        except:
            team_id = additional_soup_2
        try:
            teams = []
            for i in team_id:
                j = i.replace(' ','')
                teams.append(j)
            
            salary_team = teams[-1]
            salary_team = re.sub('[^0-9a-zA-Z]+', '', salary_team)
            player_dict['salary_team'] = salary_team
            season_count = len(teams)
            player_dict['season_count'] = season_count
    
        except:
            player_dict['salary_team'] = None
            player_dict['season_count'] = None
        
        try:
            salary_stats = player_page.find_all('div',{'id':'all_all_salaries'})
            salary_str = str(salary_stats)
            salary_str = salary_str.split('\n')
            salary_str = [k for k in salary_str if 'salary' in k]
        
            salary_select = salary_str[-2][-22:-1]
            player_dict['recent_salary'] = float(re.sub('\D','',salary_select))
        
            salary_year = salary_str[-2][50:76]
            salary_year = re.sub('\D','',salary_year)
            player_dict['salary_year'] = int(salary_year[0:4])
        except:
            player_dict['recent_salary'] = 'not_listed'
            player_dict['salary_year'] = 'not_listed'
        
        return player_dict


def generate_2016_nba_player_df(first_letter):
    index_url_link = 'https://www.basketball-reference.com/players/{}/'.format(first_letter)
    
    player_urls = []
    index_page = SoupFromURL(index_url_link)
    index_names = index_page.find_all('tr')
    index_soup = BeautifulSoup(str(index_names),"html5lib")
    links = index_soup('a', href=True)

    for l in links:
        try:
            player_urls.append('https://www.basketball-reference.com' + l.attrs['href'])
        except:
            pass
    
    player_urls = [x for x in player_urls if not 'colleges' in x]
    player_urls = [x for x in player_urls if not 'birthdays' in x]
    
    player_stats_list=[]
    for url in player_urls:
        try:
            player_stats_list.append(nba_2016_player_dict(url))
            print(url)
        except:
            pass
    
    df = pd.DataFrame(player_stats_list)
    df = df[[
        'player_name',
        'position',
        'shooting_hand',
        'height_inches',
        'weight_lbs',
        'college',
        'draft_year',
        'draft_position',
        'season_count',
        'age',
        'current_team',
        'g',
        'gs',
        'mp',
        'pts',
        'fg',
        'fga',
        'fg_perc',
        '3p',
        '3pa',
        '3p_perc',
        '2p',
        '2pa',
        '2p_perc',
        'efg_perc',
        'ft',
        'fta',
        'ft_perc',
        'orb',
        'drb',
        'trb',
        'ast',
        'stl',
        'blk',
        'tov',
        'pf',
        'all_star',
        'per',
        'ws',
        'recent_salary',
        'salary_year',
        'salary_team'
    ]]
    return df
