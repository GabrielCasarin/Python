with open("teste.txt", "r") as f:
      T = int(f.readline())
      for i in range(T):
            r1 = int(f.readline())
            t1 = [[int(k) for k in f.readline().split()] for j in range(4)]
            r2 = int(f.readline())
            t2 = [[int(k) for k in f.readline().split()] for j in range(4)]
            #candidatos = [el for el in t1[r1-1] if el in t2[r2-1]]
            candidatos = set(t1[r1-1]).intersection(set(t2[r2-1]))
            if not candidatos:
                  print("Case #{i}: Volunteer cheated!".format(**locals()))
            elif len(candidatos) == 1:
                  print("Case #{0}: {1}".format(i, next(iter(candidatos))))
            else:
                  print("Case #{i}: Bad magician!".format(**locals()))
