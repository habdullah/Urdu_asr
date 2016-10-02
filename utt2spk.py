lst = ['ammama','hammad','hamza','hina','laraib','rida','tehreem']

f = open('tsst.txt','w')
for i in range (1,31):
	t = open(str(i)+'.txt','r')
	f.write(lst[0]+'1_'+str(i)+' '+t.readline()+'\n')
# for i in range (1,31):
# 	f.write(lst[1]+'1_'+str(i)+' '+lst[1]+'1\n')
# for i in range (1,31):
# 	f.write(lst[2]+'1_'+str(i)+' '+lst[2]+'1\n')	
# for i in range (1,31):
# 	f.write(lst[3]+'1_'+str(i)+' '+lst[3]+'1\n')
# for i in range (1,31):
# 	f.write(lst[4]+'1_'+str(i)+' '+lst[4]+'1\n')
# for i in range (1,31):
# 	f.write(lst[5]+'1_'+str(i)+' '+lst[5]+'1\n')
# for i in range (1,31):
# 	f.write(lst[6]+'1_'+str(i)+' '+lst[6]+'1\n')
#with open('4.txt') as f:
  # while True:
  #   c = f.read(1)
  #   if not c:
  #     print "End of file"
  #     break
  #   #print ("Read a character:"+ c) 
  #   if c == '0'

# file = open('4.txt' , "r")
# q='\xd8';q=q.encode('utf8')
# w='\xdb';w=w.encode('utf8')
# e='\xd8';e=e.encode('utf8')

# text = [word.strip(qwe) for line in file for word in line.lower().split()]
# print(text)
f.close()

