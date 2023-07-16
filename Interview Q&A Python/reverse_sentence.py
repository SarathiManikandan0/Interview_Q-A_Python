#Problem From Chat GPT
#Problem:
#Given a string containing a sentence, write a Python function to reverse the words in the sentence.

#Example:
#Input: "Hello World, how are you?"
#Output: "you? are how World, Hello"

def reverse_sentence(sentence):
    words = sentence.split()
    reversed_word = words[::-1]
    reversed_sentence = ' '.join(reversed_word)
    return reversed_sentence
#Test the Function
sentence = "Hello world, how are you"
reversed_sentence = reverse_sentence(sentence)
print(reversed_sentence)