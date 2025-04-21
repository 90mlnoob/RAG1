import json
from agents.api_agent import call_api
from agents.browser_agent import perform_action

def execute_steps(parsed_steps_json: str):
    steps = json.loads(parsed_steps_json)

    for step in steps:
        if step["type"] == "api":
            call_api(step["endpoint"], step.get("params", {}))
        elif step["type"] == "browser":
            perform_action(step["action"], step["target"])
        else:
            print(f"[Unknown] Cannot handle step: {step}")
