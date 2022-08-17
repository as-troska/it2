

tall1 = input("Skriv inn tall 1: ")

while True:
    if (tall1.isnumeric()):
        tall1 = int(tall1)
        break
    else:
        tall1 = input("Skriv inn tall 1: ")


# tall2 = input("Skriv inn tall 2: ")

# while True:
#     try:
#         tall2 = int(tall2)
#     except:
#         tall2 = input("Skriv inn tall 2: ")
#     else:
#         break


def svaret():
    tall2 = input("Skriv inn tall 2: ")

    try:
        tall2 = int(tall2)
    except:
        svaret()
    else:
        tall2 = int(tall2)
        return tall2    

tall2 = svaret()

svar = tall1 + tall2

print(svar)