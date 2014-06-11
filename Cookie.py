n = int(input("n = "))

for i in range(n):
      s = input().split()
      C, F, X = float(s[0]), float(s[1]), float(s[2])

      taxa_cogumelos = 2
      tempo_total = 0

      cond = False
      while not cond:
            t1 = (X-C)/taxa_cogumelos
            t2 = X/(taxa_cogumelos+F)

            if t2 < t1:
                  tempo_total += C/taxa_cogumelos
                  taxa_cogumelos += F
            else:
                  tempo_total += X/taxa_cogumelos
                  cond = True

      print("Case #{}: {} ".format(i+1, tempo_total))
