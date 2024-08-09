string = "Of the bitterness that falls to the lot of humanity, there was no part which Christ did not taste. There were those who tried to cast contempt upon Him because of His birth, and even in His childhood He had to meet their scornful looks and evil whisperings. If He had responded by an impatient word or look, if He had conceded to His brothers by even one wrong act, He would have failed of being a perfect example. Thus He would have failed of carrying out the plan for our redemption. Had He even admitted that there could be an excuse for sin, Satan would have triumphed, and the world would have been lost. This is why the tempter worked to make His life as trying as possible, that He might be led to sin."
reference = "(White, E.G, DA, page 88, paragraph 2)"


strlist = string.split(" ")
firstLetterOnly = []

for s in strlist:
  letter = s[0]
  if "." in s:
     letter = letter + ". "
  firstLetterOnly.append(letter)
  
newstring = ""
for l in firstLetterOnly:
   newstring = newstring + l + " "
print(newstring)
print()
referencesplit = reference.split(",")
referencestring = ""
for r in referencesplit:
  numberofcharacters = len(r)
  spaces = ""
  for x in range(0, numberofcharacters):
     spaces = spaces + "_"
  referencestring = referencestring + spaces + " "
print(referencestring)  