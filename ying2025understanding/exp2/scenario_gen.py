import json

STATEMENTS = {
  "1_1": [
    "The player believes the blue key is in box 1.",
    "The player is sure there must be a blue key in box 3.",
    "The player believes that box 1 or 2 contain the blue key, but leans more towards box 1.",
    "The player thinks that box 1 is empty.",
    "The player believes that box 1 contains the blue key."
  ],
  "1_2": [
    "The player is sure there must be a blue key in box 3.",
    "The player knows that boxes 1 and 2 did not have the blue key.",
    "The player believes that the blue key is in box number 3.",
    "The player believes that box 3 is more likely to contain a red key than box 1.",
    "The player believes that box 3 is empty."
  ],
  "1_3": [
    "The player thinks that box 1 is empty.",
    "The player is uncertain about the contents of box 3.",
    "The player believes that box 2 is empty.",
    "The player believes that if box 1 does not have a blue key, then box 3 has a blue key.",
    "The player believes there may be a key in box 1."
  ],
  "2_1": [
    "The player knows that box 1 does not have the blue key.",
    "The player believes if the red key is not in box 2 then it must be in box 3.",
    "The player believes that box 2 has a key.",
    "The player believes box 2 might hold a red key.",
    "The player knows that box 2 is empty."
  ],
  "2_2": [
    "The player thinks that box 1 is empty.",
    "The player believes that box 3 is empty.",
    "The player thinks that box 1 is empty.",
    "The player believes that box 3 may contain a red key.",
    "The player believes that box 3 is more likely to contain a red key than box 1."
  ],
  "2_3": [
    "The player believes that box 2 may contain the red key.",
    "The player believes that box 2 is empty.",
    "The player thinks that boxes 2 and 3 might or might not contain a red key.",
    "The player believes the red key is in box 2.",
    "The player thinks that there's more likely to be a red key in box 1 or 3 than box 2."
  ],
  "3_1": [
    "The player believes box 2 is least likely to hold the blue key.",
    "The player believes that box 3 holds the blue key.",
    "The player knows box 3 contains a blue key.",
    "The player thinks that box 1 is empty.",
    "The player knows that box 2 is empty."
  ],
  "3_2": [
    "The player believes that box 2 may contain the red key.",
    "The player believes the red key is in box 2.",
    "The player does not know which box contains a red key.",
    "The player believes that box 3 may contain a red key.",
    "The player believes that box 1 might have a red key."
  ],
  "3_3": [
    "The player knows that box 1 does not have the blue key.",
    "The player thinks that box 1 is empty.",
    "The player is unsure whether the blue key is in box 3 or 1.",
    "The player believes that box 3 will either be empty or have a blue key.",
    "The player believes the red key is in box 2."
  ],
  "4_1": [
    "The player believes box 1 is more likely to contain a red key than box 2.",
    "The player believes that box 3 may contain a red key.",
    "The player thinks that there's more likely to be a red key in box 2 or 3 than box 1.",
    "The player believes that either box 2 or 3 contains a red key.",
    "The player believes box 1 does not hold a red key."
  ],
  "4_2": [
    "The player believes that box 3 may contain a red key.",
    "The player knows that box 2 is empty.",
    "The player is sure that box 1 and 2 are empty.",
    "The player believes that box 2 may contain a red key.",
    "The player thinks that box 1 is empty."
  ],
  "4_3": [
    "The player believes that box 2 may contain a red key.",
    "The player is unsure which box has a key.",
    "The player believes that box 3 may contain a red key.",
    "The player believes that the red key must be in box 3.",
    "The player believes there might be a key in box 2."
  ],
  "5_1": [
    "The player believes that box 3 might have a red key.",
    "The player believes that there is a red key in box 2.",
    "The player believes that box 1 is empty.",
    "The player believes that either box 2 or 3 has a red key.",
    "The player believes that the red key must be in box 3."
  ],
  "5_2": [
    "The player believes that box 2 may contain a red key.",
    "The player believes that box 3 is empty.",
    "The player knows that the boxes 1 and 2 were both empty.",
    "The player believes that the red key must be in box 3.",
    "The player is uncertain about the contents of box 3."
  ],
  "6_1": [
    "The player believes that box 2 probably has a key.",
    "The player knows that box 2 is empty.",
    "The player knows that there is a blue or red key in box 1.",
    "The player believes that either a red key or a blue key is in box 2.",
    "The player believes that box 1 might hold a blue key."
  ],
  "6_2": [
    "The player believes that box number 2 holds the red key.",
    "The player believes that box 2 holds a blue key.",
    "The player believes the blue key is in box 1.",
    "The player believes that there is a red key in box 2.",
    "The player believes there might be a key in Box 1 or Box 2."
  ],
  "6_3": [
    "The player believes that the boxes are both empty.",
    "The player believes that box 1 might have a red key.",
    "The player believes the red key is in box 2.",
    "The player believes that box 1 is empty.",
    "The player believes there might be a key in box 1 or box 2."
  ],
  "7_1": [
    "The player believes there might be a red key in box 3.",
    "The player knows that box 2 is empty.",
    "The player knows that box 3 is empty.",
    "The player believes that there is a red key in box 2.",
    "The player believes that box 1 might have a red key."
  ],
  "7_2": [
    "The player knows that box 1 does not have the red key.",
    "The player believes that box number 2 holds the red key.",
    "The player believes that box 1 might have a red key.",
    "The player believes there might be a key in box 2.",
    "The player believes that box 2 is more likely to contain a red key than box 3."
  ],
  "7_3": [
    "The player believes there might be a red key in box 3.",
    "The player believes that box 1 is empty.",
    "The player believes that box 2 would have a red key if box 3 is empty.",
    "The player believes there might be a key in box 2.",
    "The player knows that box 1 does not have the red key."
  ]
}

