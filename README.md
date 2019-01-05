# Project Log Analysis

This project's objective is to create a reporting tool, returning results on the basis of queries, from a database using Python and PostgreSQL.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* Vagrant and Virtual Box
* Download or clone _fullstack-nanodegree-vm_ repo

### Steps
1. Setup vagrant, command: vagrant up, then vagrant ssh
2. To load the data, 'cd' into the vagrant directory and use the command 'psql -d news -f newsdata.sql'
3. Create two database views using the following queries:
	* view 1 (Errors) : CREATE VIEW Errors as SELECT time::date as Date ,count(status) FROM log WHERE status like
                          '4%' or status like '3%' GROUP BY Date;

        * view 2 (Total) : CREATE VIEW Total as SELECT time::date as Date, count(status) FROM log group by Date;
4. use cmd line to run src.py

## Authors

* **Satwik Mishra**

