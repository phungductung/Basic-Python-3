f1 = open("F:\Learning Python\Basic Python\Basic Python 2\words.txt","r")
line_num = 0
search_phrase_1 = "tum"
print("SEARCHING FOR tum...")
for line in f1.readlines():
    line_num += 1
    if line.find(search_phrase_1) >= 0:
        print(line_num, line) 
f1.close()
print("--------------------------------------------")
f2 = open("F:\Learning Python\Basic Python\Basic Python 2\words.txt","r")
print("SEARCHING FOR sne...")
line_num_2 = 0
search_phrase_2 = "sne"
for line in f2.readlines():
    line_num_2 += 1
    if line.startswith(search_phrase_2) == 1:
        print(line_num_2, line) 
f2.close()
print("--------------------------------------------")
f3 = open("F:\Learning Python\Basic Python\Basic Python 2\words.txt","r")
search_phrase_3 = "-"
num = 0
for line in f3.readlines():
    if (line.count(search_phrase_3)) > 1:
       num +=1
print ("More than 1 hyphen:",num)
f3.close()
print("--------------------------------------------")
f4 = open("F:\Learning Python\Basic Python\Basic Python 2\words.txt","r")
a = f4.readlines()
maxlen = len(a[0])
for line in a: 
    if (len(line) > maxlen):
        maxlen = len(line)
print("Max length:",maxlen)
f4.close()