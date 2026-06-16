from ._anvil_designer import How_to_playTemplate
from anvil import *

class How_to_play(How_to_playTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.

  @handle("Homepage", "click")
  def Homepage_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('homepage')

  @handle("Score_tracker2", "click")
  def Score_tracker2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('homepage.Score_tracker')
