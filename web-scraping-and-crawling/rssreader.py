import feedparser
# import webbrowser

feed = feedparser.parse("https://finance.yahoo.com/rss/")

feed_entries = feed.entries
# print(feed_entries)

for entry in feed_entries:

    rss_title = entry.title
    rss_link = entry.link
    # rss_pubdate = entry.pubDate

    print(rss_title)
    print(rss_link)
    # print(rss_pubdate)
    print('------------------')
