#Catching the exception type
import sys
try :
  x = 5
  y=0
  result = x/y
  print("Exception ke baad ki dosti")
  print(result)
except :
  exc_type, exc_value, exc_traceback = sys.exc_info()
  print("Some error happened" , exc_type)
  print(exc_value)
  print(exc_traceback)
