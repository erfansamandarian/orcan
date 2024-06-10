from reco.core.config import Config

from reco.modules.domain import get_domain
from reco.modules.who import get_who

class Runner:
  def __init__(self, config: Config):
    self.config = config
  def __str__(self) -> str:
    return f"{self.config}"
  def run(self):
    if self.config.domain is True:
      # todo 
    if self.config.who is True:
      # todo 
