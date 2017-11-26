#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

AUTHOR = u'Masayuki Igawa'
#SITENAME = u'What is essential is invisible to the eye'
SITENAME = u"What's done is done"

SITEURL = 'https://igawa.io'
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = ('%Y-%m-%d')

# ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
# ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'

DISQUS_SITENAME = 'afterstack'

# Feed generation is usually not desired when developing
FEED_DOMAIN = 'https://igawa.io'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

THEME = '../pelican-themes/pelican-bootstrap3'
DISQUS_DISPLAY_COUNTS = True
# https://github.com/DandyDev/pelican-bootstrap3/issues/219
# DISQUSURL = 'http://afterstack.net'
# DISQUS_URL = 'http://afterstack.net'

CC_LICENSE = 'CC-BY'
TWITTER_CARDS = True
TWITTER_USERNAME = 'masayukig'
TWITTER_WIDGET_ID = '650189654373724160'
ADDTHIS_PROFILE = 'masayukig'

SOCIAL = (('Twitter', 'https://twitter.com/masayukig'),
          ('LinkedIn', 'https://www.linkedin.com/in/masayukig'),
          ('GitHub', 'https://github.com/masayukig'),
          ('Flickr', 'https://flickr.com/masayun'),
          ('Instagram', 'https://instagram.com/masayukig'),)

ABOUT_ME = '<a href="https://about.me/masayukig">about.me</a>'
#DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
RECENT_POST_COUNT = True
LINKS = (('Python.org', 'http://python.org/'),
        ('OpenStack.org', 'http://openstack.org/'),)
#BOOTSTRAP_FLUID = True
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['related_posts', 'tag_cloud', 'i18n_subsites', ]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}


CUSTOM_CSS = 'static/custom.css'
# Tell Pelican to add 'extra/custom.css' to the output dir
STATIC_PATHS = ['images', 'extra/custom.css']
# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'}
}
SHOW_ARTICLE_AUTHOR = True

DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_TAGS_ON_SIDEBAR = True

# https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3
GOOGLE_ANALYTICS_UNIVERSAL = 'UA-4773446-12'
GOOGLE_ANALYTICS_UNIVERSAL_PROPERTY = 'auto'
