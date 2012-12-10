# emoticon helper

from errbot import BotPlugin, botcmd  # Note: if you use a version < 1.6.0 see below.
import re


class EnhancedEmoticons(BotPlugin):

    @botcmd(split_args_with=' ')
    def emoticon(self, mess, args):
        """ Takes an emoticon command and saves it """
        print len(args)

        if len(args) == 2:
            self.__setitem__(str(args[0]), str(args[1]))
            return 'saved ((' + args[0] + ')) as ' + args[1] + '.'

        return 'usage: `!emoticon word http://url`'

    def callback_message(self, conn, mess):
        message = str(mess.getBody())

        emoticonCommand = re.search('\(\(([a-zA-Z0-9\-\_\s]+)\)\)', message)

        if emoticonCommand:
            key = emoticonCommand.group(1)
            if (key in self.keys()):
                self.send(mess.getFrom(), str(self.__getitem__(key)), message_type=mess.getType())
