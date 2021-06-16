word = "butts are for pooping, butts"
words = word.split()
fonz = "happy thanks giving pilgrims"
fonzer = fonz.split()
someting = "grape juice do it"


emptyList = []
while True:
    wants = input("What would you like?\n")
    if wants.lower() == "done":
        break
    else:
        emptyList.append(wants)

for t in fonzer:
    for buns in emptyList:
        if buns.lower() in someting.lower():
            print(buns)

# print(emptyList)