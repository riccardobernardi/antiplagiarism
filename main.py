from antiplagiarism.util import antiplagiarism


def main():
	print(antiplagiarism(path = "/Users/rr/PycharmProjects/antiplagiarism", type=".c", grams=2,threshold=0.1))

if __name__ == "__main__":
	main()
