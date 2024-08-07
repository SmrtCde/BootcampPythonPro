import Apps.CaesarCyphers

# inp = inp("Enter submission: ")
# inp = "0h.ii.qrF 8.-}O2"

def decrypt(a):
  # inp = a
  true = []
  code = []
  cList = []
  encryptC = []
  bList = []
  encryptB = []
  aList = []
  encryptA = []
  decode = []
  encrypt = str(a)
  shiftFactor = 4
  decrypt = ""

  # shiftFactor += inp[:1]
  # shiftFactor += inp[len(inp)-1:len(inp)]
  # shiftFactor = int(shiftFactor)

  # encrypt = inp[1:len(inp)-1]

  for num in encrypt:
    code.append(num)

  for c in code:
    x = Apps.CaesarCyphers.primaryList.index(c)
    cList.append(x)
    encryptC.append(Apps.CaesarCyphers.qList[x])

  for c in encryptC:
    x = Apps.CaesarCyphers.tList.index(c)
    bList.append(x)
    encryptB.append(Apps.CaesarCyphers.sList[x])

  for b in encryptB:
    x = Apps.CaesarCyphers.primaryList.index(b)
    aList.append(x)
    s = round(x - shiftFactor)
    true.append(s)
    decode = [Apps.CaesarCyphers.primaryList[t] for t in true]

  decrypt = ("".join(decode))

  return print(f"Your decrypted text is:\n\n {decrypt}")