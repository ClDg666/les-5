
fil_obj = open("001.txt", 'w')

while True:
    a = input('>>>')
    if a == ' ':
        fil_obj.close()
        break
    else:
        fil_obj.write(a)
