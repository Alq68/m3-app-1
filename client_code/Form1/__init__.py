from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
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
    score = int(self.player_score.content)
    score = score + 1
    self.player_score.content = str(score)

  @handle("sub_score", "click")
  def sub_score_click(self, **event_args):
    
    score = int(self.player_score.content)
    score = score - 1
    self.player_score.content = str(score)
    if score == -1:
      score = 0
      self.player_score.content = str(score)

  @handle("sub2_score", "click")
  def sub2_score_click(self, **event_args):
    """This method is called when the button is clicked"""
    score = int(self.player2_score.content)
    score = score - 1
    self.player2_score.content = str(score)
    if score == -1:
      score = 0
      self.player2_score.content = str(score)

  @handle("sub3_score", "click")
  def sub3_score_click(self, **event_args):
    score = int(self.player3_score.content)
    score = score - 1
    self.player3_score.content = str(score)
    if score == -1:
      score = 0
      self.player3_score.content = str(score)

  @handle("sub4_score", "click")
  def sub4_score_click(self, **event_args):
    score = int(self.player4_score.content)
    score = score - 1
    self.player4_score.content = str(score)
    if score == -1:
      score = 0
      self.player4_score.content = str(score)