# add your code here
encryption_characters = {"a": "f",
              "b": "g",
              "c": "h",
              "d": "i",
              "e": "j",
              "f": "k",
              "g": "l",
              "h": "m",
              "i": "n",
              "j": "o",
              "k": "p",
              "l": "q",
              "m": "r",
              "n": "s",
              "o": "t",
              "p": "u",
              "q": "v",
              "r": "w",
              "s": "x",
              "t": "y",
              "u": "z",
              "v": "a",
              "w": "b",
              "x": "c",
              "y": "d",
              "z": "e"}

def encryption(text):
    text = text.lower()
    text = [*text]
    index_text = 0
#     print(encryption_characters)
    for i in text:
        if i in encryption_characters:
            text[index_text] = encryption_characters[i]
            index_text += 1
    text = ''.join(text)
    return text

main_sentence = input("Please enter a sentence: ")
main_sentence = main_sentence.split()
encrypted_sentence = []
for i in main_sentence:
    encrypted_sentence.append(encryption(i))
es_answer = ' '.join(encrypted_sentence)

print("The encrypted sentence is: " + f"{es_answer}")
