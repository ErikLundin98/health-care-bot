from flask import Flask, jsonify
from datetime import datetime as d

app = Flask(__name__, static_folder = 'static', static_url_path = '/')

@app.route('/')
def main():
    return 'Hello world'

@app.route('/available-times', methods=['GET'])
def avail_times():
    times = [
        {
            "start" : d(2020, 11, 7, 14, 30, 0),
            "stop"  : d(2020, 11, 7, 15, 30, 0)
        },

        {
            "start" : d(2020, 11, 8, 11, 0, 0),
            "stop"  : d(2020, 11, 8, 11, 30, 0)
        },
        
        {
            "start" : d(2020, 11, 8, 14, 30, 0),
            "stop"  : d(2020, 11, 8, 15, 30, 0)
        },
        
        {
            "start" : d(2020, 11, 9, 8, 15, 0),
            "stop"  : d(2020, 11, 9, 8, 45, 0)
        },
        
        {
            "start" : d(2020, 11, 9, 10, 30, 0),
            "stop"  : d(2020, 11, 9, 11, 00, 0)
        }
        ]
    return jsonify([ {"start": time["start"].isoformat(), "stop" : time["stop"].isoformat()} for time in times ])

@app.route('/current-notifications', methods=['GET'])
def curr_notifications():
    notifications = [
        {
            "notice-media-type" : "E-mail",
            "time-after" : "2 timmar",
            "time-before" : "Ingen påminnelse", 
            "type" : "Blodtryck"
        },
        {
            "notice-media-type" : "SMS",
            "time-after" : "1 timme",
            "time-before" : "3 timmar", 
            "type" : "Vikt"
        }
    ]

    return jsonify([ {"type": notification["type"], "time-after": notification["time-after"], "time-before": notification["time-before"], "notice-media-type": notification["notice-media-type]"} for notification in notifications:
        ])