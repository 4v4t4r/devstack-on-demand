__author__ = 'barakme'

from ravello_sdk import *
import os
import time

USERNAME = os.environ["RAVELLO_USERNAME"]
PASSWORD = os.environ["RAVELLO_PASSWORD"]
BP_ID = os.environ["RAVELLO_BP_ID"]

print "Connecting to Ravello Cloud"
client = RavelloClient(username=USERNAME, password=PASSWORD)

print "Verifying Blueprint"
bp = client.get_blueprint(BP_ID)

if bp is None:
    print "Blueprint not found"
    exit(1)

app = {}
app["name"] = "api-test4"
app["baseBlueprintId"] = BP_ID

print "Creating Application"
new_app = client.create_application(app)

new_id = new_app["id"]

print "Publishing Application"
client.publish_application(new_id, {})

print "Sleeping for 5 seconds"
time.sleep(5)

current_app = client.get_application(new_id)
fqdn = current_app["design"]["vms"][0]["networkConnections"][0]["ipConfig"]["fqdn"]

print "FQDN: %s" % fqdn
