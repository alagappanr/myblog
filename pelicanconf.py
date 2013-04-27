#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Alagappan'
SITENAME = u"Alagappan's Weblog"
SITEURL = 'http://alagappan.co.in'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('_alagappan', 'http://twitter.com/_alagappan'),
          ('About', 'http://about.me/alagappanr'),
          )

# Social widget
SOCIAL = (('Facebook', 'http://facebook.com/alagappan.r'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 3

TYPOGRIFY = True

FEED_DOMAIN = SITEURL
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

OUTPUT_PATH = '../../myblog/'

THEME = "pelican-svbtle"
AUTHOR_BIO = "Software Developer, Traveller, Explorer, Runner, Trekker, Avid Reader, Amateur Photographer, NIT Trichy Alum, Weekend Foodie, Investing time/money in dreams, experiences and self."
