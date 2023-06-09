from typing import Dict, List, Optional
import flask
from flask import Flask, request, jsonify
import pathlib
import uuid
import json

app = Flask(__name__)
thisdir = pathlib.Path(__file__).parent.absolute()

def load_leaderboard() -> List[Dict[str, str]]:
  """
    Loads the leaderboard
   """
  try:
   return json.loads(thisdir.joinpath('blinkingScores.json').read_text())
  except FileNotFoundError:
   return []

def save_leaderboard(lboard: List[Dict[str, str]]):
    """
      Saves the leaderboard
    """
    jason = json.dumps(lboard)
    thisdir.joinpath('blinkingScores.json').write_text(jason)

@app.route('/leaderboard/sendscore', methods=['POST', 'GET'])
def receive_new_score() -> List[Dict[str, str]]:
  """
   Appends leaderboard with new score
  """
  mes = request.get_data()
  leaderboard = load_leaderboard()
  tojason = mes.decode('utf-8')
  leaderboard.append(tojason)
  save_leaderboard(leaderboard)
  return jsonify(leaderboard)
'''
@app.route('/leaderboard/makeboard', methods=['GET'])
def print_leaderboard():
  """
   Takes the top 5 scores from the leaderboard and prints them 
  """
  leaderboard = load_leaderboard()
'''  
    


if __name__ == "__main__":
  app.run(host = "172.20.10.7", port=5000, debug=True)
    
    
    
    
