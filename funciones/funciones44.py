
def consecutivo(listb):
 cons= 0
 v=0
 for item in range (1,len(listb)):
  a=listb[item]
  b=listb[item-1]
  c=a-b
  if c==1 and item<len(listb):
   v=v+1
  else:
   if v>cons:
    cons=v
    v=1
 return(cons)