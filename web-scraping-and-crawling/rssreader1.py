import feedparser

feed = feedparser.parse("https://finance.yahoo.com/rss/") # you can change the rss feed
feed_entries = feed.entries

try:
    filex = open("yahoofinanceRSS.txt", "a")
    for entry in feed_entries:

        rss_title = entry.title
        rss_link = entry.link
        rss_source = str(entry.source.href)
        print("Title:%s" %(rss_title))
        print("Check it here:%s" %(rss_link))
        print("News source:%s" %(rss_source))
        print('------------------')

        filex.write("Title:%s\n" %(rss_title))
        filex.write("Check it here:%s\n" %(rss_link))
        filex.write("News source:%s\n" %(rss_source))
        filex.write("--------------------------------\n")
        
    filex.close()
    print("written to file")
except ValueError as ve:
    print(ve)