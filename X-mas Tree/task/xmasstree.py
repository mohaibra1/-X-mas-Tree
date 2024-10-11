tree = []
outside = []
def print_tree(length):
   sp = length.split()
   length = int(sp[0])
   interval = int(sp[1])
   times = 1
   space = length - 1
   top = length - 1
   bottom = length - 2
   if interval > 0:
      print(f"{' '*top}X")
      increment = 0
      position = 1
      for i in range(0,length):
         print(f'{' '*space}', end='')
         if times == 1:
            print('^')
         else:
            if interval == 1:
               if i == 0:
                  print(f'/', end='')
                  print('*' + '\\')
               else:
                  print(f'/', end='')
                  hol = times - 2
                  for j in range(hol):
                     if j % 2 != 0:
                        print(f'O', end='')
                        #increment += 1
                     else:
                        print(f'*', end='')
                  print('' + '\\')
            else:
               if i == 0:
                  print(f'/', end='')
                  print('*' + '\\')
               else:
                  print(f'/', end='')
                  hol = times - 2
                  for k in range(1,hol):
                     if position % 2  == 0 and increment % interval == 1:
                        print(f'O', end='')
                     else:
                        print(f'*', end='')
                     position += 1
                     if position % 2 == 0:
                        increment += 1
                  print('*' + '\\')

         times = times + 2
         space = space - 1
      print(f'{' '*bottom}| |')
def return_tree(length, interval):
   global tree, outside
   #sp = length.split()
   length = int(length)
   interval = int(interval)
   times = 1
   space = length - 1
   top = length - 1
   bottom = length - 2
   tree.append(['X'])
   outside.append(tree)
   if interval > 0:
      #print(f"{' '*top}X")
      increment = 0
      position = 1
      for i in range(0,length):
         #print(f'{' '*space}', end='')
         if times == 1:
            #print('^')
            tree.append(['^'])
            outside.append(tree)
         else:
            if interval == 1:
               if i == 0:
                  #print(f'/', end='')
                  tree.append('/')
                  #print('*' + '\\')
                  tree.append('*')
                  tree.append('\\')
                  outside.append(tree)
               else:
                  #print(f'/', end='')
                  small = ['/']
                  hol = times - 2
                  for j in range(hol):
                     if j % 2 != 0:
                        #print(f'O', end='')
                        small.append('O')
                        #increment += 1
                     else:
                        #print(f'*', end='')
                        small.append('*')

                  #print('' + '\\')
                  small.append('\\')
                  tree.append(small)
                  outside.append(tree)
            else:
               if i == 0:
                  #print(f'/', end='')
                  tree.append('/')
                  #print('*' + '\\')
                  tree.append('*')
                  tree.append('\\')
                  outside.append(tree)
               else:
                  #print(f'/', end='')
                  small = ['/']
                  hol = times - 2
                  for k in range(1,hol):
                     if position % 2  == 0 and increment % interval == 1:
                        #print(f'O', end='')
                        small.append('O')
                     else:
                        #print(f'*', end='')
                        small.append('*')
                     position += 1
                     if position % 2 == 0:
                        increment += 1
                  #print('*' + '\\')
                  small.append('*')
                  small.append('\\')
                  tree.append(small)
                  outside.append(tree)
         times = times + 2
         space = space - 1
      #print(f'{' '*bottom}| |')
      tree.append(['|', '|'])
      outside.append(tree)


def postcard():
   outside1 = []
   for i in range(30):
      inside = []
      for j in range(50):
         if i == 0 or i == 29:
            inside.append('-')
         elif j == 0 or j == 49:
            inside.append('|')
         else:
            inside.append(' ')
      outside1.append(inside)
   outside1[27][20] = 'M'
   outside1[27][21] = 'e'
   outside1[27][22] = 'r'
   outside1[27][23] = 'r'
   outside1[27][24] = 'y'
   outside1[27][25] = ' '
   outside1[27][26] = 'X'
   outside1[27][27] = 'm'
   outside1[27][28] = 'a'
   outside1[27][29] = 's'
   return outside1

num = input('Enter the length of the Christmas tree:\n')
def postcard_with_decoration(row, col):
   row = int(row)
   col = int(col)
   for g in range(len(post)):
      for j in range(len(post[g])):
         if g == row and j == col:
            k = -1
            for o in tree:
               if len(o) > 2:
                  j -= k
               elif len(o) == 2:
                  j -= 1
               for l in o:
                  #if post[g][j] == ' ':
                  if len(o) > 2:
                     post[g][j] = l
                  elif len(o) == 2:
                     post[g][j] = l
                     j += 1
                  else:
                     post[g][j] = l
                  j += 1
               k += 1
               g += 1
               j = col
def chunkify(lst, y):
   return [lst[i::y] for i in range(y)]


n = num.split()
post = postcard()

if len(n) == 2:
   print_tree(num)
else:

   sp1 = num.split()
   p = zip(*chunkify(sp1,4))
   q = []
   for w in p:
      q.append(w)
   for f in range(len(q)):
      return_tree(q[f][0],q[f][1])
      postcard_with_decoration(q[f][2], q[f][3])

      tree = []
if len(n) > 2:
   for e in post:
      for u in e:
         print(u, end='')
      print()