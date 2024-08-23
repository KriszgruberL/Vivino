from utils.best_wineries import query_top_wineries
from utils.connect_db import close_db, connect_to_db
from utils.favorites_taste import query_favorites_taste
from utils.highlight_wines import query_highlight_wine
from utils.limited_budget import query_limited_budget


def main() : 
    cxn, cursor= connect_to_db()
    
    # query_limited_budget(cursor)
    # query_highlight_wine(cursor)
    # query_top_wineries(cursor)
    query_favorites_taste(cursor)

    
    close_db(cxn)


if __name__ == "__main__":
    main()