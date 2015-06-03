Pycachu
=======

A tool to provide a LRU cache on files.

It has been created to store gigabytes of Thumbor thumbnails on a DigitalOcean server.

Usage
~~~~~

.. code-block::

   from pycachu import Pycachu

   # Initialize the cache
   # The dir has to exist
   p = Pycachu('/storage/pycachu', 20 * (1024 ** 3))

   # Get a file
   f = p.get('/some/file')

   if f is not None:
       yield f
       f.close()
   else:
       content = generate_file_content()
       p.put('/some/file', content)
       content.seek(0)
       yield content
       content.close()


Performance
~~~~~~~~~~~

The performance is not exceptional, but operations basically take a constant time independently of
the number of files in the cache, which is not too bad.

Rough benchmarking gave about 170 get per second.
