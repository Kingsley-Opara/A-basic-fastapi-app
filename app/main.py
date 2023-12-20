from fastapi import FastAPI
from datetime import datetime
from datetime import date

today = date.today()

app = FastAPI()

def get_the_current_weekday():
    if (weekday := today.weekday()) == 0:
        return 'Monday'
    elif weekday == 1:
        return 'Tuesday'
    elif weekday == 2:
        return 'Wednesday'
    elif weekday == 3:
        return 'Thursday'
    elif weekday == 4:
        return 'Friday'
    elif weekday == 5:
        return 'Saturday'
    return 'Sunday'


@app.get('/api', status_code=200)
async def home(slack_name: str = 'Kingsley Udochukwu', track: str = 'backend'):
    hng_profile = {
        "slack_name": slack_name,
        "current_day": get_the_current_weekday(),
        "utc_time": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "track": track,
        "github_file_url": 'https://github.com/Kingsley-Opara/A-basic-fastapi-app/blob/main/app/main.py',
        "github_repo_url": "https://github.com/Kingsley-Opara/A-basic-fastapi-app/",
        "status_code": 200

    }
    
    return hng_profile
