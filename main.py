from get_words import get_words
from model.pre_process import pre_process


def main():
	gw = get_words()
	pr = pre_process()
	lng_input = input("please enter a langauge  (en / fa) : ")

	while lng_input.lower() not in ["en", "fa"]:
		lng_input = input("please enter a langauge : (en / fa)")

	text = input("please enter words : ")
	text = pr.process(text, lng_input)

	result = gw.get(text, lng_input)

	if result == 1:
		print("correct")

	else:
		print("		edit distance model		")
		for word, score in result["edit distance"].items():
			print(f"		word ----> {word} and score {score}")


		print("		jaccard similarity model		")
		for word, score in result["jaccard similarity"].items():
			print(f"		word ----> {word} and score {score}")

main()

