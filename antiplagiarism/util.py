import os
from pygraham import *
import hashlib

files = dict({})

def helper(x, grams):
	with open(x, "r") as ff:
		files[x] = set()
		count = 0
		s = ""
		for i in ff:
			files[x].add(hashlib.md5(i.encode("utf-8")).hexdigest())
			s += i
			count += 1
			if count == grams:
				files[x].add(hashlib.md5(s.encode("utf-8")).hexdigest())
				s = list(s.split("\n")[1:]).reduce(lambda x,y: IF(x=="", x+y,x+"\n"+y ))
				count-=1


def jaccard(x, u):
	try:
		return len(x[1] & u[1]) / len(x[1] | u[1])
	except:
		return 0


def antiplagiarism(s="", type=".c", grams=2):
	if s == "":
		list(os.listdir("./")).filter(lambda x: type in x).map(lambda x: helper(x, grams))
	else:
		list(os.listdir(s)).filter(lambda x: type in x).map(lambda x: helper(x, grams))
	exited = set()
	files.map(lambda x: files.filter(lambda m: m[0] != x[0]).next(lambda k: exited.add(x[0])).filter(
		lambda f: f[0] not in exited).map(lambda u: (x[0], u[0], jaccard(x, u))).map(
		lambda x: x[0] + " == " + x[1] + " --> " + str(round(x[2] * 100, 2)) + "%").next(lambda x: print(x)))
