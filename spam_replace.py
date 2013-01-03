# emoticon helper

from errbot import BotPlugin, botcmd  # Note: if you use a version < 1.6.0 see below.
import re
from time import sleep


class EnhancedEmoticons(BotPlugin):

    @botcmd(split_args_with=' ')
    def sr(self, mess, args):
        """ Takes 2 s/find/replace commands and runs one after the other
        several times """

        times = 10
        self.send(mess.getFrom(), "testing something", message_type=mess.getType())
        if len(args) == 2:
            arg1 = args[0]
            arg2 = args[1]

            for i in range(times):
                if i % 2 == 0:
                    response = arg1
                else:
                    response = arg2

                print '>>' + response
                self.send(mess.getFrom(), response, message_type=mess.getType())
                sleep(0.5)
