#imports the required librarys if it fails saying can't import then do "pip install requests" and "pip install json" from the command line
import requests, json
from datetime import datetime
url = "http://ip-api.com/json" #Enter the web address before the "#"
jsonfilename = "./Test " + str(datetime.now().date()) + ".json" #enter the name of the jsonfile
Authentication = "" #Enter the Authentication Key before the "#"
#creates the web request using HTTP GET this can be changed to by replacing requests.get to requests.post see http://docs.python-requests.org/en/master/ for more details
r = requests.get(url) #auth = Authentication
#checks to see if it was a success
if r.status_code == 200:
    #creates the json file to store data 
    with open(jsonfilename, "w" ) as f:
        #Write data to the file 
        f.write(json.dumps(r.json()))
else:
    print("Error with web request response: " + str(r.status_code))