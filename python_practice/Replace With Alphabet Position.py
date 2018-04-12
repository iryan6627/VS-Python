def alphabet_position(text):
    # numberList = []
    # text = text.lower()
    # for char in text:
    #     if char.isalpha():
    #         numberList.append(str(ord(char) - 96))
    #     else:
    #         continue
    # return " ".join(numberList)
    return " ".join(str(ord(char)-96) for char in text.lower() if char.isalpha())
print(alphabet_position("The sunset sets at twelve o' clock."))