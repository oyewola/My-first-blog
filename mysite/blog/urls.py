# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 06:50:14 2017

@author: Yinka
"""

from	django.conf.urls	import	url
from	.	import	views

urlpatterns	=	[
         url(r'^$',	views.post_list,	name='post_list'),

]