#! /usr/bin/python

def main():
    s=raw_input("Enter string:")
 #   print("your string is",  +(s))
    vowels=0
    for i in s:
       if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
                vowels=vowels+1
    print("Number of vowels are:")
    print(vowels)

if __name__=='__main__':
	main()