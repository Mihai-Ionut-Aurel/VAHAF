from Utilities import keys_config
import stackexchange
import datetime
so = stackexchange.Site(stackexchange.StackOverflow, app_key=keys_config.stackexchange_key, impose_throttling=True)
so.impose_throttling = True
so.throttle_stop = False

start_date=1509494400  #datetime.date(year=2017,month=10,day=1)
end_date=1514678400  #datetime.date(year=2017,month=12,day=31)


def search_questions(term,pages):
    results = []
    #https://api.stackexchange.com/docs/advanced-search
    # #page=1&fromdate=2017-11-01&todate=2017-12-31&order=desc&sort=activity&answers=1&tagged=android&filter=default&site=stackoverflow
    search = so.search_advanced(tagged=[term], answers=1, fromdate=start_date, todate=end_date)
    for i in range(0, pages):
        for q in search.items:
            results.append(q)
        search = search.fetch_next()
        if len(search) == 0:
            break
    return results

def questions_to_json(array):
    results = []
    for q in array:
        results.append(q.json)
    return results
