DESIRED_SUM = 12

class Solver:

  def __init__(self, data = None): 
    '''konstruktor, self.data i self.cnt ustawiane na None, zeby w przyszlosci wylapac brak tych struktur'''
    self.data = data
    self.cnt = None
	

  def save_input(self):
    '''pilnujemy tego, aby ta metoda wywowała się co najwyżej raz'''
    if self.data is not None:
      return 

    #f = open('example.txt', "r")
    #full_file_content = f.read()
    #self.data = eval(full_file_content)
    self.data = eval(input('podaj liste (np. [1, 2, 3]): '))



  def set_cnt(self):
    '''pilnujemy tego, aby dane wejsciowe zostaly wczesniej pobrane'''
    if self.data is None:
      self.save_input()

    self.cnt = [0 for i in range(DESIRED_SUM + 1)]
    for e in self.data:
      self.cnt[e] += 1


  def set_result(self):
    '''pilnujemy, aby lista self.cnt zostala wczesniej wyliczona'''
    if self.cnt is None:
      self.set_cnt()

    self.result = []  
    for e0 in range(DESIRED_SUM // 2 + 1):
      e1      = DESIRED_SUM - e0
      min_cnt = min(self.cnt[e0], self.cnt[e1]) 
      loops   = min_cnt if e0 != e1 else self.cnt[e0] // 2
      for i in range(loops):
        self.result.append([e0, e1]) 

	
  def get_solved(self):
    '''jesli nie chcemy robic na piechote, to po prostu klikamy te metode i ona robi wszystko za nas'''
    self.set_result()
    return self.result
		

if __name__ == '__main__':  
  print(*Solver().get_solved(), sep = ', ')


