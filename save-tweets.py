import time

from bs4 import BeautifulSoup
from splinter import Browser

OUTPUT_PATH = './tweet-images'

# people whose tweets i fave because they're friends
USERS_FRIENDS = {'amgo','androidqueen','asoehnlen','chooch709','chrismkayser','CogoLabs','fishmcgill','FrappeTruckJim','JeffChausse','JessaBrez','jimmuhk','JoshArenstam','kfan','kman17','mossdogmusic','otterfamilias','rascalking','rubytoo','ScubaHey','TomAssBender'}

# non-friend, non-comedy accounts
USERS_MISC    = {'StellaMadeline1','seldo','fuzzybinary','tfederman'}


if __name__=='__main__':

    browser = Browser()
    soup = BeautifulSoup(open('faves.html').read(), 'html.parser')

    faves = []
    for a in soup.find_all("a"):
        href = a.get('href')
        data_time = None
        for s in a.find_all('span'):
            data_time = s.get('data-time', data_time)

        if href and data_time and '/status' in href:
            faves.append((href, data_time))


    for n, (url, timestamp) in enumerate(faves):

        url = 'https://twitter.com%s' % url
        user, _, tweet_id = url.split('/')[3:6]

        print '%03d/%03d' % (n+1, len(faves))

        if user in USERS_FRIENDS:
            dir = 'tweets-friends'
        elif user in USERS_MISC:
            dir = 'tweets-misc'
        else:
            dir = 'tweets-public'

        output_path = '%s/%s' % (OUTPUT_PATH, dir)    

        browser.visit(url)
        browser.driver.save_screenshot('%s/tweet-%s-%s-%s.png' % (output_path, user, timestamp, tweet_id))

        time.sleep(2)
