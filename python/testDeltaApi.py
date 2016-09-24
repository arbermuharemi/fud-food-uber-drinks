import urllib2

def getFlightInfo():
	return urllib2.urlopen("https://demo30-test.apigee.net/v1/hack/status?flightNumber=1500&flightOriginDate=2016-09-25&apikey=ZINxBqol4GEAB9L1T25ZcFyG9vmapoLW").read()

print (getFlightInfo())