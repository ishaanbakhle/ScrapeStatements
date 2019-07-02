import csv
import pandas as pd
import numpy as np

def splitMember(member):
    """
    Parses member html for Processing
    """
    member_split = member.split('\n')
    split_arr = []
    for i in member_split:
        split_arr.append(i.split('>'))
    return split_arr

def getParty(splitmem):
    """
    """
    attr = splitmem[0]
    return(attr[0].split('"'))[1]

def getDate(splitmem):
    """
    """
    attr = splitmem[1]
    return(attr[0].split('"')[3])

def getName(splitmem):
    """
    """
    attr = splitmem[2]
    return(attr[4].split('</a')[0])

def getStateDistrict(splitmem):
    """
    """
    attr = splitmem[5]
    return(attr[1].split('</')[0])

def getTitle(splitmem):
    """
    """
    attr = splitmem[6]
    return(attr[2].split('</')[0])

def getLink(splitmem):
    """
    """
    attr = splitmem[6]
    return(attr[1].split('"')[1])

data = pd.read_csv('/Users/ishaanbakhle/Desktop/Projects/MemberStatements/propublica/propublica/spiders/propublica.csv')
ds = data["Rows"]

dates = []
names = []
parties = []
states_districts = []
titles = []
links = []
for page in ds:
    split_page = page.split('<tr')
    split_arr = []
    for i in split_page:
        if len(i) > 3:
            split_arr.append(i)
    for member in split_arr:
        mem = splitMember(member)
        if len(mem) >= 6:
            dates.append(getDate(mem))
            names.append(getName(mem))
            parties.append(getParty(mem))
            states_districts.append(getStateDistrict(mem))
            titles.append(getTitle(mem))
            links.append(getLink(mem))
        else:
            dates.append(np.nan)
            names.append(np.nan)
            parties.append(np.nan)
            states_districts.append(np.nan)
            titles.append(np.nan)
            links.append(np.nan)

dict = {'Date':dates,'Member Name':names, 'Party':parties,'Represented Constituency':states_districts,'Statement Title':titles, 'Link':links}
df = pd.DataFrame(dict)
df.to_excel('ProPublica_ClimateChange.xlsx')
