st = input("enter the word you want: ")
words = st.split(" ")
coding = True
if(coding):
  nwords = []
  for word in words:
    if(len(word)>=3):
      ran1 = "sfs"
      ran2 = "568"
      stnew = ran1 + word[1:] + word[0] + ran2
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))