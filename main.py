import CaesarCyphers

import CaesarCypher

CaesarCypher.encrypt()

input = "01205201201202201202201201201201207201206200220082003201201201204200720062"
## text: mission failed
## shiftFactor: 02
## cypher_pos: [15, 11, 21, 21, 11, 17, 16, 2, 8, 3, 11, 14, 7, 6]
## encrypt_S: ['1', '5', '1', '1', '2', '1', '2', '1', '1', '1', '1', '7', '1', '6', '02', '08', '03', '1', '1', '1', '4', '07', '06']
## encrypt_Output: 120520120120220120220120120120120720120620022008200320120120120420072006

code = []
pos = []
letter = ""
decrypt = 0
decode = ""

shiftFactor = ""
shiftFactor += input[:1]
shiftFactor += input[1:2]
shiftFactor = int(shiftFactor)

input = input[1:len(input)-1]

n = 2
code = [int(input[i:i+n]) for i in range(0, len(input), n)]

for num in code:
  num = int(num - shiftFactor)
  # decrypt = int([str(x) for x in num])
  # pos = CaesarCyphers.primaryList.index(decrypt)
  letter = str(CaesarCyphers.primaryList[num])
  decode += letter


print(code)
print(CaesarCyphers.primaryList)
print(pos)
print(letter)
print(decode)