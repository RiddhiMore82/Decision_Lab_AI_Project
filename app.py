from rich import print

from core.state import create_state

from agents.planner import planner_agent
from agents.clarification import clarification_agent

from agents.financial import financial_agent
from agents.risk import risk_agent
from agents.devil import devil_agent

from agents.synthesizer import synthesizer_agent


print("=" * 60)
print("🧠 Decision Lab — AI Boardroom")
print("=" * 60)

# Get user decision
decision = input("\nWhat decision are you trying to make?\n> ")

# Create state
state = create_state(decision)

# Planner
state["planner"] = planner_agent(state["decision"])

print("\n[bold cyan]📋 Planner Report[/bold cyan]")
print(state["planner"])

# Clarification
state = clarification_agent(state)

print("\n[bold green]📦 User Context[/bold green]")
print(state["user_context"])

print("\n[bold yellow]👥 Expert Panel[/bold yellow]")

# Expert reports
reports = {}

reports["financial"] = financial_agent(
    state["decision"],
    state["planner"],
    state["user_context"]
)

print("\n[bold]💰 Financial Analyst[/bold]")
print(reports["financial"])

reports["risk"] = risk_agent(
    state["decision"],
    state["planner"],
    state["user_context"]
)

print("\n[bold]⚠️ Risk Analyst[/bold]")
print(reports["risk"])

reports["devil"] = devil_agent(
    state["decision"],
    state["planner"],
    state["user_context"]
)

print("\n[bold]😈 Devil's Advocate[/bold]")
print(reports["devil"])

# Final synthesis
print("\n[bold magenta]🏛 Chairperson[/bold magenta]")

final_report = synthesizer_agent(
    state["decision"],
    state["planner"],
    reports
)

print(final_report)