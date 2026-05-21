from typing import TypedDict
from langgraph.graph import StateGraph, END


class hospitalState (TypedDict):
    patient_prompt: str
    risk_level : str
    retry_count: int
    status: str



def triage_node(state: hospitalState):
    
    print("Running triage...")

    prompt = state["patient_prompt"] #accedo al diccionario, al valor de patient_prompt

    print(prompt.lower())

    if "chest pain" in prompt.lower():

        return {
            "risk_level": "high",
            "status": "neeeds_review"
        }
    
    return {
        "risk_level": "low",
        "status": "stable"
    }

def route_patient(state: hospitalState):
    if state["risk_level"] == "high":
        return "doctor_review"
    return "discharge"


def doctor_review_node(state : hospitalState):
    print("Doctor review required")

    return {
        "stauts": "awaiting_doctor_confirm"
    }

def discharge_node(state: hospitalState):
    print ("Patient discharged")

    return {
        "status": "discharged"
    }





builder = StateGraph(hospitalState) #el objeto que le pasamos a compilar
builder.add_node ("triage", triage_node)
builder.set_entry_point("triage")
builder.add_edge("triage", END)

graph =builder.compile()



result = graph.invoke({
    "patient_prompt":"Patient reports chest pain",
    "risk_level": "",
    "retry_count": 0,
    "status": ""

})

print(result)


