import random

import CaesarCyphers

def encrypt():

  num = int(input("Please pick a number between 1 - 10: "))
  txt = input("Submit your text for encryption: ")

  nlist = []
  shiftFactor = 0
  for n in range(1,num):
    nlist.append(n)
    shiftFactor = random.choice(nlist)

  cypher_pos = []
  encrypt_S = []
  encrypt_Output = ""

  for letter in txt:
    pos = CaesarCyphers.primaryList.index(letter)
    cypher_pos.append(pos + shiftFactor)

  for n in cypher_pos:
    if len(str(n)) == 1:
      encrypt_S.append("0"+str(n))
    else:
      encrypt_S.extend([str(a) for a in str(n)])

  b = ""
  e = ""
  if len(str(shiftFactor)) == 1:
    b = "0"
    e = str(shiftFactor)[:1]
  else:
    b = str(shiftFactor)[:1]
    e = str(shiftFactor)[len(str(shiftFactor))-1:len(str(shiftFactor))]


  for x in encrypt_S:
    encrypt_Output += b
    encrypt_Output += str(x)
    encrypt_Output += e

  print(shiftFactor)
  print(b)
  print(e)
  print(cypher_pos)
  print(encrypt_S)
  print(encrypt_Output)