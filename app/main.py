from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get('/api', status_code=200)
async def home(slack_name: str = 'Kingsley Udochukwu', track: str = 'backend'):
    hng_profile = {
        "slack_name": slack_name,
        "current_day": "Saturday",
        "utc_time": datetime.utcnow(),
        "track": track,
        "github": 'https://github.com/Kingsley-Opara',
        "github_repo_url": "https://github.com/Kingsley-Opara/A-basic-fastapi-app/",
        "status_code": 200

    }
    
    return hng_profile