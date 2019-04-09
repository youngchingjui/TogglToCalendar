from toggl.TogglPy import Toggl
import pandas as pd

toggl = Toggl()

toggl.setAPIKey('2e8cb0eb95b4d98c98564e4ba8ee26ee')

data =  {
    'workspace_id': 2705063,
    'since': '2019-04-01',
    'until': '2019-04-08',
    'page': 1
}

response = toggl.getDetailedReport(data)

df = pd.DataFrame(response['data'])


# Get detailed report every 