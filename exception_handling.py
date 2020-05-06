try :
	f = open('file.txt','rb')
	if f.name == 'file.txt':
		raise Exception # You can raise Manual Exception handling
	#var = new_var
except FileNotFoundError as f:
	#print(f)
	print("Sorry! file is not found") #custom output for the exception
except Exception as e:
 	#print(e)
 	print("Sorry, the variable is not found")
else : #Runs when try block does not raise an exception
 	print(f.read())
 	f.close()
finally : #runs regardless of what happened in try block, It is executed to free up the resources
	print("This is finally block which runs regardless of what happened in try block")