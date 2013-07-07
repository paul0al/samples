
import re
import sys
import string

class Challenge(object):
    """Abstract class"""

    URL_PREFIX='http://www.pythonchallenge.com/pc/def/'

    def solution(self):
        pass

# how to define constant variables
class Challenge00(Challenge):
    def solution(self):
        print self.URL_PREFIX + str(2 ** 38) + '.html'

class Challenge01(Challenge):
    def solution(self):
        print self.URL_PREFIX + self.optimalSolution("map") + '.html'

    def attempt1(self):
        for i in range(len(input)):
            if(ord(input[i]) >= ord('a') and ord(input[i]) <= ord('z')):
                sys.stdout.write( chr(ord('a') + (ord(input[i]) - ord('a') + 2) % 26) ) 
            else:
                sys.stdout.write(input[i])
        print ""

    def optimalSolution(self, input):
        translationTable = string.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')
        return string.translate(input, translationTable)

class Challenge02(Challenge):
	def solution(self): 
		print self.URL_PREFIX + self.optimalSolution('/Users/someone/Desktop/python/challenge02.input') + '.html'

	def optimalSolution(self, filepath):
		count={}
		# catch exception if file not found
		file = open(filepath, 'r')
		for line in file:
			for char in line:
				if(count.get(char)):
					count[char] = 1 + count.get(char)
				else: 
					count[char] = 1
		file = open(filepath, 'r')
		result = ''
		for line in file:
			for char in line:
				if(count.get(char) == 1):
					result += char
		return result

class Challenge03(Challenge):
	def solution(self): 
		print self.URL_PREFIX + self.optimalSolution() + '.php'

	def optimalSolution(self):
		regex="[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]"
		file = open('/Users/someone/Desktop/python/challenge03.input').read()
		return ''.join(re.findall(regex, file))

	def attempt02(self):
		file = open('/Users/someone/Desktop/python/challenge03.input')
		for line in file:
			result = re.findall(regex, line)
			if(len(result) > 0):
				print(result)

	def attempt01(self):
		file = open('/Users/someone/Desktop/python/challenge03.input')
		currentLine = ""
		for line in file:
			currentLine += line.strip().upper()
			for i in range(len(currentLine) - 6):
				if(isSameChar(currentLine, i, 1)):
				   	print currentLine[i+3]
			currentLine = currentLine[len(currentLine) - 6:]

	def isSameChar(data, startIndex, increment): 
		if(increment == 3):
			return isSameChar(data, startIndex, increment + 1)
		elif(increment <= 6):
			return (data[startIndex] == data[startIndex + increment]) and isSameChar(data, startIndex, increment + 1)
		return True

# Enumerates throught the classes
for clazz in Challenge.__subclasses__():
    challenge = clazz()
    challenge.solution()

# Returns the docstring for Challenge
print Challenge.__doc__
