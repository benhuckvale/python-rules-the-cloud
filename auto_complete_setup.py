import readline
import rlcompleter

class filtered_rlcompleter(rlcompleter.Completer):
    def attr_matches(self, text):
        orig = rlcompleter.Completer.attr_matches(self, text);
        filtered = filter(lambda x: x.find(".__")==-1, orig)
        return filtered

if 'libedit' in readline.__doc__:
    readline.parse_and_bind("bind ^I rl_complete")
else:
    readline.parse_and_bind("tab: complete")

readline.set_completer(filtered_rlcompleter().complete)
