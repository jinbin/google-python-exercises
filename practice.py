
s = "hello"

def main():
    print mix_up("hello", "world")

def fix_start(s):
  store = []
  result = []
  for index in range(len(s)):
    if s[index] in store:
      result.append("*")
    else:
      result.append(s[index])
      store.append(s[index])

  return result

def mix_up(a, b):
  pre_a = a[0] + a[1]
  pre_b = b[0] + b[1]

  after_a = a[2:len(a)]
  after_b = b[2:len(b)]

  return pre_b + after_a + " " + pre_a + after_b

def verbing(s):
  if len(s) < 3:
    return s
  elif s.endswith("ing"):
    return s + "ly"
  else:
    return s + "ing"

def not_bad(s):
  try:
    index_not = s.index("not")
  except ValueError:
    index_not = -1

  try:
    index_good = s.index("bad")
  except ValueError:
    index_good = -1

  if index_not != -1 and index_good != -1 and index_not < index_good:
    print index_good
    print index_not
    return s.replace(s[index_not:index_good+3], "good")
  else:
    return s

def front_back(a, b):
  if len(a) % 2 == 0:
    a_middle = len(a)/2 - 1
  else:
    a_middle = len(a)/2

  if len(b) % 2 == 0:
    b_middle = len(b)/2 - 1
  else:
    b_middle = len(b)/2

  return a[0:a_middle+1] + b[0:b_middle+1] + a[a_middle+1:len(a)] + b[b_middle+1:len(b)]

def assign_list():
  a = ["a", "b"]
  b = a
  b[0] = "c"
  print a

def match_ends(words):
  num = 0
  for word in words:
    if(len(word) >= 2 and word[0] == word[1]):
      num += 1
  return num

def front_x(words):
  x_list = []
  list = []
  for word in words:
    if word.startswith("x"):
      x_list.append(word)
    else:
      list.append(word)

  x_list.sort()
  list.sort()
  return x_list + list

if __name__ == "__main__":
    a = ["a", "b", "b", "c"]
    del a[1]
    print a






