#! /usr/bin/env python3

"""
Udacity Fullstack Nanodegree, Project: Log Analysis
This program creates a reporting tool, returning
results on the basis of some queries.

@author: Satwik Mishra
"""

import psycopg2


class LogReport:

    def __init__(self):
        self.db = psycopg2.connect("dbname=news")
        self.cur = self.db.cursor()

    def __del__(self):
        self.db.close()

    @staticmethod
    def show(result):
        """
        Prints the result.
        :param result:
        :return: None
        """
        for res in result:
            print("{:<50}{:<50}".format(res[0], res[1]))

    def query1(self):
        """
        Query: What are the most popular three
        articles of all time?
        :return: None
        """
        self.cur.execute(" SELECT title as Article_Name, count(log.id) as "
                         "Views "
                         "FROM log JOIN articles "
                         "ON log.path = concat('/article/', articles.slug) "
                         "GROUP BY Article_Name "
                         "ORDER BY Views desc "
                         "LIMIT 3;")
        print("{:<50}{:<50}".format("Article_Name", "Views"))
        print("---------------------------------------------------------")
        result = self.cur.fetchall()
        self.show(result)

    def query2(self):
        """
        Query: Who are the most popular
        article authors of all time?
        :return: None
        """
        self.cur.execute(" SELECT name, count(log.id) as Views "
                         "FROM authors JOIN articles on "
                         "authors.id = articles.author, log "
                         "WHERE log.status = '200 OK' "
                         "and log.path = concat('/article/', articles.slug) "
                         "GROUP BY name "
                         "ORDER BY Views desc;")
        print("{:<50}{:<50}".format("Author_Name", "Views"))
        print("---------------------------------------------------------")
        result = self.cur.fetchall()
        self.show(result)

    def query3(self):
        """
        Query : On which days did more than 1% of requests lead to errors?
        Using the following two views, namely Errors and Total to find
        the dates where request failures > 1%
        view 1 (Errors) : create view Errors as select time::date
                          as Date ,count(status) from log where status like
                          '4%' or status like '3%' group by Date;
        view 2 (Total) : create view Total as select time::date as Date,
                         count(status) from log group by Date;
        :return: None
        """
        self.cur.execute(" SELECT Errors.Date, "
                         "Round((Errors.count*1.0/Total.count*1.0)*100,2) as "
                         "perc "
                         "FROM Errors JOIN Total ON Errors.Date = Total.Date "
                         "WHERE (Errors.count*1.0/Total.count*1.0)*100 > 1;")
        res = self.cur.fetchone()
        print("{:<50}{:<50}".format("Day", "Percentage error"))
        print("---------------------------------------------------------")
        res = "{:%d, %b %Y}".format(res[0]), "{}".format(res[1])
        print("{:<50}{:<50}".format(res[0], res[1]))


def main():
    log = LogReport()
    log.query1()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    log.query2()
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    log.query3()
    del log


if __name__ == "__main__":
    main()
