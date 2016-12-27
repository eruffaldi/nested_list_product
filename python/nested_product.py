# TODO: replace itertools.product with something more numpy compatible
# similar to combivec of Matlabs
import itertools
import numpy as np

class Enum:
	"""Encapsulates an enumeration

	.name
	.fullname  full name in the generated list
	.index     in the generated list
	.values    values
	.children  dictionary with key=value from values, value= single Enum or [Enum]
	"""
	def __init__(self,name,values):
		self.name = name 
		self.index = 0
		self.fullname = ""
		self.values = values
		self.children = {} # by value
	def findvalue(self,value):
		"""Index of value in the list. Can be optimized"""
		for i,v in enumerate(self.values):
			if v == value:
				return i
		return -1
	def __repr__(self):
		return "Enum(%s,%d items)" % (self.name,len(self.values))

def gencases(spec_list):

	def mergelists(y):
		"""list of list of list => list of lists merging deepest"""
		r = [sum(l,[]) for l in y]
		return r

	def prods2mat(*args):
		# product creates an iteration of tuples, each with the content, that is a list
		# TODO replace with something more numpy compatible
		return np.array(mergelists(itertools.product(*args)),dtype=np.int32).transpose()

	def prod2mat(*args):
		# TODO replace with something more numpy compatible
		return np.array(list(itertools.product(*args)),dtype=np.int32).transpose()

	Y = prod2mat(*[range(0,len(x.values)) for x in spec_list])

	# make new list, to which we'll append the others
	sr = spec_list[:]
	for i,s in enumerate(spec_list):
		s.fullname = s.name
		s.index = i		
		for k,v in s.children.iteritems():
			# find all 
			j = s.findvalue(k)
			if j < 0:
				continue
			if isinstance(v,Enum):
				v = [v]
			rows = Y.shape[0]
			Yc,sc = gencases(v)

			# enlarge domain to accomodate vars
			prefix = s.fullname + "_%s_" % k
			for q,subspec in enumerate(sc):
				subspec.fullname = prefix + subspec.fullname
 				subspec.index = rows+q
 				sr.append(subspec)

			matching = Y[i,:] == j
			Yk = Y[:,matching]
			# product of: matching with Ya
			Yknew = prods2mat(Yk.transpose().tolist(),Yc.transpose().tolist())
			Ynk = Y[:,~matching]

			# re-assemble
			# YnotK   ,  YK repeated
			# -1      ,  YC			
			Ynk_nan = -np.ones((Yc.shape[0],Ynk.shape[1]))
			Ynk = np.concatenate((Ynk,Ynk_nan),axis=0) # append nan down
			Y = np.concatenate((Ynk,Yknew),axis=1) # first the matching 
	return Y,sr


if __name__ == '__main__':
	# testing
	c = Enum("case",["aug10","sim"])
	m = Enum("model",["zhu","young","pep"])

	vp = Enum("version",["original","svd","reorder"])
	m.children["pep"] = [vp]

	vpo = Enum("order",[1,2,3])
	vp.children["reorder"] = [vpo]

	vp = Enum("version",["pure","perfect"])
	m.children["young"] = [vp]

	r,rs = gencases([c,m])
	print r
	print r.shape
	print [(x.fullname,x.index) for x in rs]

	print gencases_alt([c,m])