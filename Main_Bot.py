import json
from tkinter import *
from tkinter import ttk
import sqlite3
import time
import requests
from selenium import webdriver
from csv import reader
import random
from webdriver_manager.firefox import GeckoDriverManager


window = Tk()
window.title('Verify Your Product Key ')
window.geometry('200x250')
window.configure(bg='#96001e')

options = ["Subscribers", "Views", "Sub + Views", "Likes", "All"]


def whole_story():
    root = Toplevel()

    root.title('My Awesome Bot ')
    root.geometry('500x500')
    root.configure(bg='#96001e')

    def loginer(id_str, pass_str):
        global browser
        try:
           
            browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            url = 'https://www.gmail.com/'
            browser.delete_all_cookies()
            browser.get(url)
            email_field = browser.find_element_by_id("identifierId")
            email_field.clear()
            email_field.send_keys(id_str)
            email_next_button = browser.find_element_by_id("identifierNext")
            email_next_button.click()
            w1 = random.randint(2, 15)
            time.sleep(w1)
            password_field = browser.find_element_by_name("password")
            password_field.clear()
            password_field.send_keys(pass_str)
            password_next_button = browser.find_element_by_id("passwordNext")
            password_next_button.click()
            w1 = random.randint(17, 24)
            time.sleep(w1)
        except Exception as j:
            print(j)

    def new_func(event):

        _subscriber_label = Label(root, text='Amount in Numbers (eg: 800)', fg='White', bg='#96001e')
        _subscriber_label.pack()
        numbers = Entry(root, bg='black', fg='white', width=10)
        numbers.pack()
        if clicked.get() == 'Subscribers':
            _subscriber_label_channel = Label(root, fg='white', bg='#96001e')
            _subscriber_label_channel.config(text='Please enter the link of the channel :-)')
            _subscriber_label.config(bg='#96001e')
            _subscriber_label_channel.pack()
            _subscriber_entry_ = Entry(root, bg='black', fg='white', width=30)
            _subscriber_entry_.pack()

            def _subscriber_():
                def _subscriber_maker():

                    try:
                        loginer(id_str, id_pass)
                        browser.get(_subscriber_entry_.get())
                        subscribe_next_button = browser.find_element_by_class_name(
                            "style-scope ytd-subscribe-button-renderer")
                        subscribe_next_button.click()
                        w3 = random.randint(5, 10)
                        time.sleep(w3)
                    except:
                        browser.close()

                with open('id_pass.csv', 'r', encoding='Latin-1') as read_obj:
                    # pass the file object to reader() to get the reader object
                    csv_reader = reader(read_obj)
                    # Pass reader object to list() to get a list of lists
                    list_of_rows = list(csv_reader)
                print("Total Ids and Passwords: ", len(list_of_rows))
                total_Len = len(list_of_rows)
                ids_pass_list = list_of_rows
                try:
                    how_many = int(numbers.get())
                    # int(numb) #int(input("Please enter the number of likes, views or subscribers that you need: "))
                    for i in range(how_many):
                        id_str = ids_pass_list[i][0]
                        id_pass = ids_pass_list[i][1]
                        print("This is {} number turn.".format(i))
                        print("Login Id: ", id_str)
                        print("Login Password: ", id_pass)
                        _subscriber_maker()
                except ValueError:
                    print("Not converted")

            _subscriber_button = Button(root, text='Start The Process', width=40, font='10',
                                        bg='Black', fg='White',
                                        command=_subscriber_)
            _subscriber_button.pack(pady=70)

        elif clicked.get() == 'Views':
            views_label = Label(root, fg='white', bg='#96001e')
            views_label.config(text='Please enter the link of a video :-)')
            views_label.pack()
            _views_entry_ = Entry(root, bg='black', fg='white', width=30)
            _views_entry_.pack()

            def _views_():
                def _views_maker_():

                    try:
                        loginer(id_str, id_pass)
                        browser.get(_views_entry_.get())
                        w4 = random.randint(20, 30)
                        time.sleep(w4)
                    except:
                        pass

                with open('id_pass.csv', 'r', encoding='Latin-1') as read_obj:
                    # pass the file object to reader() to get the reader object
                    csv_reader = reader(read_obj)
                    # Pass reader object to list() to get a list of lists
                    list_of_rows = list(csv_reader)
                print("Total Ids and Passwords: ", len(list_of_rows))
                total_Len = len(list_of_rows)
                ids_pass_list = list_of_rows
                try:
                    how_many = int(numbers.get())
                    # int(numb) #int(input("Please enter the number of likes, views or subscribers that you need: "))
                    for i in range(how_many):
                        id_str = ids_pass_list[i][0]
                        id_pass = ids_pass_list[i][1]
                        print("This is {} number turn.".format(i))
                        print("Login Id: ", id_str)
                        print("Login Password: ", id_pass)
                        _views_maker_()

                except ValueError:
                    print("Not converted")

            _subscriber_button = Button(root, text='Start The Process', width=40, font='10',
                                        bg='Black', fg='White',
                                        command=_views_)
            _subscriber_button.pack(pady=70)
        elif clicked.get() == 'Sub + Views':
            sub_views_label = Label(root, fg='white', bg='#96001e')
            sub_views_label.config(text='Please enter the link of a video :-)')
            sub_views_label.pack()
            _sub_views_entry_ = Entry(root, bg='black', fg='white', width=30)
            _sub_views_entry_.pack()

            def _sub_views_():
                def _sub_views_maker_():

                    try:
                        loginer(id_str, id_pass)
                        browser.get(_sub_views_entry_.get())
                        sub_and_watch = browser.find_element_by_xpath(
                            '//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/tp-yt-paper-button')
                        browser.execute_script("arguments[0].click();", sub_and_watch)
                        w6 = random.randint(20, 30)
                        time.sleep(w6)
                    except:
                        pass

                with open('id_pass.csv', 'r', encoding='Latin-1') as read_obj:
                    # pass the file object to reader() to get the reader object
                    csv_reader = reader(read_obj)
                    # Pass reader object to list() to get a list of lists
                    list_of_rows = list(csv_reader)
                print("Total Ids and Passwords: ", len(list_of_rows))
                total_Len = len(list_of_rows)
                ids_pass_list = list_of_rows
                try:
                    how_many = int(numbers.get())
                    # int(numb) #int(input("Please enter the number of likes, views or subscribers that you need: "))

                    for i in range(how_many):
                        id_str = ids_pass_list[i][0]
                        id_pass = ids_pass_list[i][1]
                        print("This is {} number turn.".format(i))
                        print("Login Id: ", id_str)
                        print("Login Password: ", id_pass)
                        _sub_views_maker_()

                except ValueError:
                    print("Not converted")

            _subscriber_button = Button(root, text='Start The Process', width=40, font='10',
                                        bg='Black', fg='White',
                                        command=_sub_views_)
            _subscriber_button.pack(pady=70)

        elif clicked.get() == 'Likes':
            likes_label = Label(root, text='Please enter the link of a video :-)', fg='white', bg='#96001e')
            likes_label.pack()
            _likes_entry_ = Entry(root, bg='black', fg='white', width=30)
            _likes_entry_.pack()

            def _likes_():
                def _likes_maker_():
                    try:

                        loginer(id_str, id_pass)
                        w1 = random.randint(17, 24)
                        time.sleep(w1)
                        browser.get(_likes_entry_.get())
                        like_it = browser.find_element_by_xpath(
                            '//*[@id="top-level-buttons-computed"]/ytd-toggle-button-renderer[1]/a')
                        browser.execute_script("arguments[0].click();", like_it)
                        w5 = random.randint(10, 18)
                        time.sleep(w5)
                    except:
                        browser.quit()

                with open('id_pass.csv', 'r', encoding='Latin-1') as read_obj:
                    # pass the file object to reader() to get the reader object
                    csv_reader = reader(read_obj)
                    # Pass reader object to list() to get a list of lists
                    list_of_rows = list(csv_reader)
                print("Total Ids and Passwords: ", len(list_of_rows))
                total_Len = len(list_of_rows)
                ids_pass_list = list_of_rows
                try:
                    how_many = int(numbers.get())
                    # int(numb) #int(input("Please enter the number of likes, views or subscribers that you need: "))

                    for i in range(how_many):
                        id_str = ids_pass_list[i][0]
                        id_pass = ids_pass_list[i][1]
                        print("This is {} number turn.".format(i))
                        print("Login Id: ", id_str)
                        print("Login Password: ", id_pass)
                        _likes_maker_()

                except ValueError:
                    print("Not converted")

            _subscriber_button = Button(root, text='Start The Process', width=40, font='10',
                                        bg='Black', fg='White',
                                        command=_likes_)
            _subscriber_button.pack(pady=70)


        elif clicked.get() == 'All':
            all_label = Label(root, fg='white', bg='#96001e')
            all_label.config(text='Please enter the link of a video :-)')
            all_label.pack()
            _all_entry_ = Entry(root, bg='black', fg='white', width=30)
            _all_entry_.pack()

            def _all_():
                def _all_maker_():
                    try:
                        loginer(id_str, id_pass)
                        w1 = random.randint(3, 10)
                        time.sleep(w1)
                        browser.get(_all_entry_.get())
                        time.sleep(random.randint(8, 15))
                        sub = browser.find_element_by_xpath(
                            '//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/tp-yt-paper-button')
                        browser.execute_script("arguments[0].click();", sub)
                        time.sleep(random.randint(10, 20))
                        like = browser.find_element_by_xpath(
                            '//*[@id="top-level-buttons-computed"]/ytd-toggle-button-renderer[1]/a')
                        browser.execute_script("arguments[0].click();", like)
                        w6 = random.randint(10, 12)
                        time.sleep(w6)
                        browser.quit()
                    except:
                        browser.quit()

                with open('id_pass.csv', 'r', encoding='Latin-1') as read_obj:
                    # pass the file object to reader() to get the reader object
                    csv_reader = reader(read_obj)
                    # Pass reader object to list() to get a list of lists
                    list_of_rows = list(csv_reader)
                print("Total Ids and Passwords: ", len(list_of_rows))
                total_Len = len(list_of_rows)
                ids_pass_list = list_of_rows
                try:
                    how_many = int(numbers.get())
                    # int(numb) #int(input("Please enter the number of likes, views or subscribers that you need: "))

                    for i in range(how_many):
                        id_str = ids_pass_list[i][0]
                        id_pass = ids_pass_list[i][1]
                        print("This is {} number turn.".format(i))
                        print("Login Id: ", id_str)
                        print("Login Password: ", id_pass)
                        _all_maker_()

                except ValueError:
                    print("Not converted")

            _subscriber_button = Button(root, text='Start The Process', width=40, font='10',
                                        bg='Black', fg='White',
                                        command=_all_)
            _subscriber_button.pack(pady=70)

    clicked = StringVar()
    clicked.set('Heyy.. Click Me :-)')
    options_menu = OptionMenu(root, clicked, *options, command=new_func)
    options_menu.pack(pady=20)


