from typing import Dict, List, Optional
from flask import Flask, request, jsonify
import pathlib
import uuid
import json

app = flask.Flask(__name__)
thisdir = pathlib.Path(__file__).parent.absolute()

def load_leaderboard() -> Dict[str, str]]:
  """
    Loads the leaderboard
   """
  try:
   return json.loads(thisdir.joinpath('blinkingScores.json').read_text())
  except FileNotFoundError:
   return []

def save_leaderboard(lboard: Dict[str, str]]) -> None:
    """
      Saves the leaderboard
    """
    thisdir.joinpath('blinkingScores.json').write_text(json.dumps(lboard, indent=4))

@app.route('/leaderboard/sendscore', methods=['POST'])
def receive_new_score():
  """
   Appends leaderboard with new score
  """
  mes = request.get_data()
  print(str(mes))
  return str(mes)

@app.route('/leaderboard/makeboard', methods=['GET'])
def print_leaderboard():
    """
     Takes the top 5 scores from the leaderboard and prints them 
    """
    


if __name__ == "__main__":
  app.run()
    
    
    
    
