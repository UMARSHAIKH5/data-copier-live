import sys
from config import DB_Details

def main():
    env = sys.argv[1]
    db_details = DB_Details[env]

if __name__=='__main__':
    main()