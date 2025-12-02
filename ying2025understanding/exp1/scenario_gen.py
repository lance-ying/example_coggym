import json

STATEMENTS = {
  "1_1": [
    "The player initially believed that box 3 contained a blue key.",
    "The player initially believed that box 1 and 2 contained no blue key.",
    "The player initially believed that box 1 might have the blue key.",
    "The player initially believed the blue key was not in box 2.",
    "The player initially thought that there may have been a key in box 2."
  ],
  "1_2": [
    "The player initially believed that box 3 contained a blue key.",
    "The player initially believed that box 1 might have the blue key.",
    "The player initially had no idea which box contained a blue key.",
    "The player initially believed that 1 of the boxes had a blue key.",
    "The player initially believed that box 1 and 2 contained no blue key."
  ],
  "1_3": [
    "The player initially believed that box 2 contained a blue key.",
    "The player initially believed that the first box is empty and held no key.",
    "The player initially believed there was an equal chance of the key being in box 1, box 2, or box 3.",
    "The player initially thought that there may have been a key in box 2.",
    "The player initially believed that box 3 was empty."
  ],
  "2_1": [
    "The player initially did not believe box 3 had a red key.",
    "The player initially knew that box 3 did not have the red key.",
    "The player initially thought that box 2 contained a red key.",
    "The player initially believed the red key was in box 1.",
    "The player initially did not know if box 2 had a key."
  ],
  "2_2": [
    "The player initially believed that box 2 was more likely to contain a red key than box 1 and box 3.",
    "The player initially thought that box 1 most likely contained a red key.",
    "The player initially thought box 3 had the red key.",
    "The player initially believed that box 1 was empty.",
    "The player initially believed that box 3 was empty."
  ],
  "2_3": [
    "The player initially thought that box 1 most likely contained a red key.",
    "The player initially expected to find a key in box 3.",
    "The player initially thought that box 2 contained a red key.",
    "The player initially knew there would be a red key in 1 of the boxes.",
    "The player initially thought that box 2 did not contain a red key."
  ],
  "3_1": [
    "The player initially believed there was no key in box 1.",
    "The player initially knew there was a blue key in box 1, box 2, or box 3.",
    "The player initially believed box 1 was empty.",
    "The player initially knew there was a key in box 2 or box 3.",
    "The player initially believed there might be a chance of seeing a key in box 2."
  ],
  "3_2": [
    "The player initially did not know which box might contain a red key.",
    "The player initially believed there might be a key in box 1.",
    "The player initially believed that box 1 was empty.",
    "The player initially did not know the color of the key in box 3.",
    "The player initially believed a red key was most likely in box 2."
  ],
  "3_3": [
    "The player initially knew that box 1 did not have a red key.",
    "The player initially believed a blue key was more likely to be inside box 2 than box 1 or box 3.",
    "The player initially believed box 1 was not empty.",
    "The player initially believed a red key was most likely in box 2.",
    "The player initially knew that box 1 did not have the blue key."
  ],
  "4_1": [
    "The player initially did not have confidence box 1 would hold the red key.",
    "The player initially believed that both box 2 and 3 must each contain a red key.",
    "The player initially believed box 2 and 3 might be empty.",
    "The player initially believed they could get a red key in box 2 or 3.",
    "The player initially believed that box 1 did not contain a red key."
  ],
  "4_2": [
    "The player initially believed that there was a key in box 2.",
    "The player initially believed a red key was more likely to be in box 2 or 3 than box 1.",
    "The player initially believed a red key was most likely in box 2.",
    "The player initially believed that box 1 had a red key.",
    "The player initially believed that either box 1 or 2 contained a key."
  ],
  "4_3": [
    "The player initially believed that either box 1 and 2 contained the red key.",
    "The player initially did not know if box 3 contained a red key.",
    "The player initially believed there might be a key in box 1.",
    "The player initially did not know for sure which box contained a key.",
    "The player initially thought that box 2 might have the red key."
  ],
  "5_1": [
    "The player initially knew that there was a key in box 1.",
    "The player initially knew that box 1 did not have a red key.",
    "The player initially believed that box 2 was empty.",
    "The player initially thought that box 2 might have the red key.",
    "The player initially believed a red key was more likely to be in box 2 or 3 than box 1."
  ],
  "5_2": [
    "The player initially believed there might be a key in box 1.",
    "The player initially believed a red key was more likely to be in box 2 or 3 than box 1.",
    "The player initially did not know for sure which box contained the key.",
    "The player initially believed that either box 1 or 2 contained the red key.",
    "The player initially believed that box 2 had a red key."
  ],
  "6_1": [
    "The player initially knew that there was a key in box 1.",
    "The player initially believed that box 1 might contain a blue key or a red key.",
    "The player initially believed that a red key would be located in either box 1 or box 2.",
    "The player initially thought that box 1 was empty.",
    "The player initially believed that box 2 was empty."
  ],
  "6_2": [
    "The player initially believed that either box 1 or 2 contained the blue key.",
    "The player initially believed that box 1 and 2 contained no blue key.",
    "The player initially believed that box 2 had a red key.",
    "The player initially believed that box 1 had a red key.",
    "The player initially believed there was a blue key in either box 1 or box 2."
  ],
  "6_3": [
    "The player initially believed that box 2 was empty.",
    "The player was initially unsure about the contents of boxes 1 and 2.",
    "The player initially believed box 1 had a red key.",
    "The player initially believed that box 2 had a red key.",
    "The player initially believed there might be a key in box 1."
  ],
  "7_1": [
    "The player initially believed box 1 had a red key.",
    "The player initially believed that box 2 might have a red key.",
    "The player initially thought that boxes 2 or 3 contained a key.",
    "The player initially thought that box 1 was empty.",
    "The player initially believed box 2 and 3 might be empty."
  ],
  "7_2": [
    "The player initially believed box 2 and 3 might be empty.",
    "The player initially thought that box 1 was most likely to contain a red key.",
    "The player initially did not have confidence box 1 would hold the red key.",
    "The player initially believed there was a red key in box 2.",
    "The player initially believed the red key could be in box 2."
  ],
  "7_3": [
    "The player initially believed that box 2 was empty.",
    "The player initially believed box 2 and 3 might be empty.",
    "The player initially believed that box 2 had a red key.",
    "The player was initially unsure what box contained the red key.",
    "The player initially believed box 1 had a red key."
  ]
}

GOAL_PROMPT = "Which gem(s) are most likely to be the player's goal?"
STATEMENT_PROMPT = "Please rate the following statements about the agent's initial beliefs:"
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
  "id": "STIMULUS_ID",
  "stimuli": [
    {
      "input_type": "img",
      "media_url": [
        "ASSETS_URL"
      ]
    }
  ],
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

with open("trial.jsonl", "w") as f:
    for scenario in all_scenarios:
        f.write(scenario + "\n")
