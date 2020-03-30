#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'ethikkommission.eecs.tu-berlin.de'
RELATIVE_URLS = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

STATIC_PATHS = ['img', 'files', 'extra']
#STATIC_PATHS = ['img', 'extra/CNAME', 'files']
EXTRA_PATH_METADATA = {'extra/favicon.ico': {'path': 'favicon.ico'},
					   'extra/favicon-16x16.png': {'path': 'favicon-16x16.png'}
						}

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
