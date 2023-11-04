from helium import *
from selenium import webdriver
import time

def send_messages(user_name="", password="", user_to_send="" ,num_of_messages=0, message=""):
    options = webdriver.ChromeOptions()
    options.add_argument('lang=en')

    driver = start_chrome("instagram.com", maximize=True, options=options)
    
    wait_until(Button("Log in").exists)

    write(user_name, into="Phone number, username, or email")
    write(password, into="Password")
    click("Log in")

    time.sleep(7)
  
    go_to("instagram.com/direct/inbox/")

    click("Send message")

    if Button("Not now").exists:
        click("Not now")

    click("send message")
    write(user_to_send, into="Search...")

    wait_until(Button(to_right_of="To:").exists, timeout_secs=1000)
  
    click("Chat")
  
    time.sleep(2)

    for i in range(num_of_messages):
        write(message, into="Message...")
        click("Send")

def main():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    user_to_spam = input("Enter the username of the recipient: ")
    num_of_messages = int(input("Enter the number of messages to send: "))
    msg = input("Enter the message to send: ")

    send_messages(username, password, user_to_spam, num_of_messages, msg)


if __name__ == "__main__":
    main()
