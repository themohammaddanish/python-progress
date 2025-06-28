# Encoding Part
st = input("Enter a sentence to encode: ")
words = st.split(" ")
coding = True

if coding:
    nwords = []
    for word in words:
        if len(word) >= 3:
            ran1 = "sfs"
            ran2 = "568"
            stnew = ran1 + word[1:] + word[0] + ran2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    encoded_sentence = " ".join(nwords)
    print("Encoded Sentence:", encoded_sentence)

# Decoding Part
decoding = input("Do you want to decode the sentence? (yes/no): ").lower()

if decoding == "yes":
    decoded_words = []
    for word in encoded_sentence.split():
        if word.startswith("sfs") and word.endswith("568"):
            middle = word[3:-3]  # remove 'sfs' and '568'
            original = middle[-1] + middle[:-1]  # last char to front
            decoded_words.append(original)
        else:
            decoded_words.append(word[::-1])
    decoded_sentence = " ".join(decoded_words)
    print("Decoded Sentence:", decoded_sentence)
