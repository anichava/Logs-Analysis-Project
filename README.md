# Logs Analysis Project

## Quick start

Project Setup:

- Make sure you have [Vagrant](https://www.vagrantup.com) installed.
- Make sure you have [VirtualBox](https://www.virtualbox.org/wiki/Downloads) installed.
    - Install the platform package for your operating system. You do not need the extension pack or the SDK.
- Make sure you have python installed. Check version: `python3 --version`.
- This project was tested on `Python 3.5.2`.
- Download [FSND-Virtual-Machine.](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip)
    - This will give you a directory called FSND-Virtual-Machine.
- From the terminal, `cd` into `FSND-Virtual-Machine` directory.
    - Inside, you will find another directory called `vagrant`. `cd` into the `vagrant` directory. 
- Start the virtual machine:
    - Inside the `vagrant` directory, run the command `vagrant up`.
    - Then, run `vagrant ssh` to log in to your newly installed Linux VM!
- Download [SQL Data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) into the `vagrant` folder.
- To load the data, use the command `psql -d news -f newsdata.sql` inside the `vagrant` folder in your newly installed Linux VM.
- Clone repo into the `vagrant` directory: `git clone https://github.com/anichava/Logs-Analysis-Project.git`.

Before Launch - Creating Views:
- Inside `vagrant` directory inside the VM, run `psql -d news`
- Copy, paste, and run: `create view slug_views as select a.slug, a.author, count(a.slug) from articles a, log l where l.path like concat ('%',a.slug) group by a.slug, a.author;`
- Copy, paste, and run: `create view success_table as select date(time), count(l.status) as success_count from log l where l.status like '%200%' group by date(time);`
- Copy, paste, and run: `create view error_table as select date(time), count(l.status) as error_count from log l where l.status not like '%200%' group by date(time);`
- Copy, paste, and run: `create view failure_rates as select s.date, (sum(e.error_count)/(sum(s.success_count) + sum(e.error_count))) * 100 as percentage from error_table e, 
success_table s where s.date = e.date group by s.date;`

Launching:
- `cd` to `Logs-Analysis-Project` from inside the `vagrant` folder (inside the VM).
- Run the program: `python3 logsanalysis.py`

## Summary

The database contains newspaper articles, as well as the web server log for a site. Using that information, this code will answer questions about the site's user activity. 

When the program is executed, you will see answers to 3 questions regarding the data in the database:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors? 

You should look around the data in your database so that you get a better understanding of the data.

All of the data is processed on the database side, and the code only makes requests and prints the data out for the user to see.

Views were created so that they could be potentially used by multiple queries, so that queries as a whole get smaller and easier to manage.