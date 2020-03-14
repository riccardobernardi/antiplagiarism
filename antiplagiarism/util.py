import os
from pygraham import *
import hashlib

files = dict({})

def helper(x, grams):
	with open(x, "r", encoding='utf-8') as ff:
		files[x] = set()
		count = 0
		s = ""
		for i in ff:
			try:
				i = i.replace(" ","").replace(",","")
				files[x].add(hashlib.md5(i.encode('utf-8')).hexdigest())
			except:
				print("error of codec in: ", x)
			s += i
			count += 1
			if count == grams:
				try:
					files[x].add(hashlib.md5(s.encode("utf-8")).hexdigest())
				except:
					print("error of codec in: ", x)
				s = list(s.split("\n")[1:]).reduce(lambda x,y: IF(x=="", x+y,x+"\n"+y ))
				count-=1


def jaccard(x, u):
	try:
		return len(x[1] & u[1]) / len(x[1] | u[1])
	except:
		return 0


def antiplagiarism(path="", type=".c", grams=2,threshold=0):
	if path == "":
		list(os.listdir("./")).filter(lambda x: type in x).map(lambda x: helper(x, grams))
	else:
		list(os.listdir(path)).filter(lambda x: type in x).map(lambda x: helper(path + "/" + x, grams))
	exited = set()

	m = files.map(lambda x: files.filter(lambda m: m[0] != x[0]).next(lambda k: exited.add(x[0])).filter(
		lambda f: f[0] not in exited).map(lambda u: (x[0], u[0], jaccard(x, u))).filter(lambda x: x[2] > threshold).map(
		lambda x: x[0].split("/")[-1] + " == " + x[1].split("/")[-1] + " --> " + str(round(x[2] * 100, 2)) + "%"))

	for i in m:
		for j in i:
			print(j)