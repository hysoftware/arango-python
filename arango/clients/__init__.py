import sys
import logging
logging.basicConfig()

__all__ = ("Client",)

ISPY3 = sys.version_info >= (3, 0)

logger = logging.getLogger("arango.clients")

if ISPY3 is False:
    try:
        from .pycurlclient import PyCurlClient
        Client = PyCurlClient
    except ImportError:
        try:
            logger.warning(u"PyCurl not available, trying Urllib2. %s", str(e))
            from .urllib2client import Urllib2Client
            Client = Urllib2Client
        except ImportError:
            logger.warning(u"Urllib2 not available. %s", str(e))
    except Exception as e:
        logger.warning(u"No library available for opening URLs. %s", str(e))
else:
    try:
        from .urllib2client import Urllib2Client
        Client = Urllib2Client
    except ImportError:
<<<<<<< HEAD
        logger.warning(u"Urllib2 not available. %s", str(e))
=======
        logger.warning(u"Urllib2 not available. %s", str(e))
>>>>>>> 73964918896a8bee82f15757c4e2a712ff38eadb
