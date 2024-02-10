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
  return remove_punctuation(name)

def remove_punctuation(name:str):
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
  return transform_vector(name)

def transform_vector(name:str):
  name = name.split()
  return rewrite(name)

def rewrite(name:list):
  new_name = ""
  for i in range(len(name)):
    new_name += name[i] + "-"
  new_name = new_name[:-1]
  return new_name
