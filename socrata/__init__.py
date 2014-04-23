from pickle_warehouse import Warehouse

from socrata.download import download as _download

__version__ = '0.0.1'

def metadata(domain, directory):
    'Generate metadata about datasets.'
    warehouse = Warehouse(directory)
    yield from download(warehouse, domain)
