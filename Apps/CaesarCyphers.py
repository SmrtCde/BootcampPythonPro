import string

sp = list(" ")
low = list(string.ascii_lowercase)
up = list(string.ascii_uppercase)
dig = list(string.digits)
pun = list(string.punctuation)

primaryList = (sp+low+up+dig+pun)

sList = [' ','j', '1', 'x', '^', '0', '9', '|', 'Z', 'c', '.', 'H', '$', 'k', '<', 'e', 'm', 'C', 'R', '_', '"', '3', 'v', '>', '{', 'U', 'n', 'l', 'K', 'D', ']', 'z', '~', '&', '-', 'N', 'g', 'E', 'o', 'h', '\\', '!', 'Q', ',', '`', ':', '[', '=', 'P', 'X', 'w', '7', 'Y', 'J', 'I', '}', 'd', 'p', 'O', 'i', "'", 'u', 'W', 'S', '(', 'F', '*', 'M', 'A', '@', 'L', '#', 'G', 'B', 't', 'r', '+', '/', '%', 'a', 'y', 'q', ')', 'V', 's', '4', '?', '5', '8', 'T', '6', ';', '2', 'b', 'f']

tList = ['A', 'p', 'd', 'n', '/', 'l', 'c', '%', 'r', 'e', '9', 'a', 's', '3', ';', 'o', '&', 'C', '_', 'F', 'S', '+', '.', '#', 'Z', '!', '^', 'x', 'U', ')', 'E', 'z', 'y', 't', '"', 'u', '$', ':', 'K', ' ', 'q', '(', '|', '0', 'L', '1', 'T', 'V', 'i', 'P', '-', ',', 'f', 'B', 'g', '2', 'h', 'j', '[', '<', "'", 'k', 'M', '}', 'R', 'N', '{', 'Y', 'W', '7', 'b', '*', '`', ']', '5', 'w', '>', 'Q', '~', '@', '?', 'H', 'D', '=', '6', 'I', 'G', 'm', 'X', '8', '\\', 'v', 'J', '4', 'O']

qList = ['x', 'X', '@', 's', "'", 'd', '{', 'Y', 'z', 'b', '(', 't', 'i', '=', '3', 'c', ';', ')', ']', 'P', 'H', '.', 'f', '!', 'k', 'Q', 'G', '#', 'm', 'R', '<', '5', 'A', 'B', '>', 'a', 'J', '2', 'h', '6', 'e', ' ', 'M', 'I', '$', 'O', '9', '*', 'V', ':', 'T', ',', '?', 'v', '+', '"', 'K', 'U', '%', '8', '`', '4', 'F', 'E', 'Z', 'y', 'r', '-', 'D', '0', 'o', 'g', '^', '}', 'N', 'n', 'w', 'u', '&', '|', '~', 'C', '/', 'l', '\\', 'j', '7', 'W', '1', 'S', 'q', '_', 'L', 'p', '[']

# secondaryIndex = []
# for pos in secondaryList:
#   secondaryIndex.append(secondaryList.index(pos))

def comp (a):
  z =[]
  y = [int(x) for x in a]
  z.append(y)
  return z