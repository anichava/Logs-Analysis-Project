#!/usr/bin/env python3
import psycopg2


def get_most_popular_three_articles(cursor):
    statement = "select a.title, s.count from articles a, slug_views s"
    statement += " where a.slug = s.slug order by s.count DESC limit 3"
    cursor.execute(statement)
    results = cursor.fetchall()
    print("1. Most popular three articles of all time:\n")
    for row in results:
        print('"%s"' % (row[0]), '-', row[1], 'views')


def get_most_popular_authors(cursor):
    statement = "select a.name, sum(s.count) from slug_views s, authors a"
    statement += " where s.author = a.id group by a.name order by sum DESC"
    cursor.execute(statement)
    results = cursor.fetchall()
    print("\n\n2. Most popular article authors of all time are:\n")
    for row in results:
        print(row[0], '-', row[1], 'views')


def get_highest_error_percentage(cursor):
    statement = "select date, round(percentage,2) from failure_rates where"
    statement += " percentage > 1"
    cursor.execute(statement)
    results = cursor.fetchall()
    print("\n\n3. Days where more than 1% of requests lead to errors:\n")
    for row in results:
        print(row[0], '-', "{0}%".format(row[1]), "errors")


def main():
    pg = psycopg2.connect("dbname=news")
    cursor = pg.cursor()
    get_most_popular_three_articles(cursor)
    get_most_popular_authors(cursor)
    get_highest_error_percentage(cursor)
    pg.close()


if __name__ == "__main__":
    main()
