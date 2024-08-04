  import random

  import CaesarCyphers

  # def encrypt():

  num = int(input("Please pick a number between 1 - 9: "))
  txt = input("Submit your text for encryption: ")

  shiftFactor = 0

  nlist = []
  true = []
  cypherPos = []
  encryptA = []
  encryptB = []
  encryptC = []
  encryptS = []
  aList = []
  bList = []
  cList = []
  encryptOutput = ""
  b = ""
  e = ""

  for n in range(1, num):
    nlist.append(n)
    shiftFactor = random.choice(nlist)

  for letter in txt:
    pos = CaesarCyphers.primaryList.index(letter)
    true.append(pos)
    s = pos * int(shiftFactor)
    aList.append(s)
    encryptA = [CaesarCyphers.primaryList[x] for x in aList]

  for a in encryptA:
    pos = CaesarCyphers.sList.index(a)
    bList.append(pos)
    encryptB = [CaesarCyphers.tList[x] for x in bList]

  for b in encryptB:
    pos = CaesarCyphers.qList.index(b)
    cList.append(pos)
    encryptC = [CaesarCyphers.primaryList[x] for x in cList]

  if len(str(shiftFactor)) == 1:
    b = "0"
    e = str(shiftFactor)[:1]
  else:
    b = str(shiftFactor)[:1]
    e = str(shiftFactor)[len(str(shiftFactor)) - 1:len(str(shiftFactor))]

  encryptOutput += b
  for x in encryptC:
    encryptOutput += str(x)
  encryptOutput += e

  print(f"\nText: {txt}")
  print(f"\nshiftFactor: {shiftFactor}")
  print(f"\nb value {b}")
  print(f"\ne value {e}")
  print(f"\ntrue: {true}")
  print(f"\naList: {aList}")
  print(f"\nencryptA: {encryptA}")
  print(f"\nbList: {bList}")
  print(f"\nencryptB: {encryptB}")
  print(f"\ncList: {cList}")
  print(f"\nencryptC: {encryptC}")
  print(f"\nencryptOutput: {encryptOutput}")