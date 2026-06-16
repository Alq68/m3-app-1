from ._anvil_designer import Score_trackerTemplate
from anvil import *

class Score_tracker(Score_trackerTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.

  @handle("add_score", "click")
  def add_score_click(self, **event_args):
    score = int(self.player_score.content)
    score = score + 1
    self.player_score.content = str(score)

  @handle("add2_score", "click")
  def add2_score_click(self, **event_args):
    score = int(self.player2_score.content)
    score = score + 1
    self.player2_score.content = str(score)

  @handle("add3_score", "click")
  def add3_score_click(self, **event_args):
    score = int(self.player3_score.content)
    score = score + 1
    self.player3_score.content = str(score)

  @handle("add4_score", "click")
  def add4_score_click(self, **event_args):
    score = int(self.player4_score.content)
    score = score + 1
    self.player4_score.content = str(score)

  @handle("How_to2", "click")
  def How_to2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('homepage.How_to_play')

  @handle("Homepage_2", "click")
  def Homepage_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('homepage')
