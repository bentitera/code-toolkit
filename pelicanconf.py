#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import datetime as date


AUTHOR = 'Jacob Frias Koehler, PhD'
SITENAME = "Jacob's Blog"
SITEURL = ' '

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('My Website', 'www.dubmathematics.com'),)

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/jacob.koehler.503'),
          ('Instagram', 'https://www.instagram.com/dubmathematics/'),
          ('LinkedIn', 'https://www.linkedin.com/in/jacob-frias-koehler-phd-56627424/'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
MARKUP = ('md', 'ipynb')

PLUGIN_PATH = ['./plugins']
PLUGINS = ['ipynb/markup.py']
THEME = 'pelican-themes/aboutwilson'

#JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# Menu
# MENUITEMS = (
#     ('Categories', '/' + CATEGORIES_SAVE_AS),
#     ('Archive', '/' + ARCHIVES_SAVE_AS),
# )