import sys
from config import DB_Details

from util import get_tables

def main():
    env = sys.argv[1]
    db_details = DB_Details[env]
    tables=get_tables('table_list')
    for tables in tables['table_name']:
        print(tables)

if __name__=='__main__':
    main()