GOAL_PROMPT = "Which gem(s) are most likely to be the player's goal?"
STATEMENT_PROMPT = "Please rate the following statements about the agent's current beliefs:"
GOAL_OPTIONS = ["<icon>assets/icons/triangle.png</icon> Triangle", "<icon>assets/icons/square.png</icon> Square", "<icon>assets/icons/hexagon.png</icon> Hexagon", "<icon>assets/icons/circle.png</icon> Circle"]

STIMULI_SETS = [
    ["1_1_1", "1_1_2", "1_1_3"],
    ["1_2_1", "1_2_2", "1_2_3"],
    ["1_3_1", "1_3_2", "1_3_3"],
    ["2_1_1", "2_1_2", "2_1_3"],
    ["2_2_1", "2_2_2", "2_2_3"],
    ["2_3_1", "2_3_2", "2_3_3"],
    ["3_1_1", "3_1_2", "3_1_3", "3_1_4"],
    ["3_2_1", "3_2_2", "3_2_3"],
    ["3_3_1", "3_3_2", "3_3_3"],
    ["4_1_1", "4_1_2", "4_1_3"],
    ["4_2_1", "4_2_2", "4_2_3"],
    ["4_3_1", "4_3_2", "4_3_3"],
    ["5_1_1", "5_1_2", "5_1_3"],
    ["5_2_1", "5_2_2", "5_2_3"],
    ["6_1_1", "6_1_2"],
    ["6_2_1", "6_2_2", "6_2_3"],
    ["6_3_1", "6_3_2", "6_3_3"],
    ["7_1_1", "7_1_2", "7_1_3"],
    ["7_2_1", "7_2_2", "7_2_3"],
    ["7_3_1", "7_3_2", "7_3_3"]
      ]

TRIAL_TEMPLATE = """{
  "stimuli_id": "STIMULUS_ID",
  "input_type": "img",
  "media_url": [
    "ASSETS_URL"
  ],
  "commentary": "",
  "queries": QUERY_TEMPLATE
  }
  """
QUERY_TEMPLATE = """
 [
    {
      "prompt": GOAL_PROMPT,
      "type": "multi-select",
      "tag": "agent_goal",
      "options": GOAL_OPTIONS,
      "required": true
    },
    {
    "prompt": STATEMENT_PROMPT,
      "type": "multi-slider",
      "options": STATEMENT_OPTIONS,
      "slider_config": STATEMENT_SLIDER_CONFIG,
      "sampling_size": 2,
      "tag": "statement_rating",
      "randomize_order": true,
      "required": true
    }
  ]
"""

STATEMENT_SLIDER_CONFIG = {
        "min": 1,
        "max": 7,
        "default_value": 4,
        "labels": [
          { "value": 1, "label": "Extremely unlikely" },
          { "value": 7, "label": "Extremely likely" }
        ],
        "show_label_values": True,
        "required": True
      }

all_scenarios = []

for stimulus_set in STIMULI_SETS:
    for i, stimulus in enumerate(stimulus_set):
      scenario = TRIAL_TEMPLATE.replace("STIMULUS_ID", stimulus)
      query = QUERY_TEMPLATE
      if i < len(stimulus_set) - 1:
            query = query.replace("GOAL_PROMPT", json.dumps(GOAL_PROMPT))
            query = query.replace("STATEMENT_PROMPT", json.dumps(STATEMENT_PROMPT))
            query = query.replace("GOAL_OPTIONS", json.dumps(GOAL_OPTIONS))
            query = query.replace("STATEMENT_SLIDER_CONFIG", json.dumps(STATEMENT_SLIDER_CONFIG))
            query = query.replace("STATEMENT_OPTIONS", json.dumps(STATEMENTS[stimulus[:-2]]))
            scenario = scenario.replace("ASSETS_URL", f"assets/stimuli/{stimulus}.gif")
            scenario = scenario.replace("QUERY_TEMPLATE", query)
            all_scenarios.append(scenario)
      else: 
          scenario = scenario.replace("ASSETS_URL", f"assets/stimuli/{stimulus}.gif")
          scenario = scenario.replace("QUERY_TEMPLATE", "[]")
          all_scenarios.append(scenario)

with open("stimuli.jsonl", "w") as f:
    for scenario in all_scenarios:
        f.write(scenario + "\n")
