Python driver 0.2.2 for ArangoDB 2.0.7
--------------------------

Driver for **ArangoDB REST API** inrerface, `arangodb.org <http://arangodb.org>`_

.. image:: https://travis-ci.org/joymax/arango-python.png?branch=master


Installation
************
::

  Download from repository

  wget https://github.com/appscluster/arango-python/archive/master.zip

  7z x master.zip ( if you don't have 7z : sudo apt-get install p7zip-full )

  cd arango-python-master

  python setup.py install


Usage
*****
To start work with **ArangoDB** try following example::

    from arango import create

    # create connection to database
    conn = create(db="test")
    conn.database.create()

    # create collection with name `test_collection`
    conn.test_collection.create()

    # create document
    conn.test_collection.documents.create({"sample_key": "sample_value"})

    # get first document
    doc = conn.test_collection.documents().first
    # get document body
    doc.body

    # get all documents in collection

    for doc in conn.test_collection.query.execute():
      print doc.id

To use **ArangoDB authentication via HTTP** try following example::

    from requests.auth import HTTPBasicAuth
    from arango.clients.requestsclient import RequestsClient
    from arango.core import Connection

    # Login to ArangoDB
    RequestsClient.config(auth=HTTPBasicAuth('arango_user', 'password'))

    # Connect to the appropriate DB 
    c = Connection(db="test", client=RequestsClient)
    c = c.collection
    c.test_collection.create()
    c.test_collection.documents.create({"key": "value"})

    # get first document
    doc = c.test_collection.documents().first
    # get document body
    doc.body

    # get all documents in collection
    for doc in c.test_collection.query.execute():
      print doc.id

For more details please read `Documentation <http://arangodb-python-driver.readthedocs.org/en/latest/>`_


Supported Python interpreters and versions:

 - cPython 3.3
 - cPython 2.7
 - PyPy 1.9

Supported **ArangoDB versions**: *1.4x*

Tested on **ArangoDB version**: *2.0.7*

Developed by `Maksym Klymyshyn <http://ua.linkedin.com/in/klymyshyn>`_

Forked by `Abdul Hamid <https://twitter.com/@appsclusterhub>`_

Changelog
*********

0.2.2
~~~~~~

 * Separated the use of the libraries available for opening URLs to use either PyCurl or Urllib2 and not to load both.

0.2.1
~~~~~~

 * Improved work with Edges
 * Added `not a variable` mode to `V()` (`~V()`)


0.2.0
~~~~~~

 * Added support for multiple databases


0.1.8
~~~~~~

 * Added support of **bulk inserts**
