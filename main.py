"""A small tweeter bot."""

from twitter import Twitter, OAuth
from random import choice
from config import consumer_key, consumer_secret, \
    access_token, access_token_secret


adjective = "adjective.txt"
animal = "animal.txt"
friend = "friend.txt"


def adjectiveanimalfriend():
    with open(adjective) as adjective_file:
        with open(animal) as animal_file:
            with open(friend) as friend_file:
                adjective_list = adjective_file.readlines()
                animal_list = animal_file.readlines()
                friend_list = friend_file.readlines()

                return "{} {} {}".format(choice(adjective_list).rstrip(),
                                         choice(animal_list).rstrip(),
                                         choice(friend_list).rstrip())


def main():
    t = Twitter(auth=OAuth(access_token, access_token_secret, consumer_key,
                           consumer_secret))

    t.statuses.update(status=adjectiveanimalfriend())
if __name__ == "__main__":
    main()
