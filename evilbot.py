import webbrowser
import os
import sys
import random
from random import randint
import time
import pyfiglet


def ran_time():
    sec = randint(min_sec, max_sec)
    for remaining in range(sec, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining))
        sys.stdout.flush()
        time.sleep(1)

    sys.stdout.write("\rComplete!            \n")


def open_page():
    link = ["https://techforhack.com/84-woocommerce-extensions-updates/",
            "https://techforhack.com/56-woocommerce-extensions-updates/",
            "https://techforhack.com/newspaper-v10-3-7-wordpress-news-theme/",
            "https://techforhack.com/elementor_pro_3-0-4_nulled/",
            "https://techforhack.com/adobe-cc-2020-universal-crack-for-adobe-cc-2020-full-version/",
            "https://techforhack.com/wireshark-termux/",
            "https://techforhack.com/windows-10-kali-linux-subsystem-full-tutorial/",
            "https://techforhack.com/tool-x/",
            "https://techforhack.com/routersploit/",
            "https://techforhack.com/newspaper-v10-3-7-wordpress-news-theme/",
            "https://techforhack.com/networkingfundamentals/",
            "https://techforhack.com/networkdevices/",
            "https://techforhack.com/portable_hacking_device/",
            "https://techforhack.com/tbomber/",
            "https://techforhack.com/metasploit-termux/",
            "https://techforhack.com/lazy_script/",
            "https://techforhack.com/nethunter-on-android/",
            "https://techforhack.com/install-hidden-eye-advanced-phishing-tool-full-guide/",
            "https://techforhack.com/instagram-tools-hack-insta-from-termux/",
            "https://techforhack.com/black_hydra/",
            "https://techforhack.com/nmap/",
            "https://techforhack.com/hackpro/",
            "https://techforhack.com/fix-any-android-game-lag-in-few-minutes/",
            "https://techforhack.com/elementor_pro_3-0-4_nulled/",
            "https://techforhack.com/ddos-termux/",
            "https://techforhack.com/databasetechnology/",
            "https://techforhack.com/database-models-all-you-need-to-know/",
            "https://techforhack.com/metasploit-payload-termux/"
            ]

    url_link_1 = random.choice(link)
    url_link_2 = random.choice(link)
    url_link_3 = random.choice(link)

    print("Opening URL")
    print(url_link_1, "||", url_link_2, "||", url_link_3)

    webbrowser.open_new_tab(url_link_1)
    time.sleep(10)
    webbrowser.open_new_tab(url_link_2)
    time.sleep(12)
    webbrowser.open_new_tab(url_link_3)
    time.sleep(9)


def loop():
    i = views
    try:
        completed_views = 0
        while i > 0:
            print(i, " views remaining")
            open_page()
            ran_time()
            i -= 3
            completed_views += 1
            print("Closing Browser")
            os.system("./setting.sh")
    except Exception as e:
        print(e)
        print("you got", completed_views, "visitors")

    print("you got", completed_views, "visitors")


def taking_input():
    global min_sec, max_sec, views
    try:
        views = int(input("Number of visitors : "))
        print("----------------------------------------------------------------------------------")
        print("How much time have to spend in the page")
        print("Enter the time in seconds.")
        print("Enter numbers only.")
        min_sec = int(input("Minimum waiting time : "))
        print("----------------------------------------------------------------------------------")
        print("How much time have to spend in the page")
        print("Enter the time in seconds.")
        max_sec = int(input("Maximum waiting time : "))
        print("----------------------------------------------------------------------------------")
    except Exception as error:
        print(error)

    if min_sec < max_sec:
        loop()
    else:
        print("Oooops! the value you enter is wrong.")
        print("Try again.")
        taking_input()


if __name__ == '__main__':
    ascii_banner = pyfiglet.figlet_format("     E Traffic Bot", font="slant")
    print(ascii_banner)
    print("##################################################################################")
    print("Generate free traffic")
    taking_input()
