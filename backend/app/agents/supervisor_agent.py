from typing import TypedDict, Optional

from langgraph.graph import StateGraph, END
from sqlalchemy.orm import Session

from app.agents.knowledge_agent import knowledge_agent
from app.agents.email_agent import generate_email_draft
from app.agents.report_agent import generate_business_report
from app.agents.sales_agent import analyze_sales
from app.agents.crm_agent import analyze_customers


class SupervisorState(TypedDict):
    message: str
    route: str
    response: str
    db: Optional[Session]


def router_node(state: SupervisorState):
    message = state["message"].lower()

    if "email" in message or "draft" in message:
        return {"route": "email"}

    if "report" in message or "summary" in message:
        return {"route": "report"}

    if "sales" in message or "revenue" in message or "product" in message:
        return {"route": "sales"}

    if "customer" in message or "crm" in message or "client" in message:
        return {"route": "crm"}

    return {"route": "knowledge"}


def email_node(state: SupervisorState):
    email = generate_email_draft(
        recipient_name="Customer",
        purpose=state["message"],
        tone="professional"
    )
    return {"response": f"Subject: {email['subject']}\n\n{email['body']}"}


def report_node(state: SupervisorState):
    return {"response": generate_business_report(state["message"])}


def sales_node(state: SupervisorState):
    return {"response": analyze_sales(state["db"])}


def crm_node(state: SupervisorState):
    return {"response": analyze_customers(state["db"])}


def knowledge_node(state: SupervisorState):
    return {"response": knowledge_agent(state["message"])}


def choose_route(state: SupervisorState):
    return state["route"]


graph = StateGraph(SupervisorState)

graph.add_node("router", router_node)
graph.add_node("email", email_node)
graph.add_node("report", report_node)
graph.add_node("sales", sales_node)
graph.add_node("crm", crm_node)
graph.add_node("knowledge", knowledge_node)

graph.set_entry_point("router")

graph.add_conditional_edges(
    "router",
    choose_route,
    {
        "email": "email",
        "report": "report",
        "sales": "sales",
        "crm": "crm",
        "knowledge": "knowledge"
    }
)

graph.add_edge("email", END)
graph.add_edge("report", END)
graph.add_edge("sales", END)
graph.add_edge("crm", END)
graph.add_edge("knowledge", END)

supervisor_graph = graph.compile()


def supervisor_agent(message: str, db: Session) -> dict:
    result = supervisor_graph.invoke({
        "message": message,
        "route": "",
        "response": "",
        "db": db
    })

    return {
        "response": result["response"],
        "route": result["route"]
    }