import keyboard

delay = int(input("enter delay(in ms): "))/1000
key = input("enter the key: ")

def start():
	print("press ctrl+c for quit")
	while True:
		keyboard.press(key)

print("press 'y' for start")
if (keyboard.read_key() == "y"):
	start()