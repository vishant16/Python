import re
msg="call me at 879-374-856 or at 123-456-789"
#pattern to be  get to create re object and {3} no of [0-9] is 3 times
PhoneNoRegex=re.compile(r'[0-9]{3}-[0-9]{3}-[0-9]{3}')
#
Matched_text=PhoneNoRegex.search(msg)
print(Matched_text.group()) #search return single matched pattern

Matched_text=PhoneNoRegex.findall(msg)
print(Matched_text) #findall return list of all Matched pattern

PhoneNoRegex=re.compile(r'([0-9]{3})-([0-9]{3}-[0-9]{3})')
Matched_text=PhoneNoRegex.search(msg)
print(Matched_text.group(1)) # return (1) of msg


msg="vishant 12345678 12312"
PhoneNoRegex=re.compile(r'[0-9]{3,6}') #it takes longest pattern
Matched_text=PhoneNoRegex.search(msg)
print(Matched_text.group())

PhoneNoRegex=re.compile(r'[0-9]{3,6}?') #take small/3 pattern
Matched_text=PhoneNoRegex.search(msg)
print(Matched_text.group())

msg="vishant 12312 ok"
PhoneNoRegex=re.compile(r'\d+\s\w ') #search all numbers
Matched_text=PhoneNoRegex.findall(msg)
print(Matched_text)

PhoneNoRegex=re.compile(r'[^o]') #except o
Matched_text=PhoneNoRegex.findall(msg)
print(Matched_text)


#start with ^ and end with $
msg="vishantok 12312 vishantokok"
PhoneNoRegex=re.compile(r'^vishant') #except o
Matched_text=PhoneNoRegex.search(msg)
print(Matched_text)

msg="123vishant ok 1vishant"
PhoneNoRegex=re.compile(r'vishant$') #except o
Matched_text=PhoneNoRegex.search(msg)
print(Matched_text)

# .to find occurance of substring .ok
msg="123vishantokokkok 2ok 1ok"
PhoneNoRegex=re.compile(r' .ok') #except o
Matched_text=PhoneNoRegex.findall(msg)
print(Matched_text)

msg="{123vishantokokkok} 2ok 1ok"
PhoneNoRegex=re.compile(r'{.*?}') #except o
Matched_text=PhoneNoRegex.findall(msg)
print(Matched_text)
