from aa import ca
from datetime import datetime

PRIMARY_ARCHIVER = 'http://archiver.pri.diamond.ac.uk/archive/cgi/ArchiveDataServer.cgi'
PV = 'SR-DI-DCCT-01:SIGNAL'

fetcher = ca.CaFetcher(PRIMARY_ARCHIVER)

start = datetime(2016, 1, 2)
