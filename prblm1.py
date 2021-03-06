# def word_potential(stmnt):
#     """proggram to arrange a sentence in a way that their potential
#     will be in increading order"""
#     terminators = (",", ".", "?", "!")
#     if stmnt.endswith(terminators):
#         stmnt = stmnt[0:-1]
#         list_of_word = stmnt.split()
#         word_potential = {}
#         for word in list_of_word:
#             potential = 0
#             frequency = list_of_word.count(word)
#             for char in word:
#                 potential += ord(char)
#             word_potential[potential] = (word, frequency)
#     else:
#         return "Invalid Statement"

#     keys = list(word_potential.keys())
#     keys.sort()
#     finalstmnt = ""
#     print(f"word | potential")
#     for key in keys:
#         for _ in range(word_potential[key][-1]):
#             print(f"{word_potential[key][0].ljust(10)}{key}")
#             finalstmnt += " "+word_potential[key][0]
#     return finalstmnt.lstrip()


# # statement = input("Enter a statement")
# statement = "LOOK BEFORE YOU LEAP."
# fs = word_potential(statement)
# print(f"\nOUTPUT \n{fs}")


from functools import reduce


def strength(w): return reduce(lambda x, y: x + y, w)


statement = "HOW DO YOU DO?"
if statement.endswith(("?", "!", ",", ".")):
    reqstatement = [(word, strength([ord(c) for c in word]))
                    for word in statement[:-1].split(" ")]
    reqstatement.sort(key=lambda x: x[1])
    [print(f"{r[0]}  {r[1]}") for r in reqstatement]
    [print(f"{r[0]}", end=' ') for r in reqstatement]
