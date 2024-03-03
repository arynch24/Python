#If exception doesn't happen
#Catching the exception type
import sys
try :
  x = 5
  y=1
  result = x/y
  print(result)
except :
  exc_type, exc_value, exc_traceback = sys.exc_info()
  print("Some error happened" , exc_type)