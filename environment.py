# Environment module
# Cells have these features:
'''
{'type': 'normal', 'reward': -1, 'occupied_by': ''}
{'type': 'risky', 'reward': -2, 'occupied_by': ''}
{'type': 'pickup', 'reward': +14, 'occupied_by': '', 'block_count': 10}
{'type': 'dropoff', 'reward': +14, 'occupied_by': '', 'block_count': 0}
'''

'''
Environtment is sent to state, which is sent to agent. Agent makes move, changing the environment. Like a triangle cycle.
'''
class Environment:
  def __init__(self):
    first_level = [
      [
        {'type': 'normal', 'reward': -1, 'occupied_by': 'f'},
        {'type': 'normal', 'reward': -1, 'occupied_by': ''},
        {'type': 'dropoff', 'reward': +14, 'occupied_by': '', 'block_count': 0}
      ],
      [
        {'type': 'normal', 'reward': -1, 'occupied_by': ''},
        {'type': 'pickup', 'reward': +14, 'occupied_by': '', 'block_count': 10},
        {'type': 'risky', 'reward': -2, 'occupied_by': ''}
      ],
      [
        {'type': 'normal', 'reward': -1, 'occupied_by': ''},
        {'type': 'normal', 'reward': -1, 'occupied_by': ''},
        {'type': 'normal', 'reward': -1, 'occupied_by': ''}
      ]
    ]
    second_level = [
      [
        {'type': 'dropoff', 'reward': +14, 'occupied_by': '', 'block_count': 0},
        {'type': 'normal', 'reward': -1, 'occupied_by': ''},
        {'type': 'normal', 'reward': -1, 'occupied_by': ''}
      ],
      [
        {'type': 'normal', 'reward': -1, 'occupied_by': ''},
        {'type': 'risky', 'reward': -2, 'occupied_by': ''},
        {'type': 'normal', 'reward': -1, 'occupied_by': ''}
      ],
      [
        {'type': 'normal', 'reward': -1, 'occupied_by': ''},
        {'type': 'normal', 'reward': -1, 'occupied_by': ''},
        {'type': 'pickup', 'reward': +14, 'occupied_by': '', 'block_count': 10}
      ]
    ]
    third_level = [
      [
        {'type': 'dropoff', 'reward': +14, 'occupied_by': '', 'block_count': 0},
        {'type': 'normal', 'reward': -1, 'occupied_by': ''},
        {'type': 'normal', 'reward': -1, 'occupied_by': ''}
      ],
      [
        {'type': 'normal', 'reward': -1, 'occupied_by': ''},
        {'type': 'normal', 'reward': -1, 'occupied_by': ''},
        {'type': 'dropoff', 'reward': +14, 'occupied_by': 'm', 'block_count': 0}
      ],
      [
        {'type': 'normal', 'reward': -1, 'occupied_by': ''},
        {'type': 'normal', 'reward': -1, 'occupied_by': ''},
        {'type': 'normal', 'reward': -1, 'occupied_by': ''}
      ]
    ]
    self.env = [first_level, second_level, third_level]
    
  def move_agent(self, old_coords, action):
    self
