from agents.clinical_agent import clinical_agent
from tools.medical_extract import medical_extract_tool
import json


def run_clinical_workflow():

    max_retries = 2
    retry_count = 0

    while retry_count < max_retries:

        decision = clinical_agent()
        
        
        try:

            decision = json.loads(decision)

        except json.JSONDecodeError:

            retry_count += 1

            print(f"Invalid JSON. Retry {retry_count}")

            continue


        if "tool" not in decision:

            retry_count += 1

            print(f"No tool specified. Retry {retry_count}")

            continue


        if decision["tool"] == "medical_extract":

            result = medical_extract_tool()


            if result["return_code"] != 0:

                retry_count += 1

                print(f"Tool execution failed. Retry {retry_count}")

                continue


            return result


        else:

            return {
                "error": "tool not found"
            }


    return {
        "error": "Max retries exceeded",
        "decision" : "escalate to human"
    }

print(run_clinical_workflow())