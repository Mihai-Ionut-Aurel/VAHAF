from Utilities.ITunesAPI.itunes import *
from DataStructures import store_app
if not is_caching_enabled():
    enable_caching('Data/itunes_cache') #If no param given it creates a folder in /tmp


def siri_app_itunes(query,pages):
    results=[]
    for i in range(0,pages):
        results.extend(list(search_app(query=query,limit=200,offset=(i*200))))

    storeApps= []
    software = Software(1)
    for software in results:
        app = store_app.StoreAppData(software.get_id())
        app.release_date=software.release_date
        app.ratings_count=software.get_num_ratings()
        app.rating=software.get_avg_rating()
        app.ratings_count_curr=software.get_num_ratings_current_version()
        app.ratings_curr_ver=software.get_avg_rating_current_version()
        app.name=software.get_name()
        app.url=software.get_url()
        app.languages=software.get_languages()
        app.supported_devices=software.get_supported_devices()
        app.genre=software.get_genres()
        storeApps.append(app)
    return storeApps
