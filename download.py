import requests
from bs4 import BeautifulSoup


BASE_URL = 'https://fangj.github.io/friends/'


def get_html_file(url):
    content = requests.get(BASE_URL+url).text
    soup = BeautifulSoup(content, "lxml")
    return soup.text


def save_season_script(season, episodes):
    i = 1
    for episode_url in episodes:
        content = get_html_file(episode_url)
        f = open("dataset/{}.{}.txt".format(season, str(i)),
                 "w", encoding='utf-8')
        f.write(content)
        f.close()
        i += 1
        print("Created {}.{}.txt".format(season, i))


def get_episode_list():

    content = requests.get(BASE_URL).text
    soup = BeautifulSoup(content, "lxml")

    all_episode = [a['href'] for a in soup.find_all('a')]

    season1 = all_episode[0:24]
    save_season_script('1', season1)

    season2 = all_episode[24:47]
    save_season_script('2', season2)

    season3 = all_episode[47:72]
    save_season_script('3', season3)

    season4 = all_episode[72:95]
    save_season_script('4', season4)

    season5 = all_episode[95:118]
    save_season_script('5', season5)

    season6 = all_episode[118:141]
    save_season_script('6', season6)

    season7 = all_episode[141:164]
    save_season_script('7', season7)

    season8 = all_episode[165:188]
    save_season_script('8', season8)

    season9 = all_episode[188:211]
    save_season_script('9', season9)

    season10 = all_episode[211:]
    save_season_script('10', season10)
