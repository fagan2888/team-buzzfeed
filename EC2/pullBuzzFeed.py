
import urllib2
import json
import datetime

def getfeed (country, data):
    # GET API FEED
    webUrl = urllib2.urlopen(data)
    jsonfeed = "initialized"
    if webUrl.getcode() == 200:
        jsonfeed = webUrl.read()
    else:
        jsonfeed = "Received an error from server, cannot get feeds.\n"
    now = datetime.datetime.now()
    # DIRECTORY WHERE DATA FILES WILL BE STORED
    datapath = "./buzzfeeddata/"
    # WRITE FEED TO FILENAME CCYYYYMMDDHHMMSS, CC IS COUNTRY CODE
    todaydate = str(now.date())
    nowtime = str(now.time())
    feedfilename = str(todaydate) + str(nowtime)
    # CANNOT HAVE NON ALPHANUMERIC CHARACTERS IN FILENAME; REMOVE THEM
    feedfilename = feedfilename.replace("-","")
    feedfilename = feedfilename.replace("-","")
    feedfilename = feedfilename.replace(":","")
    # WE DON'T NEED MILLISECONDS FOR THE FILENAME; REMOVE IT.
    feedfilename = feedfilename.partition(".")[0]
    feedfilename = datapath + country + feedfilename + ".txt"
    f = open(feedfilename, "w")
    f.write(jsonfeed)
    f.close()



def main():
    urlData="https://www.buzzfeed.com/api/v2/feeds/trending?country=en-us"
    getfeed("us",urlData)
    urlData="https://www.buzzfeed.com/api/v2/feeds/trending?country=en-uk"
    getfeed("uk",urlData)
    urlData="https://www.buzzfeed.com/api/v2/feeds/trending?country=en-au"
    getfeed("au",urlData)
    urlData="https://www.buzzfeed.com/api/v2/feeds/trending?country=en-in"
    getfeed("in",urlData)
    urlData="https://www.buzzfeed.com/api/v2/feeds/trending?country=en-canada"
    getfeed("ca",urlData)


if __name__ == "__main__":
    main()
