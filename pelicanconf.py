#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Muhammad Kaisar Arkhan'
SITENAME = u"Yuki's Boredom"
SITEURL = 'https://yukiisbored.github.io/'

PATH = 'content'

TIMEZONE = 'Asia/Jakarta'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SOCIAL = (
    ('twitter', 'https://twitter.com/yuki_is_bored'),
    ('telegram', 'https://telegram.me/yuki_is_bored'),
    ('github', 'https://github.com/yukiisbored'),
    ('gitlab', 'https://gitlab.com/yuki_is_bored')
)

PROFILE_IMG_URL = 'https://avatars2.githubusercontent.com/yukiisbored?&s=300'

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["asciidoc_reader", "org_reader"]

ORG_READER_EMACS_LOCATION = "/usr/bin/emacs"

THEME = 'pure-single'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
