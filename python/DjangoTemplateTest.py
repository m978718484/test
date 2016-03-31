from django import template
from django.template import Template,Context
import datetime
from django.conf import settings 
settings.configure()

d = datetime.date(2016,03,31)
t = Template('the month is {{ date.month }} and the year is {{ date.year }}.')
c = Context({'date':d})
print t.render(c)

print 'asdf'

class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