def verify(key):
    global score

    score = 0

    # Definie Our Check Digit
    check_digit = key[2]
    check_digit_count = 0

    # Separate By Dash
    chunks = key.split('-')

    # Loops through and check stuff
    for chunk in chunks:
        if len(chunk) != 4:
            return False

        for char in chunk:
            if char == check_digit:
                check_digit_count += 1
            # Grab the score of the ANSCII character
            score += ord(char)

    # Check for rules
    if score > 1700 and score < 1800 and check_digit_count == 3:
        return True
    else:
        return False





def verificationFun():

    key_entered = keyEntry.get()
    with open('database.txt', 'w') as data:
        data.write(key_entered)
        data.close()
    abab = open('database.txt', 'r')
    key = abab.read()

    if not verify(key):
       pass
    else:
        whole_story()
try:
    abab = open('database.txt', 'r')
    key = abab.read()
    if not verify(key):
        keyEntry = Entry(window, bg='black', fg='white', width=30)
        keyEntry.pack(pady=20)
        Key_button = Button(window, text='Enter Your Product Key', bg='black', fg='white', command=verificationFun)
        Key_button.pack(pady=20)


    else:
        lblb = Label(window, text="Don't close me", bg='black', fg='white')
        lblb.pack(pady=20)
        whole_story()

except:
    keyEntry = Entry(window, bg='black', fg='white', width=30)
    keyEntry.pack(pady=20)
    Key_button = Button(window, text='Enter Your Product Key', bg='black', fg='white', command=verificationFun)
    Key_button.pack(pady=20)


window.mainloop()
