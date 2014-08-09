Python driver 0.2.3 for ArangoDB 2.1.1
--------------------------

Driver for **ArangoDB REST API** inrerface, `arangodb.org <http://arangodb.org>`_

.. image:: https://travis-ci.org/hysoftware/arango-python.svg?branch=master
    :target: https://travis-ci.org/hysoftware/arango-python


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
    import sys
    
    def ARDBconnect():
        try:
            # Prepare Login for ArangoDB
            RequestsClient.config(auth=HTTPBasicAuth('arango_user', 'password'))
            # Login for ArangoDB
            db = Connection(db="test", client=RequestsClient)
            # Connect to the appropriate DB 
            arango = db.version
            print 'Connected to ArangoDB version: ', arango.version
            return db
        except Exception, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
            sys.exit(1)
    
    # Create ArangoDB connection handle        
    c = ARDBconnect()
    c = c.collection
    
    # Create a new collection
    c.test_collection.create()
    # Add a document to the collection
    c.test_collection.documents.create({"key": "value"})

    # get first document
    doc = c.test_collection.documents().first
    # get document body
    doc.body

    # get all documents in collection
    for doc in c.test_collection.query.execute():
      print doc.id

To **change or reset** arangodb **user** account **password**::

    # In terminal run
    arangosh
    
    # For improving security its a good idea to change the root account password
    # Once in arangosh run the following commands
    users = require("org/arangodb/users");
    users.update("root", "the_new_password", true);
    users.reload();
    
    quit
    
    # restart arangodb
    /etc/init.d/arangodb restart
    

To enable arangodb **authentication** change the following 2 config files::

    # 1. > /etc/arangodb/arangob.conf
    [server]
    disable-authentication = false

    # 2. > /etc/arangodb/arangod.conf
    # disable authentication for the admin frontend
    disable-authentication = no
    
    # restart arangodb for changes to take effect
    /etc/init.d/arangodb restart

For more details please read `Documentation <http://arangodb-python-driver.readthedocs.org/en/latest/>`_


Supported Python interpreters and versions:

 - cPython 3.3
 - cPython 2.7
 - PyPy 1.9

Supported **ArangoDB versions**: *1.4x*

Tested on **ArangoDB version**: *2.0.7, 2.1.0 and 2.1.1*

Developed by `Maksym Klymyshyn <http://ua.linkedin.com/in/klymyshyn>`_

Forked by `Abdul Hamid <https://twitter.com/@appsclusterhub>`_

Changelog
*********

0.2.3
~~~~~~

 * default initialisation temporarily disabled and used RequestsClient.config directly instead. 
 * Added exception handling for status code 401 authentication failure to ArangoDB

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
