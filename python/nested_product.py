import itertools
import numpy as np

class Spec:
	def __init__self(name,values):
		self.name = name
		self.index = 0
		self.fullname = name
		self.values = values
		self.children = {} # by value
	def findvalue(self,value):
		pass


def gencases(spec_list):

	a = np.array(product(*[range(0,len(x.values)) for x in spec_list]),type=np.int32)
	return a


if __name__ == '__main__':
	# testing
	c = Spec("case",["aug10","sim"])
	m = Spec("model",["khu","yun","young","pep"])
	print gencases([c,m])