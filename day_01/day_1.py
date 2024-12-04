def problem_1():
   l1 = []
   l2 = []
   difs = 0
   with open('day_01/input_1.txt', 'r') as f:
      for line in f:
         num = line.split()
         l1.append(num[0])
         l2.append(num[1])

      l1.sort()
      l2.sort()
      for i in range(len(l1)):
         difs += abs(int(l1[i]) - int(l2[i]))
   f.close()
   return difs

def problem_2():
   l1 = []
   l2 = []
   difs = 0
   with open('day_01/input_1.txt', 'r') as f:
      for line in f:
         num = line.split()
         l1.append(num[0])
         l2.append(num[1])

      l1.sort()
      l2.sort()
      for c in range(len(l1)):
         difs += l2.count(l1[c]) * int(l1[c])
   f.close()
   return difs