#Made By HarveyGW

def anagramchk(word,chkword):
  for letter in word:
    if letter in chkword:
      chkword = chkword.replace(letter,'',1)
    else:
      return 0
  return 1

wordin = input("Enter Anagram: ")

f=open('Dictionary.txt', 'r')
for line in f:
  line=line.strip()
  if len(line)>=3:
    if anagramchk(line,wordin):
      print(line)
f.close()


