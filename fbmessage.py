import fbchat
from getpass import getpass
username = input("Username: ")
client = fbchat.Client(username,getpass())
question = input("Do you want to send an image?[Y/N]") #whether to send an image or text as message
if question == "N": #For sending text
	no_of_friends = int(input("Number of friends: "))
	for i in range(no_of_friends):
		name = input("Enter friend's name: ")
		friends = client.searchForUsers(name) #Searches your friend list for the name you entered
		friend = friends[0]
		print("enter your message here:")
		msg = input() 
		sent = client.sendMessage(msg,friend.uid) #message sent
		if sent:
			print("Message has been sent successfully.!")
else: #for sending image
	no_of_friends1 = int(input("Number of friends: "))
	for i in range(no_of_friends1):
		name = input("Enter friend's name: ")
		friends = client.searchForUsers(name)
		friend = friends[0]
		st = input("Enter the path of the image: ") #local path of the image file to be sent
		sent = client.sendLocalImage(st,message="This is sent from cmd via python script",thread_id=friend.uid)
		if sent:
			print("Image has been sent successfully!")
