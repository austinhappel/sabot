# emoticon helper

from errbot import BotPlugin, botcmd  # Note: if you use a version < 1.6.0 see below.
from random import randint


class Roll_dice(BotPlugin):

    @botcmd(split_args_with=' ')
    def roll(self, mess, args):
        """ Rolls the dice """

        max_sides = 6
        if args[0] != '':
            max_sides = int(args[0])

        return 'Result of rolling D' + str(max_sides) + ': ' + str(randint(1, max_sides)) + '!'
