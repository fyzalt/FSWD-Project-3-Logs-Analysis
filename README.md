## Logs Analysis

### About this Project

An internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

### Prerequisites

1.Python 2.7 or 3.6

2.SQL

3.Vagrant and Virtual Box

### Preparation and Setup

1.Download and unzip database file [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) or by cloning this repository.

2.The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.

3.Start the virtual machine.

4.To load the data, use the command shown below.
```
psql -d news -f newsdata.sql.
```
5.Run "python logs_analysis.py".

### Sample Outputs
```
vagrant@vagrant:/vagrant/newsdata$ python logs_analysis.py
Getting data...

1.What are the most popular three articles of all time?
"Candidate is jerk, alleges rival" - 338647 views
"Bears love berries, alleges bear" - 253801 views
"Bad things gone, say good people" - 170098 views

2.Who are the most popular article authors of all time?
Ursula La Multa - 507594 views
Rudolf von Treppenwitz - 423457 views
Anonymous Contributor - 170098 views
Markoff Chaney - 84557 views

3.On which days did more than 1% of requests lead to errors?
Jul,17,2016 - 2.26% errors
vagrant@vagrant:/vagrant/newsdata$


```
