
print 'testing url_feeder'

from aquire import url_feeder
feeder = url_feeder('sites.txt')
for site in feeder:
	print site

print 'testing url_grabber'

from aquire import url_grabber
feeder = url_feeder('sites.txt')
grabber = url_grabber()
for site in feeder:
	html = grabber.retrieve(site)
	print len(html)

print 'testing data_extractor'

from prune import data_extractor
extractor = data_extractor(feeder)
extractor.extract(html)
