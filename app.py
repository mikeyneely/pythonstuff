def greatest_sib(n):
  #convert n into a list of strings
  n = list(str(n)) 
  #assign a var for the numerically sorted, reversed list
  finaln = n.sort(key = int, reverse = True)
  #bring it back together as an interger
  print ("".join(n))
  #dont ever play ya self, call yo function
greatest_sib(3495837101)