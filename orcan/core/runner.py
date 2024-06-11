from orcan.core.config import Config

from orcan.modules.domain import get_domain
from orcan.modules.who import get_who

banner = """
                  #####
                 #####
  ##########+++ #####
#######-.-+####+#####
+-.---+##+...+####+---
 #+-.....###########+--
   +++--.-############+-
     ##++-+############+--
     ####+++###########++-
    ######+++++########+.-+
     ####  ++++++++#####+-+#
      ###    ++++++++####+-#
                +++++########
                  ++++#######
                  ##+++######
                       +####+
                        ###+
                        ##++
                     ########
                    ##########
                    ###########
                            ###
"""

class Runner:
  def __init__(self, config: Config):
    self.config = config
  def __str__(self) -> str:
    return f"{self.config}"
  def run(self):
    print(banner)
    if self.config.url is not None: # is there a better way to do this?
      if self.config.domain is True:
        get_domain(self.config.url)
      if self.config.who is True:
        get_who(self.config.url)
    else:
      print("URL cannot be empty!")