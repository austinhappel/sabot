# emoticon helper

from errbot import BotPlugin, botcmd  # Note: if you use a version < 1.6.0 see below.
import re


class EnhancedEmoticons(BotPlugin):

    def __init__(self):
        self.saved_emoticons = {}

    @botcmd(split_args_with=' ')
    def emoticon(self, mess, args):
        """ Takes an emoticon command and saves it """

        if (len(args) == 2):
            self.saved_emoticons[str(args[0])] = str(args[1])

        return 'saved ((' + args[0] + ')) as ' + args[1] + '.'

    def callback_message(self, conn, mess):
        search = re.search('\(\(([a-zA-Z0-9\-\_\s]+)\)\)', str(mess.getBody()))

        if search:
            key = search.group(1)
            if (key in self.saved_emoticons):
                self.send(mess.getFrom(), str(self.saved_emoticons[key]), message_type=mess.getType())
