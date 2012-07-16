Django RST Bug
--------------

1. In django.contrib.admindocs.utils module, comment out the line

   docutils.parsers.rst.roles.DEFAULT_INTERPRETED_ROLE = 'cmsreference'
