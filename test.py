def hmily(nb_petals):
  
  l = ['I love you', "a little", "a lot", "passionately" ,"madly", "not at all"]
  return l[(nb_petals % len(l))]


print(hmily(0))