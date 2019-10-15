from aa.js import JsonFetcher
from datetime import datetime
from tzlocal import get_localzone
import matplotlib as dnp

tz = get_localzone()


ArchiverBessy = 'archiver.bessy.de'
CurrentBessy = 'TOPUPCC:rdCur'


start = tz.localize(datetime(2019, 5, 2,14))

end = tz.localize(datetime(2019, 5, 2, 15))

jfetcher_Bessy = JsonFetcher(ArchiverBessy,80)


#eventBessy = jfetcher_Bessy.get_values(CurrentBessy, start, end,1,{'firstFill':60})
eventffBessy = jfetcher_Bessy.get_values(CurrentBessy, start, end, binning_params={'firstFill':60})
eventBessy = jfetcher_Bessy.get_values(CurrentBessy, start, end)
#plot1 = dnp.pyplot.


event = jfetcher_Bessy.get_event_at(CurrentBessy, start)

print(event.value)


#data = fetcher._get_values(PV, start, end)

print (eventBessy)