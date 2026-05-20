# removing punctuation from given string
import sys
import string
class PUNCTUATION:
  def __init__(self , a):
    try:
      self.a=a
    except Exception as e:
      er_t,er_m,er_l = sys.exc_info()
      print(f"Error in Line no : {er_l.tb_lineno} : Reason  : {er_m} :due to {er_t}")
  def remove_punctuations(self):
    try:
      c=''
      for i in self.a:
        if i not in string.punctuation: # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 
          c=c+i
      return c
    except Exception as e:
      er_t,er_m,er_l = sys.exc_info()
      print(f"Error in Line no : {er_l.tb_lineno} : Reason  : {er_m} :due to {er_t}")
try:
  aa=input('enter a text:')
  texts =PUNCTUATION(aa)
except Exception as e:
      er_t,er_m,er_l = sys.exc_info()
      print(f"Error in Line no : {er_l.tb_lineno} : Reason  : {er_m} :due to {er_t}")

print(texts.remove_punctuations())
""" OUT PUT:-
enter a text: data science *(&)*&^ and a*&&^i
 data science  and ai """
