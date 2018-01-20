import urllib2, time, sys

def main():
    print('*'*37)
    print('+       Inc\'s PSN Name Checker      +')
    print('*'*37)

    word = raw_input('Please Enter A PSN Name: ')

    req = urllib2.Request('https://io.playstation.com/playstation/psn/profile/public/userData?onlineId=' + word)
    req.add_header('Referer', 'https://www.playstation.com/en-us/my/public-trophies')
    req.add_header('Origin', 'https://www.playstation.com')
    resp = urllib2.urlopen(req)
    content = resp.read()

    if "handle" not in content:
        print('Account Available: ' + word)
    else:
        print('Account Taken: '+word)

    retry = raw_input('Would You Like To Check Another Account (Y/N)?: ')

    if retry == 'y' or retry == 'Y':
        main()
    elif retry == 'n' or retry == 'N':
        Exit()

def Exit():
        print('Script Is Shutting Down In 3 Seconds')
        time.sleep(3)
        sys.exit("Thanks For Using My Script!\n~Inc")


if __name__ == '__main__':
    main()
