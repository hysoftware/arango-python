'''
# temporarily disabled and RequestsClient.config used directly instead
from arango.core import Connection


def create(**kwargs):
    """Connection factory"""

    conn = Connection(**kwargs)

    return conn.collection

c = Connection()
collection = c.collection
'''