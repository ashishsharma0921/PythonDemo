import webapp2
from google.appengine.ext.webapp.util import run_wsgi_app
import os
from google.appengine.ext.webapp import template
import helloworld

import sys
from google.appengine.ext import ndb
from google.appengine.ext.remote_api import remote_api_stub
from gcloud import datastore





# from oauth2client import client

# try:
# #     sdk_path = 'C:\Program Files (x86)\Google\google_appengine'
# #     sys.path.insert(0, sdk_path)
#     sys.path.append('C:\Program Files (x86)\Google\google_appengine')
#     sys.path.append('C:\Program Files (x86)\Google\google_appengine\lib\yaml\lib')
#     if 'google' in sys.modules:
#         del sys.modules['google']
#      
#     import dev_appserver
#     
#     dev_appserver.fix_sys_path()
# except ImportError:
#     print('Please make sure the App Engine SDK is in your PYTHONPATH.')
#     raise


class Login(webapp2.RequestHandler):
    
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'login.html')
        self.response.out.write(template.render(path, template_values))
        
        
    def post(self):
        f = self.request.get('firstName')
        l = self.request.get('lastName')
        query = helloworld.Employee.query(helloworld.Employee.firstName == f)
        employees =  query.fetch()
        for employee in employees:
            print(employee.firstName)
        print("all printed")
#         remote_api_stub.ConfigureRemoteApiForOAuth(
#                                                    '{}.appspot.com'.format('demo11-1147'),
#                                                    '/_ah/remote_api')
        client = datastore.Client("demo11-1147")
        key = client.key('Person')
        
        entity = datastore.Entity(key=key)
        entity['name'] = f
        entity['age'] = 25
        client.put(entity)
            
            
        