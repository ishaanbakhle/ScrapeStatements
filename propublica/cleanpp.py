import csv
import pandas as pd

data = pd.read_json('/Users/ishaanbakhle/Desktop/Projects/MemberStatements/propublica/propublica/spiders/propublica.json')

member_list = data["Rows"][0]
# dict = {'Attr':splitMember(member_list[0])}
# df = pd.DataFrame(dict)
# df
def splitMember(member):
    """
    Parses representative profiles from propublica statement tables
    """
    mem_less = member.split("<")
    mem_split = []
    for i in mem_less:
        mem_split.append(i.split(">"))
    return(mem_split)

def getName(splitmem):
    """
    Returns member name
    """
    attr = splitmem[9]
    return(attr[1][1:])

def getLink(splitmem):
    """
    Returns link from splitMember output
    """
    attr = splitmem[17]
    return(attr[0].split('a href=')[1].split('"')[1])

def getTitle(splitmem):
    """
    Returns statement title from splitMember output
    """
    attr = splitmem[17]
    return(attr[1])

def getDate(splitmem):
    """
    Returns statement date from splitMember output
    """
    attr = splitmem[2]
    return(attr[0].split("data-title=")[1].split('"')[1])


def getParty(splitmem):
    """
    Returns party from splitMember output
    """
    attr = splitmem[1][0].split('"')
    return(attr[1])

def getState(splitmem):
    """
    Returns party from splitMember output
    """
    attr = splitmem[14]
    return(attr[1])



dates = []
member_names = []
parties = []
states_districts = []
titles = []
links = []

for member in member_list:
    split = splitMember(member)
    dates.append(getDate(split))
    member_names.append(getName(split))
    parties.append(getParty(split))
    states_districts.append(getState(split))
    titles.append(getTitle(split))
    links.append(getLink(split))

dict = {'Date':dates, 'Member Name':member_names, 'Parties':parties, 'State/District':states_districts,'Title':titles,'Links':links}
df = pd.DataFrame(dict)
df
