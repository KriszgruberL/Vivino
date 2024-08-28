from utils.best_wineries import query_top_wineries
from utils.connect_db import close_db, connect_to_db
from utils.favorites_taste import query_favorites_taste
from utils.highlight_wines import query_highlight_wine
from utils.limited_budget import query_limited_budget
from utils.wines_by_taste import query_wine_by_taste

from utils.best_wines_per_grape import query_common_grapes
from utils.country_leaderboard import query_best_vintage_and_wine_per_country

def main() : 
    try :
        cxn, cursor= connect_to_db()
        
        query_limited_budget(cursor)
        query_highlight_wine(cursor)
        query_top_wineries(cursor)
        query_favorites_taste(cursor)
        query_common_grapes(cursor)
        query_wine_by_taste(cursor)
        query_best_vintage_and_wine_per_country(cursor)

    finally: 
        close_db(cxn)

if __name__ == "__main__":
    main()