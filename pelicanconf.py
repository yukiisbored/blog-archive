#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Muhammad Kaisar Arkhan'
SITENAME = u"Yuki's Boredom"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Jakarta'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('coala DevOps', 'https://solar.coala.io'),
         ('Loklak', 'https://loklak.org'),
         ('Planet coala', 'https://blog.coala.io'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/yuki_is_bored'),
          ('Github', 'https://github.com/yukiisbored'),)

#DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["asciidoc_reader"]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
