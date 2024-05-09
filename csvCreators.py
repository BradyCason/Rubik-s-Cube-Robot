import csv
import copy

with open("plls1.csv", "r") as csvFile:
    reader = csv.DictReader(csvFile)
    algs = [x for x in reader]
    for alg in algs:
        alg["alg"] = eval(alg["alg"])


with open("plls2.csv", "w") as newCsvFile:
    writer = csv.DictWriter(newCsvFile, fieldnames=["pattern","alg"])
    writer.writeheader()
    writer.writerow(algs[0])
    for i in range(1,len(algs)):
        if (i-1) % 4 == 0 or (i-1) % 4 == 2:
            writer.writerow(algs[i])
        elif (i-1) % 4 == 1:
            writer.writerow({"pattern":algs[i]["pattern"],"alg":algs[i+2]["alg"]})
        else:
            writer.writerow({"pattern":algs[i]["pattern"],"alg":algs[i-2]["alg"]})

# allAlgs = []
# for alg in algs:
#     allAlgs.append(alg)
#     alg1 = copy.deepcopy(alg)
#     alg1["pattern"] = alg1["pattern"][3:] + alg1["pattern"][0:3]
#     newAlg = []
#     for move in alg1["alg"]:
#         if "r" in move:
#             move = move.replace("r","b")
#         elif "b" in move:
#             move = move.replace("b","l")
#         elif "l" in move:
#             move = move.replace("l","f")
#         elif "f" in move:
#             move = move.replace("f","r")
#         newAlg.append(move)
#     alg1["alg"] = newAlg
#     allAlgs.append(alg1)
    
#     alg2 = copy.deepcopy(alg1)
#     alg2["pattern"] = alg2["pattern"][3:] + alg2["pattern"][0:3]
#     newAlg = []
#     for move in alg2["alg"]:
#         if "r" in move:
#             move = move.replace("r","b")
#         elif "b" in move:
#             move = move.replace("b","l")
#         elif "l" in move:
#             move = move.replace("l","f")
#         elif "f" in move:
#             move = move.replace("f","r")
#         newAlg.append(move)
#     alg2["alg"] = newAlg
#     allAlgs.append(alg2)

#     alg3 = copy.deepcopy(alg2)
#     alg3["pattern"] = alg3["pattern"][3:] + alg3["pattern"][0:3]
#     newAlg = []
#     for move in alg3["alg"]:
#         if "r" in move:
#             move = move.replace("r","b")
#         elif "b" in move:
#             move = move.replace("b","l")
#         elif "l" in move:
#             move = move.replace("l","f")
#         elif "f" in move:
#             move = move.replace("f","r")
#         newAlg.append(move)
#     alg3["alg"] = newAlg
#     allAlgs.append(alg3)
# print(allAlgs)


# with open("plls1.csv", "w") as newCsvFile:
#     writer = csv.DictWriter(newCsvFile, fieldnames=["pattern","alg"])
#     writer.writeheader()
#     for alg in allAlgs:
#         writer.writerow(alg)




    #     for alg in algs:
    #         # Make 4 new algs:

    #         # Rotate 0 times, 

    #         writer.writerow(alg)

# newAlgs = []
# for alg in algs:
#     moves = alg["algorithm"].split(" ")
#     newMoves = []
#     for move in moves:
#         move = move.replace("(", "")
#         move = move.replace(")", "")
#         move = move.casefold()
#         newMoves.append(move)
#     newAlgs.append({"pattern":alg["pattern"], "alg":newMoves})

# with open("olls.csv", "w") as csvFile:
#     writer = csv.DictWriter(csvFile, fieldnames=["pattern","alg"])
#     writer.writeheader()
#     for alg in newAlgs:
#         writer.writerow(alg)
        
