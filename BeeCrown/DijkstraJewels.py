# -*- coding: utf-8 -*-
## End of File Error: https://www.altcademy.com/blog/what-is-an-eof-error-in-python/#:~:text=Handling%20an%20EOFError%20is%20similar,action%20when%20an%20EOFError%20occurs.

## CODE FULLY WORKING ##

jewel = []
try: #try until theres a EOFerror 
  while (n := input()): # Its seems like attribuying the value n here at the while it's more quick
    jewel.append(n)
except: #EOFerror
    pass
uniqueJewels = set(jewel)
print(len(uniqueJewels))


