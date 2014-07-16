# Flask-yo
This is a simple app, using Yo API with flask.

## Setup

First, you must get  a  [Yo API key](http://yoapi.justyo.co/)

### local
1. Clone this repo locally. `git clone https://github.com/braitom/Flask-yo.git`
2. `cd Flask-yo`
3. `pip install -r requirements.txt`		
NOTICE : If you necessary, set the VirtualEnv.
4. Replace '[YOUR_YO_API_TOKEN]' in config.py
5. Run this app. `python flask-yo.py`

### heroku
1. Clone this repo locally. `git clone https://github.com/braitom/Flask-yo.git`
2. `cd Flask-yo`
3. `heroku login`
4. `heroku create`
4. Replace '[YOUR_YO_API_TOKEN]' in config.py
6. `git push heroku master`

## Useing
* POST `/`  
Send yo, to all subscribers.
* GET `/count`  
You get subscribers counts.


## License
MIT License
