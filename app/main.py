punctuation = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
vowels = ["a", "e", "i", "o", "u"]
accentuation = [
  ["á", "â"], 
  ["é", "ê"], 
  ["í", "î"], 
  ["ó", "ô"], 
  ["ú", "û"]
]

def rename(name:str):
  name = name.lower()
  return removePunctuation(name)

def removePunctuation(name:str):
  name = name.replace("ç", "c")
  name = name.replace("à", "a")
  name = name.replace("ã", "a")
  name = name.replace("õ", "o")
  name = name.replace("ª", "a")
  name = name.replace("º", "o")
  name = name.replace("°", "gr")
  for i in range(len(punctuation)):
    name = name.replace(punctuation[i], " ")
  for i in range(5):
    for j in range(2):
      name = name.replace(accentuation[i][j], vowels[i])
  return transformVector(name)

def transformVector(name:str):
  name = name.split()
  return rewrite(name)

def rewrite(name:list):
  newName = ""
  for i in range(len(name)):
    newName += name[i] + "-"
  newName = newName[:-1]
  return newName
