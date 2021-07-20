from flask import Flask, g, request, redirect, url_for
import functools
app = Flask(__name__)

def login_required(func):
    """Make sure user is logged in before proceeding"""
    @functools.wraps(func)
    def wrapper_login_required(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("login", next=request.url))
        return func(*args, **kwargs)
    return wrapper_login_required

@app.route("/secret")
@login_required
def secret():
    pass

# The final example before moving on to some fancier decorators is commonly used when working with
# a web framework. In this example, we are using Flask to set # up a /secret web page that should
# only be visible to users that are logged in or otherwise authenticated:
#
# While this gives an idea about how to add authentication to your web framework, you should usually
# not write these types of decorators yourself. # For Flask, you can use the Flask-Login
# extension instead, which adds more security and functionality.