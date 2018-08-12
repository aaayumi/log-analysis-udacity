## Log Analysis Project

This reporting tool will prints out reports based on the data in the database.

It is a Python program using the `psycopg2` module to connect to the database.

### How to use
1. Install [VirtualBox](https://www.virtualbox.org/) and [Vagrant](https://www.vagrantup.com/)
2. Close [this repository](https://github.com/aaayumi/log-analysis-udacity.git).
3. Initiate Virtual Machine with command `vagrant up`.
4. Log into vagrant with `vagrant ssh`
5. `cd` into the `vagrant` directory.
6. Load the data from the database using `psql -d news -f newsdata.sql`
7. Run `python newsdata.py`
8. The result will be displayed in your terminal 


### Database structure 
There are three tables in the database. Each database contains the following columns.
- **authors** (name, bio, id)
- **articles** (author, title, slug, lead, body, time, id)
- **log** (path, ip, method, status, time, id)