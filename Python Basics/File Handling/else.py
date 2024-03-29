#We can use else as well
import sys
try :
  x = 5
  y=1
  result = x/y

except :
  exc_type, exc_value, exc_traceback = sys.exc_info()
  print("Some error happened" , exc_type)
else :
  print(result)
finally :
  print("I will be always executed")