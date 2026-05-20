#### Find the Palindrome of Above numbers
import sys
class PALINDROME:
  def __init__(self , a):
    self.a =a
    
  def check_pali(self):
    try:
      for i in self.a:
        num = temp=i
        rev = 0
        while num >0:
          re = num % 10
          rev = rev *10 + re
          num //=10
        if temp == rev :
          print(f'{temp} is palindrom')
        else:
          print(f'{temp} is not palindrom')
    except Exception as e:
      er_t,er_m,er_l = sys.exc_info()
      print(f"Error in Line no : {er_l.tb_lineno} : Reason  : {er_m} :due to {er_t}")
try:
  check=PALINDROME([101 , 135 , 129 , 284,6,222])
  check.check_pali()
except Exception as e:
      er_t,er_m,er_l = sys.exc_info()
      print(f"Error in Line no : {er_l.tb_lineno} : Reason  : {er_m} :due to {er_t}")

"""
OUT PUT:-
101 is palindrom
135 is not palindrom
129 is not palindrom
284 is not palindrom
6 is palindrom
222 is palindrom """
