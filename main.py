from learningClass import learning

if __name__ == '__main__':
  new1 = learning(start=0, stop=20, count=6)
  new1.print_list()
  print(new1.half_list())
  new1.comparison_list()

  new = learning(start=0, stop=20, count=5)
  new.print_list()
  print(new.half_list())
  new.comparison_list()





