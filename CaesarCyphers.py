import string

sp = list(" ")
low = list(string.ascii_lowercase)
up = list(string.ascii_uppercase)
dig = list(string.digits)
pun = list(string.punctuation)

primaryList = (sp+low+up+dig+pun)

secondaryList = [' ','j', '1', 'x', '^', '0', '9', '|', 'Z', 'c', '.', 'H', '$', 'k', '<', 'e', 'm', 'C', 'R', '_', '"', '3', 'v', '>', '{', 'U', 'n', 'l', 'K', 'D', ']', 'z', '~', '&', '-', 'N', 'g', 'E', 'o', 'h', '\\', '!', 'Q', ',', '`', ':', '[', '=', 'P', 'X', 'w', '7', 'Y', 'J', 'I', '}', 'd', 'p', 'O', 'i', "'", 'u', 'W', 'S', '(', 'F', '*', 'M', 'A', '@', 'L', '#', 'G', 'B', 't', 'r', '+', '/', '%', 'a', 'y', 'q', ')', 'V', 's', '4', '?', '5', '8', 'T', '6', ';', '2', 'b', 'f']

secondaryIndex = []
for pos in secondaryList:
  secondaryIndex.append(secondaryList.index(pos))

def comp (a):
  z =[]
  y = [int(x) for x in a]
  z.append(y)
  return z