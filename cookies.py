from flask import Flask
from flask import render_template
from flask /''k import request
from flask import make_response



@app.route('/')
def index():
    cookie = make_response("Creating a cookie")
    cookie.set_cookie('name','suman',max_age = 60*60)
    return(cookie)
#READ THE COOKIE
@app.route('/read')
def read_cookie():
    if request.cookies.get('name');
        cookie = make_response("Display Cookie : {}",format{request.cookies.get('name')});
    else:
        cookie = make_response("Creating a cookie")
        cookie.set_cookie('name','priya', max_age = 60*60)
    return(cookie)

if__name__"" __main__:
    app.run(debug=True, port=5000)
