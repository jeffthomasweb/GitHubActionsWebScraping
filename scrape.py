import feedparser
import re

def rss(rss_address):
    #Use feedparser library to get RSS feed data. Data will originally be in a XML format.
    feedparser_parse = feedparser.parse(rss_address)
    #Create anempty list story_list to add RSS feed story titles and story summaries.
    story_list = []
    #The feedparser library is good at parsing the original XML format RSS feed data but is unable to take out some HTML tags like <em> and </em>
    #Use Python's regular expression library to get rid of these <em> and </em> tags. Create two empty lists for this process.
    clean_story_list1 = []
    clean_story_list2 = []
    #Use feedparser to get the 15 stories in the RSS feed.
    for i in range(0,15):
        story_list.append(feedparser_parse.entries[i].title + '. ' + feedparser_parse.entries[i].summary)

    #Use regular expression to clean the <em> and </em> tags.
    for cleantag in story_list:
        clean_story_list1.append(re.sub('<em>', '', cleantag))

    for cleantag2 in clean_story_list1:
        clean_story_list2.append(re.sub('</em>', '', cleantag2))

    #Return the final, cleaned list.
    return clean_story_list2

#Variable npr_list is the saved RSS feed data for NPR's feed. ars_list and buffalo_list are the saved RSS feed data for two other feeds.
npr_list = rss("https://feeds.npr.org/1001/rss.xml")

ars_list = rss("https://feeds.arstechnica.com/arstechnica/index")

buffalo_list = rss("https://www.wgrz.com/feeds/syndication/rss/news/local")

with open("output.txt", "w") as output_file:
    output_file.writelines("**********NPR stories**********\n\n")
    for individual_npr in npr_list:
        output_file.writelines(individual_npr)
        output_file.writelines("\n\n")
    output_file.writelines("**********Ars Technica stories**********\n\n")
    for individual_ars in ars_list:
        output_file.writelines(individual_ars)
        output_file.writelines("\n\n")
    output_file.writelines("**********Buffalo News stories**********\n\n")
    for individual_buffalo in buffalo_list:
        output_file.writelines(individual_buffalo)
        output_file.writelines("\n\n")
