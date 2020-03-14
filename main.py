from antiplagiarism.util import antiplagiarism


def main():
	result = antiplagiarism(path = "/Users/rr/PycharmProjects/antiplagiarism", type=".c", grams=2,threshold=0.1)
	for i in result:
		print(i)

if __name__ == "__main__":
	main()
