from agent.agent import run_agent
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    print("💬 Write your health-related question:")
    query = input(">> ")
    response = run_agent(query)
    print("\n🤖 Agent Response:\n")
    print(response)

