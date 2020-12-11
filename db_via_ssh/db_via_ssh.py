#!/usr/bin/python3

import paramiko
from sshtunnel import SSHTunnelForwarder
# from paramiko import SSHClient   # Not Used

# Needed for PyMySQL and Pandas
# import pymysql
# import pandas as pd

# Needed for SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.sql import text
#from sqlalchemy.orm import sessionmaker
#from sqlalchemy.ext.declarative import declarative_base


ssh_host = 'www.haikudesigns.com'
ssh_port = 22
ssh_user = 'redacted'
ssh_pkey = paramiko.RSAKey.from_private_key_file('redacted')
# if you want to use ssh password use - ssh_password='your ssh password', below

sql_hostname = 'localhost'
sql_username = 'redacted'
sql_password = 'redacted'
sql_main_database = 'redacted'
sql_port = 3306

########################################################################################################################

def create_mysql_ssh_tunnel(ssh_host, ssh_port, ssh_user, ssh_pkey, sql_hostname, sql_username, sql_password,
                            sql_main_database, sql_port):

    with SSHTunnelForwarder(
            (ssh_host, ssh_port),
            ssh_username=ssh_user,
            ssh_pkey=ssh_pkey,
            remote_bind_address=(sql_hostname, sql_port)) as tunnel:

        print("Tunnel: {}".format(tunnel))
        print("----------------------------------------------")

        #query_db_with_pymysql(tunnel, sql_username, sql_password, sql_main_database)
        query_db_with_sqlalchemy(tunnel, sql_username, sql_password, sql_main_database)

        tunnel.close()


# def query_db_with_pymysql(tunnel, sql_username, sql_password, sql_main_database):
#     conn = pymysql.connect(host='127.0.0.1', user=sql_username,
#                            passwd=sql_password, db=sql_main_database,
#                            port=tunnel.local_bind_port)
#     query = '''SELECT VERSION();'''
#     data = pd.read_sql_query(query, conn)
#
#     print("Data: {}".format(data))
#     conn.close()


def query_db_with_sqlalchemy(tunnel, sql_username, sql_password, sql_main_database):
    db_driver = 'mysql+pymysql'
    engine = create_engine('{}://{}:{}@{}:{}/{}'.format(db_driver, sql_username, sql_password, '127.0.0.1',
                                                     tunnel.local_bind_port, sql_main_database),
                           echo=False)

    # Session = sessionmaker(bind=engine)
    # session = Session()
    # Base = declarative_base()

    sql = text('''SELECT VERSION();''')

    results = engine.connect().execute(sql, {})
    print("Rows: {}".format(results.rowcount))



########################################################################################################################

create_mysql_ssh_tunnel(ssh_host, ssh_port, ssh_user, ssh_pkey, sql_hostname, sql_username, sql_password,
                                 sql_main_database, sql_port)

