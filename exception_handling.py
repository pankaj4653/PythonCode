try :
	f = open('file.txt','rb')
	var = new_var
except FileNotFoundError as f:
	#print(f)
	print("Sorry! file is not found") #custom output for the exception
except Exception as e:
 	#print(e)
 	print("Sorry, the variable is not found")

