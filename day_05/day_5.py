from collections import defaultdict

def parse_input(input_text):
   rules_text, updates_text = input_text.strip().split("\n\n")
   
   rules = []
   for line in rules_text.split("\n"):
      before, after = map(int, line.split("|"))
      rules.append((before, after))
    
   updates = []
   for line in updates_text.split("\n"):
      pages = list(map(int, line.split(",")))
      updates.append(pages)
        
   return rules, updates


def get_middle_number(pages):
    return pages[len(pages) // 2]

def problem_1():
   with open('day_05/input_5.txt', 'r') as f:
      input_text = f.read()
      rules, updates = parse_input(input_text)
      sum = 0
    
      for update in updates:
         valid = True
         for i in range(len(update)-1):
            if (update[i], update[i+1]) not in rules:
               valid = False
               break
         if valid:
            sum += get_middle_number(update)
   
   return sum

def problem_2():
   with open('day_05/input_5.txt', 'r') as f:
      input_text = f.read()
      rules, updates = parse_input(input_text)
      sum = 0

      for update in updates:
         wrong = False
         while True:
            changed = False
            for r1, r2 in rules:
               try:
                  idx1, idx2 = update.index(r1), update.index(r2)
                  if idx1 > idx2:
                     update[idx1], update[idx2] = update[idx2], update[idx1]
                     changed, wrong = True, True
               except ValueError:
                  continue
            if not changed:
               break

         if wrong:
            sum += get_middle_number(update)

      return sum




   



