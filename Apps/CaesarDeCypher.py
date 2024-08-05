import CaesarCyphers

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
    x = CaesarCyphers.primaryList.index(c)
    cList.append(x)
    encryptC.append(CaesarCyphers.qList[x])

  for c in encryptC:
    x = CaesarCyphers.tList.index(c)
    bList.append(x)
    encryptB.append(CaesarCyphers.sList[x])

  for b in encryptB:
    x = CaesarCyphers.primaryList.index(b)
    aList.append(x)
    s = round(x - shiftFactor)
    true.append(s)
    decode = [CaesarCyphers.primaryList[t] for t in true]

  decrypt = ("".join(decode))

  return (
  # print(f"\ninp: {inp}")
  # print(f"\ncode: {code}")
  # ,print(f"\ncList: {cList}")
  # ,print(f"\nencryptC: {encryptC}")
  # ,print(f"\nbList: {bList}")
  # ,print(f"\nencryptB: {encryptB}")
  # ,print(f"\naList: {aList}")
  # ,print(f"\nencryptA: {encryptA}")
  # ,print(f"\ntrue: {true}")
  # ,print(f"\ndecode: {decode}")
  print(f"\ndecrypt: {decrypt}")
  )