# emoticon helper

from errbot import BotPlugin, botcmd  # Note: if you use a version < 1.6.0 see below.
import re
import config


class ThisIsThat(BotPlugin):

    # @botcmd(split_args_with=' ')
    def parseThisThat(self, message):
        """ Looks for 'is' and saves XXXX is XXXX into database"""

        if len(args) == 2:
            self.__setitem__(str(args[0]), str(args[1]))
            return 'saved ((' + args[0] + ')) as ' + args[1] + '.'

        return 'usage: `!emoticon word http://url`'

    # TODO: what if name is stated twice in message
    def callback_message(self, conn, mess):
        message = str(mess.getBody())
        myFullName = config.BOT_IDENTITY['username']
        myShortName = myFullName[0:myFullName.find('@')]

        if myFullName in message \
        or myShortName + ':' in message \
        or '@' + myShortName in message:
            print "yes!"
            self.parseThisThat(message)

#        if emoticonCommand:
#            key = emoticonCommand.group(1)
#            if (key in self.keys()):
#                self.send(mess.getFrom(), str(self.__getitem__(key)), message_type=mess.getType())
