
print 'testing url_feeder'

from aquire import url_feeder
feeder = url_feeder('sp500.csv')
i = 0
for site in feeder:
	i += 1
	if i > 1:
		break
	print site

print 'testing url_grabber'

from aquire import url_grabber
feeder = url_feeder('sp500.csv')
grabber = url_grabber()
i = 0
for site in feeder:
	i += 1
	if i > 1:
		break
	xml = grabber.retrieve(site)

print 'testing data_extractor'

from prune import data_extractor
extractor = data_extractor(feeder)
extractor.extract(xml[0])
