from __future__ import unicode_literals

from pkg_resources import get_distribution, DistributionNotFound
from .builders import JSONTOCHTMLBuilder

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    __version__ = None

def setup(app):
    app.add_builder(JSONTOCHTMLBuilder)
    return {'version': __version__, 'parallel_read_safe': True}
