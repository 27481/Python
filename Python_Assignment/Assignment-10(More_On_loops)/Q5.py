def fun(string):
	st=set();
	for i in range(len(string)//2):
		st.add(string[i])

	if len(string)>1:
		return "YES"
	else: 
	    return "NO";



t=int(input())

while (t>0):
	string =input("")
	t=t-1
	print(fun(string))