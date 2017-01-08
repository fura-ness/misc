import time

from splinter import Browser

browser = Browser()

#urls = """
#https://twitter.com/Tommytoughstuff/status/517455614038257664
#https://twitter.com/KattsDogma/status/724985571760824320
#https://twitter.com/FrancyHam/status/621362196522467329
#""".split()

tweets = [[f.strip() for f in line.split('\t')] for line in open('all-favorite-tweets.csv', 'r')]
tweets = [('https://twitter.com%s' % tweet[0], tweet[1]) for tweet in tweets]

friends = {'amgo','androidqueen','asoehnlen','chooch709','chrismkayser','CogoLabs','fishmcgill','FrappeTruckJim','JeffChausse','JessaBrez','jimmuhk','JoshArenstam','kfan','kman17','mossdogmusic','otterfamilias','rascalking','rubytoo','ScubaHey','tfederman','TomAssBender'}
misc = {'StellaMadeline1','seldo','fuzzybinary'}  # seldo gone?

for n, (url, timestamp) in enumerate(tweets):

    user, _, tweet_id = url.split('/')[3:6]
    print n, user, tweet_id

    browser.visit(url)

    dir = 'tweets-public'
    if user in friends:
        dir = 'tweets-friends'
    elif user in misc:
        dir = 'tweets-misc'

    browser.driver.save_screenshot('%s/tweet-%s-%s-%s.png' % (dir, user, timestamp, tweet_id))

    time.sleep(2)

browser.quit()


