import sys
class DICTIONARY:
  def __init__(self,a):
      self.a =a
  def frequency_check(self):
    try:
      frequency ={}
      for i in self.a:
        frequency[i]=self.a.count(i)
      print(frequency)
    except Exception as e:
      er_t,er_m,er_l = sys.exc_info()
      print(f"Error in Line no : {er_l.tb_lineno} : Reason  : {er_m} :due to {er_t}")
try:
  didd=DICTIONARY(input('enter a string what you want for frequency:'))
  didd.frequency_check()
except Exception as e:
      er_t,er_m,er_l = sys.exc_info()
      print(f"Error in Line no : {er_l.tb_lineno} : Reason  : {er_m} :due to {er_t}")
"""
OUT PUT:-
enter a string what you want for frequency:"data science and ai"
{'"': 2, 'd': 2, 'a': 4, 't': 1, ' ': 3, 's': 1, 'c': 2, 'i': 2, 'e': 2, 'n': 2} """
