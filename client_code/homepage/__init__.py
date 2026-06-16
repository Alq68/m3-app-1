from ._anvil_designer import homepageTemplate
from anvil import *

class homepage(homepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.

  @handle("score_tracker_1", "click")
  def score_tracker_1_click(self, **event_args):
    open_form('homepage.Score_tracker')

  @handle("How_to1", "click")
  def How_to1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('homepage.How_to_play')
