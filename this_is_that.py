# emoticon helper

from errbot import BotPlugin, botcmd  # Note: if you use a version < 1.6.0 see below.
import re
import string
import config
from random import randint

# import string


class ThisIsThat(BotPlugin):

    my_full_name = config.BOT_IDENTITY['username']
    regex_punctuation = r'!"#$%&\'()*+,-./:;<=>?@\[\\\]^_`{|}~\s'
    question_regex = r'\b(what|who) is\b'

    @property
    def my_short_name(self):
        return self.my_full_name[0:self.my_full_name.find('@')]

    @property
    def short_name_regex(self):
        return r'[' + self.regex_punctuation + r']*' + self.my_short_name + \
        r'[' + self.regex_punctuation + r']*'

    def get_answer_flavor_text(self):
        flavors = [
            'I have been told that ',
            'Someone once said that ',
            'I think ',
            'I believe ',
            ''
        ]

        return flavors[randint(0, len(flavors) - 1)]

    def get_sender_short_name(self, sender):
        return sender[0:sender.find('@')]

    # @botcmd(split_args_with=' ')
    def parse_command(self, mess):
        """ Looks for 'is' and saves XXXX is XXXX into database"""

        message = str(mess.getBody())
        sender = str(mess.getFrom())
        strip_characters = string.punctuation + ' '
        cleaned_message = re.sub(self.short_name_regex, '', message)
        this_that = re.split(r'\bis\b', cleaned_message, maxsplit=1)

        # save to the database, strip whitespace and punctuation from both
        self.__setitem__(this_that[0].strip().strip(strip_characters), \
            this_that[1].strip().strip(strip_characters))

        return "Whatever you say, " + self.get_sender_short_name(sender) + "."

    def parse_question(self, mess, must_respond=False):
        """ Searches the db for a key whose name comes after the 'is'
        in the message."""

        message = str(mess.getBody())
        strip_characters = string.punctuation + ' '

        # remove name
        message_clean = re.sub(self.short_name_regex, '', message)

        # remove everything before trigger statement (what is)
        message_clean = re.split(self.question_regex, message_clean, maxsplit=1)[2]

        key = message_clean.strip().strip(strip_characters)

        if key in self.keys():
            return self.get_answer_flavor_text() + key + ' is ' + self.__getitem__(key)
        elif must_respond is True:
            return "I don't know what " + key + " is."

    # TODO: what if name is stated twice in message
    def callback_message(self, conn, mess):
        message = str(mess.getBody())

        # is my name mentioned?
        if re.search(self.short_name_regex, message) != None:
            # is this a command?
            if re.search(self.question_regex, message) is None and \
            re.search(r'\bis\b', message) != None:
                response = self.parse_command(mess)
                if response != None:
                    self.send(mess.getFrom(), response, message_type=mess.getType())

            # is this a request?
            if re.search(self.question_regex, message) != None:
                response = self.parse_question(mess, True)
                if response != None:
                    self.send(mess.getFrom(), response, message_type=mess.getType())

        else:
            # is this a request?
            if re.search(self.question_regex, message) != None:
                response = self.parse_question(mess)
                if response != None:
                    self.send(mess.getFrom(), response, message_type=mess.getType())
