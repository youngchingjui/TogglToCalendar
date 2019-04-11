from toggl.TogglPy import Toggl
import pandas as pd
import datetime

toggl = Toggl()

toggl.setAPIKey('2e8cb0eb95b4d98c98564e4ba8ee26ee')

duration = 5 # minutes
until = datetime.datetime.now()
since = until - datetime.timedelta(min=duration)
page = 1
more_results = True

# Run while we have more results on the next page
while (more_results):
    data =  {
        'workspace_id': 2705063,
        'since': since,
        'until': since.strftime,
        'page': page
    }
    response = toggl.getDetailedReport(data)

    df = pd.DataFrame(response['data'])

    # For each new entry, create a new Calendar entry

    for i, row in df.iterrows:
        createNewCalendarEntry(i)

    page += 1
    total_results = response['total_count']

    more_results = ((page-1) * 50 < total_results)
    

def createNewCalendarEntry(i):
    # TODO: Implement
    pass
