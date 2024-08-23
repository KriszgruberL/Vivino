from utils.connect_db import close_db, connect_to_db
from utils.limited_budget import query_limited_budget


def main() : 
    cxn, cursor = connect_to_db()
    
    query_limited_budget()
    
    
    
    close_db(cxn)


if __name__ == "__main__":
    main()