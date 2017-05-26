from logs_analysis_db import get_popular_articles,\
                             get_popular_authors, \
                             get_error_rate

print("Getting data...")

"""Getting top 3 most popular articles from the 'database'"""
popular_articles = get_popular_articles()
print("")
print("1. What are the most popular three articles of all time?")
for row in popular_articles:
    print('"%s" - %s views' % row)

"""Getting top 3 most popular authors from the 'database'"""
popular_authors = get_popular_authors()
print("")
print("2. Who are the most popular article authors of all time?")
for row in popular_authors:
    print('%s - %s views' % row)

"""Getting days with more than 1% of requests lead to errors"""
error_rate = get_error_rate()
print("")
print("3. On which days did more than 1% of requests lead to errors?")
for row in error_rate:
    print ("{0[0]:%b,%d,%Y} - {0[1]:.2f}% errors".format(row))
