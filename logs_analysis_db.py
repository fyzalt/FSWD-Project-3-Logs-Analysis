import psycopg2

DBNAME = "news"

# SQL code for most popular articles
query_articles = """
SELECT
  articles.title,
  COUNT(log.path) AS views
FROM
  articles,
  log
WHERE
  (log.path = '/article/' || articles.slug)
   AND (log.status = '200 OK')
GROUP BY
  articles.title
ORDER BY
  views DESC
LIMIT 3 """

# SQL code for most popular authors
query_authors = """
SELECT
  authors.name,
  COUNT(log.path) AS views
FROM
  articles,
  authors,
  log
WHERE
  (log.path = '/article/' || articles.slug)
  AND (articles.author = authors.id)
  AND (log.status = '200 OK')
GROUP BY
  authors.name
ORDER BY
  views DESC
LIMIT 4"""

# SQL code for request error rate
query_error_rate = """
SELECT
  DATE(time),
  ROUND(SUM(CASE WHEN log.status!='200 OK' THEN 1 ELSE 0 END)*100.0
  /COUNT(log.status),2) AS error_rate
FROM
  log
GROUP BY
  DATE(time)
HAVING
  SUM(CASE WHEN log.status!='200 OK' THEN 1 ELSE 0 END)*100.0
  /COUNT(log.status) > 1
ORDER BY
  error_rate DESC"""


def get_popular_articles():
    """Returning top 3 most popular articles from the 'database'"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query_articles)
    result = c.fetchall()
    db.close()
    return result


def get_popular_authors():
    """Returning top 3 most popular authors from the 'database'"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query_authors)
    result = c.fetchall()
    db.close()
    return result


def get_error_rate():
    """Returning days with more than 1% of requests lead to errors"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query_error_rate)
    result = c.fetchall()
    db.close()
    return result
