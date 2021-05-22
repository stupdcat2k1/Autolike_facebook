import json

from facebook_bot.facebook_bot import facebook_bot

if __name__ == '__main__':
    with open('config.json') as file:
        config = json.load(file)

    driver = config['driver']
    url = config['url']
    username = config['username']
    password = config['password']

    fb = facebook_bot(driver, url, username, password)
    #fb.like1()
    #fb.like2()
    fb.likev2()