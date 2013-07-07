class Sample(object):
	def run(self):
		pass

class ReturnMultipleValues(Sample):
	"""Python can return multiple values"""
	def returnMultipleValues(self):
		return ("apples", "oranges", "pears", "watermelons")

	def run(self):
		fruit1, fruit2, fruit3, fruit4 = self.returnMultipleValues()
		print fruit1, fruit2, fruit3, fruit4
		fruits = self.returnMultipleValues()
		print fruits;

class VariableArguments(Sample):
	"""Python stores variable arguments as list and variable name/value pairs as maps"""
	def varargs(self, msg, *fruits, **animals):
		print msg, fruits, animals

	def run(self):
		self.varargs("2 variable args & 0 variable map:", "apple", "pears")
		self.varargs("2 variable args & 1 variable map:", "apple", "pears", cat='lion')
		self.varargs("2 variable args & 2 variable map:", "apple", "pears", cat='lion', fish=('tuna', 'catfish'))

class DefaultArguments(Sample):
	"""Python supports default arguments"""
	def log(self, msg, component='unknown component'):
		print component + ": " + msg

	def run(self):
		self.log("Some message")
		self.log("Some message", "Washer machine")

class AutoVariableArgumentExpansion(Sample):
	"""Python automatically expands variables from list & maps and pass them into methods"""
	def expand(self, greeting, person):
		print greeting, person

	def run(self):
		values = ("Hello", "Hal")
		self.expand(*values)
		values = {'person': "Hal", 'greeting': 'What is up?'}
		self.expand(**values)

# Enumerates throught the classes
for clazz in Sample.__subclasses__():
    sample = clazz()
    print sample.__doc__
    sample.run()
    print "*" * 60
