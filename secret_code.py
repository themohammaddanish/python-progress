st = input("enter the word you want: ")
coding = True
if(coding):
  if(len(word)>=3):
    ran1 = "sfs"
    ran2 = "568"
    word_new = ran1 + word[1:] + word[0] + ran2
    print(word_new)