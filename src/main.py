import instaloader
from getpass import getpass


def main():
    # clear old textfile
    open('usernames.txt', 'w').close()
    # import ig loader account
    ig = instaloader.Instaloader()

    # get personal account info from terminal and login
    username = input("Enter your username: ")
    # use getpass to hide user input in terminal
    password = getpass("Enter your password: ")
    ig.login(username, password)
    print('Logged in')

    # get profile metadata
    profile = instaloader.Profile.from_username(ig.context, username)
    print('Profile retrieved')
    following = set([p.username for p in profile.get_followees()])
    followers = set([p.username for p in profile.get_followers()])

    # find difference
    difference = following - followers

    # print to a text file
    f = open("usernames.txt", "w+")
    for opp in difference:
        f.write(opp + "\n")


main()
