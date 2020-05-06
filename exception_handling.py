try :
	f = open('file_.txt','rb')
except FileNotFoundError as e:
	print("Sorry! file is not found") #custom output for the exception
except Exception as e:
 	print(e)
