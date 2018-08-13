#!/usr/bin/env python2
import psycopg2

DBNAME = "news"


def connect_database(query):
    """Connect to the news database"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)

    return c.fetchall()
    db.close()


query1 = '''select title, count(title) as num from articles, log
         where log.path = concat('/article/', articles.slug)
         group by title order by num desc limit 3;'''

query2 = '''select name, count(name) as num from authors, articles,log
         where articles.author = authors.id
         and log.path = concat('/article/', articles.slug)
         group by name order by num desc;'''

query3 = '''select * from(
         select all_queries.date,
         (cast(error_queries.errors *100 as float)/all_queries.all) as ratio
         from (
         (select date(time), count(status) as errors
         from log where status != '200 OK'
         group by date(time)) error_queries
         full join
         (select date(time), count(status) as all from log
         group by date(time)) all_queries
         on all_queries.date = error_queries.date
         )) ratio_table
         where ratio_table.ratio > 1;
         '''


def print_query1_answer(query):
    answers = connect_database(query)
    print('What are the most popular three articles of all time? ')
    for answer in answers:
        print('\t' + str(answer[0]) + ' - ' + str(answer[1]) + ' views')


def print_query2_answer(query):
    answers = connect_database(query)
    print('Who are the most popular article authors of all time? ')
    for answer in answers:
        print('\t' + str(answer[0]) + ' - ' + str(answer[1]) + ' views')


def print_query3_answer(query):
    answers = connect_database(query)
    print('On which days did more than 1% of requests lead to errors?')
    for answer in answers:
        print('\t' + str(answer[0]) + ' - ' + str(answer[1]) + ' % errors')


# call results
print_query1_answer(query1)

print_query2_answer(query2)

print_query3_answer(query3)
