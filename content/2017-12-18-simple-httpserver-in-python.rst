:title: Simple HTTPServer in Python
:slug: simple-httpserver-in-python
:tags: oss, python
:category: OSS
:date: 2017-12-18
:Status: published

.. note::

    This is an article for `鰻 Advent Calendar 2017
    <https://adventar.org/calendars/2628>`_.

-----

Every time I'd like to use a http server in development such as
checking generated HTML documentation files, I need to google how to
do it. So I post a blog as a memorandum.

`Python2`_
==========

::

  $ python -m SimpleHTTPServer [PORT]
  # default port is 8000
  Serving HTTP on 0.0.0.0 port 8000 ...

`Python3`_
==========

::

  $ python3 -m http.server [PORT]
  # default port is 8000
  Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...


.. _Python2: https://docs.python.org/2/library/simplehttpserver.html
.. _Python3: https://docs.python.org/3/library/http.server.html

Happy Hacking!
