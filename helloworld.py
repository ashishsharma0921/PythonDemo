# from google.appengine.ext import webapp
import cgi

from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.ext.webapp.util import run_wsgi_app
import webapp2
import json
import login
import threading


import os
from google.appengine.ext.webapp import template


class Employee(ndb.Model):
    firstName = ndb.StringProperty()
    lastName = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)
#     _config_cache = None
#     _config_lock = threading.Lock()

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))
#         self.response.headers['Content-Type'] = 'text/plain'
#         self.response.out.write('Hello, webapp2 World!')
    
    def post(self):
        f = self.request.get('firstName')
        l = self.request.get('lastName')
        a = os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/')
        Employee(firstName=f, lastName= l).put()
        





application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/login', login.Login)
    
], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
