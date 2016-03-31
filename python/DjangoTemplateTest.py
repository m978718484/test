from django import template
from django.template import Template,Context
import datetime
from django.conf import settings 
settings.configure()

class Person(object):
	"""docstring for Person"""
	def __init__(self, first_name,last_name):
		super(Person, self).__init__()
		self.first_name = first_name
		self.last_name = last_name

d = datetime.date(2016,03,31)
t = Template('the month is {{ date.month }} and the year is {{ date.year }}. ')
c = Context({'date':d})
print t.render(c)

t = Template('Hello, {{ person.first_name }} {{ person.last_name.upper }}.')
c = Context({'person':Person('John','Smith')})
print t.render(c)

t = Template('{{ var }}--{{ var.upper }}--{{ var.isdigit }}')
c = Context({'var':'Hello'})
print t.render(c)
c = Context({'var':'12'})
print t.render(c)

t = Template('item 2 is {{ items.2 }}')
c = Context({'items':['0','1','2']})
print t.render(c)