## Develop May Month 2026 Calender Application Using OOPS
class CALENDER:
  def __init__(self , days,dayno):
    try:
      self.days=days
      self.dayno=dayno
    except Exception as e:
      er_t,er_m,er_l = sys.exc_info()
      print(f"Error in Line no : {er_l.tb_lineno} : Reason  : {er_m} :due to {er_t}")

  def DAY_NAME(self):
    try:
      if self.dayno > 31 or self.dayno <=0:
        return 'invalid number in date'
      else:
        f =self.dayno % 7
        return f'{self.dayno}-MAY-2026 is {self.days[f-1]}'
    except Exception as e:
      er_t,er_m,er_l = sys.exc_info()
      print(f"Error in Line no : {er_l.tb_lineno} : Reason  : {er_m} :due to {er_t}")
try:
  days=['Friday','Saturday','Sunday',"Monday","Tuesday",'Wednesday','Thursday']
  dayno=int(input('enter a day number between 1 to 31:'))
  first=CALENDER(days,dayno)
except Exception as e:
      er_t,er_m,er_l = sys.exc_info()
      print(f"Error in Line no : {er_l.tb_lineno} : Reason  : {er_m} :due to {er_t}")
print(first.DAY_NAME())



""" OUT PUT :-
enter a day number between 1 to 31:31
31-MAY-2026 is Sunday
"""
