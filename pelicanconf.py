#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#
# About the site
#
AUTHOR = u'Marianne Maertens, Guillermo Aguilar, and Rebecca Hesse'
SITENAME = u'Ethikkommission - Fakultät IV -  TU Berlin'
SITETITLE = u'Ethik-Kommission'
SITESUBTITLE = u'der Fakultät IV'
SITEURL = 'ethikkommission.eecs.tu-berlin.de'

FAVICON = SITEURL + '/img/favicon.ico'

TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = u'en'
LOCALE = u'en_US.UTF-8'

MAIN_MENU = True

#
# Configure Pelican a bit
#
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [ 'sitemap']
SITEMAP = { 'format': 'xml' }

DIRECT_TEMPLATES = ['404'] # unset all templates; add 404
THEME = 'theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#
# Configure the site
#
STATIC_PATHS = ['img', 'files']
MENUITEMS = (('Information', 'index.html'),
             ('Unterlagen', 'unterlagen.html')
)

DEFAULT_PAGINATION = False

# We prefer document-relative URLs
RELATIVE_URLS = True

CACHE_CONTENT = False
