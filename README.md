# Rest API Service that returns median pickup time for a restaurant

# Example:
Request:
localhost:50000/median_pickup_time?location_id=21&start_time=2019-01-09T11:00:00&end_time=
2019-01-09T12:00:00
Response:
{
‘median’: 23
}

# About the project
This project has a REST API endpoint that accepts location id, start time and end time parameters and returns the median pickup time.This project also concerns about data caching. Redis is used data caching. 

# Requirements
- virtualenv
- python3
- Redis

# Installation
1. Clone the repo
'''
git clone https://github.com/UmmulFatima/Wolt-Coding-Assignment-Pickup-times-service.git
'''
2. Create a virtual environment
 '''
 python3 -m venv pickuptime-service
 '''
3. cd to the folder
'''
cd pickuptime-service
'''
4. Activate the virtual env:
'''
source bin/activate
'''
5. Install requirements:
'''
pip3 install requirements.txt
'''
6. Install redis server
'''
[Redis](https://redis.io/topics/quickstart)
'''
# All done!
Now you are ready to run the APP
python wolt_app.py
