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
num = input('Enter the length of the Christmas tree:\n')

print_tree(num)

