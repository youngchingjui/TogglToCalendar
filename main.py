from toggl.TogglPy import Toggl
import pandas as pd
import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def root():
    # For the sake of example, use static information to inflate the template.
    # This will be replaced with real information in later steps.
    dummy_times = [datetime.datetime(2018, 1, 1, 10, 0, 0),
                   datetime.datetime(2018, 1, 2, 10, 30, 0),
                   datetime.datetime(2018, 1, 3, 11, 0, 0),
                   ]

    return render_template('index.html', times=dummy_times)

@app.route('/run')
def run():

    # Connect with Google Calendar

    from google.auth import app_engine
    import googleapiclient.discovery

    project = "toggltocalendar"
    SCOPES = ['https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/calendar.events']

    # Explicitly use App Engine credentials. These credentials are
    # only available when running on App Engine Standard.
    credentials = app_engine.Credentials(scopes=SCOPES)

    # Explicitly pass the credentials to the client library.
    storage_client = googleapiclient.discovery.build('storage', 'v1', credentials=credentials)

    # Make an authenticated API request
    buckets = storage_client.buckets().list(project=project).execute()
    print(buckets)


    # Connect with Google Calendar to read and create events


    service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)

    calendars = service.calendarList().list().execute()

    print(calendars)

    # Create toggl object
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

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)