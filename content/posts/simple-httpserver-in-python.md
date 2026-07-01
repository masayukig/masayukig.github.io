---
title: Simple HTTPServer in Python
date: '2017-12-18T00:00:00+09:00'
slug: simple-httpserver-in-python
categories:
- OSS
tags:
- oss
- python
draft: false
disqus_identifier: 2017-12-18-simple-httpserver-in-python
cover:
  image: /images/covers/oss.png
  alt: Simple HTTPServer in Python
---

> This is an article for [鰻 Advent Calendar 2017](https://adventar.org/calendars/2628).

-----

Every time I'd like to use a http server in development such as
checking generated HTML documentation files, I need to google how to
do it. So I post a blog as a memorandum.

## [Python2](https://docs.python.org/2/library/simplehttpserver.html)

```
$ python -m SimpleHTTPServer [PORT]
# default port is 8000
Serving HTTP on 0.0.0.0 port 8000 ...
```
## [Python3](https://docs.python.org/3/library/http.server.html)

```
$ python3 -m http.server [PORT]
# default port is 8000
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```
Happy Hacking!
