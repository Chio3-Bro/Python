from tkinter import *
import time

root = Tk()
 
clicks = 0
cmd_list = 'Commands:\n1.--------ddos--------,\n2.--------ipv4--------,\n3.-------kill_pc--------,\n4.--------mac--------,\n5.--------logger--------'
mac = '34-55-33-45-FD-46'

root['bg'] = 'black'
root.title('Hack login')
root.geometry('300x150')

def click_button():
	global clicks
	clicks +=1
	if clicks == 1:
		print('User logged in the system...')
	root.destroy()
	print('Enter his username:')
	uname = input()
	print(cmd_list)
	print('Enter func:')
	func = input()

	if func == 'logger':
		print('#> Func KeyLogger is paid! You have to donate or input code')
		print('#> Do u want to enter code?[y/n]:')
		sure5 = input()
		if sure5 == 'y':
			print('#> Enter here')
			ip = input()
			if ip == '#> 164-643-8413-8521-4265':
				print('#> Reboot pc and go more)')
			else:
				print('#> sorry bro :(')
		if sure5 == 'n':
			print('#> Processes are stopped, you can close window')

	if func == 'mac':
		print('#> MAC of the victim is: ' + mac )
		print('#> Do u want to continue(c-continue, d-close):')
		sure4 = input()
		if sure4 == 'c':
			print('#> Commands ' + cmd_list)
			print('#> Restart and choose another commands')
		if sure4 == 'd':
			print('#> Processes are stopped, you can close window')

	if func == 'ipv4':
		print('#> IPv4 of the ' + uname+ ' is 116.214.48.211')
		print('#> Do u want to continue(c-continue, d-close):')
		sure3 = input()
		if sure3 == 'c':
			print('#> Commands ' + cmd_list)
			print('#> Restart and choose another commands')
		if sure3 == 'd':
			print('#> Processes are stopped, you can close window')

	if func == 'ddos':
		print('#> DDoS attach for User '+ uname + ' wait about 3 sec-s')
		time.sleep(3)
		print('#> Well done! PC was killed!')
		print('#> Do u want to continue(c-continue, d-close):')
		sure2 = input()
		if sure2 == 'c':
			print('#> Commands ' + cmd_list)
			print('#> Restart and choose another commands')
		if sure2 == 'd':
			print('Processes are stopped, you can close window')

	if func == 'kill_pc':
		print('#> Are you sure want to kill pc of the User '+uname+ ' [Да/Нет][Y/N]: ')
		sure = input()
		if sure == 'Да' or 'Y':
			print('#> Killing ' + uname + ' pc')
			print('10%')
			time.sleep(2)
			print('20%')
			time.sleep(2)
			print('30%')
			time.sleep(2)
			print('40%')
			time.sleep(2)
			print('50%')
			time.sleep(2)
			print('60%')
			time.sleep(2)
			print('70%')
			time.sleep(2)
			print('80%')
			time.sleep(2)
			print('90%')
			time.sleep(2)
			print('100%')
			time.sleep(2)
			print('#> Well done! PC was killed!')
			print('#> Do u want to continue(c-continue, d-close):')
			sure1 = input()
			if sure1 == 'c':
				print('#> Commands ' + cmd_list)
			print('#> Restart and choose another commands')
			if sure1 == 'd':
				print('#> Processes are stopped, you can close window')

				
r_txt1 = Label(text='Войдите в систему для взлома...').pack()
r_txt2 = Label(text='Логин:').pack()
r_f1 = Entry().pack()
r_txt3 = Label(text='Пароль:').pack()
r_f2 = Entry(show = '*').pack()
btn = Button(bg='red', text='Продолжить (ENG(USA))', width=20,height=1, command = click_button,).pack()

root.resizable(width=False, height=False)

root.mainloop()