from Models.Agent import Agent
from dal.dal_agent import DalAgent

class Manager:

    def __init__(self):
        self.manager = DalAgent()

    @staticmethod
    def input_int(prompt):
        while True:
            val = input(prompt).strip()
            if val.isdigit():
                return int(val)
            print("Invalid input, please enter a number")

    @staticmethod
    def input_status():
        valid_statuses = ["Active", "Injured", "Missing", "Retired"]
        while True:
            status = input(f"Status ({'/'.join(valid_statuses)}): ").strip()
            if status in valid_statuses:
                return status
            print(f"Invalid status. Choose from {valid_statuses}.")

    def add_agent_flow(self):
        code_name = input("code name: ")
        real_name = input("Real name: ")
        location = input("Location: ")
        status = Manager.input_status()
        mission_completed = Manager.input_int("Missions completed (number): ")

        agent = Agent(
            code_name=code_name,
            real_name=real_name,
            location=location,
            status=status,
            missions_completed=mission_completed
        )

        new_id = self.manager.add_agent(agent)
        print(f"Agent added with ID {new_id}")

    def update_agent_flow(self):
        print("=== Update Agent ===")
        agent_id = Manager.input_int("Enter the ID of the agent to update: ")

        fields_to_update = {}

        print("\nLeave empty to skip updating a field.\n")

        code_name = input("New code name (leave empty to skip): ")
        if code_name:
            fields_to_update["codeName"] = code_name

        real_name = input("New real name (leave empty to skip): ")
        if real_name:
            fields_to_update["realName"] = real_name

        location = input("New location (leave empty to skip): ")
        if location:
            fields_to_update["location"] = location

        status = input("New status (Active/Injured/Missing/Retired) (leave empty to skip): ")
        if status:
            fields_to_update["status"] = status

        missions_completed = Manager.input_int("New missions completed (leave empty to skip): ")
        if missions_completed:
            fields_to_update["missionsCompleted"] = missions_completed

        if not fields_to_update:
            print("No fields selected for update.")
            return

        updated_rows = self.manager.update_agent(agent_id, fields_to_update)
        if updated_rows:
            print(f"Agent {agent_id} updated successfully.")
        else:
            print("Update failed or no rows affected.")

    def delete_agent_flow(self):
        agent_id = Manager.input_int("Enter agent ID to delete: ")
        rows = self.manager.delete_agent(agent_id)
        if rows:
            print(f"Agent {agent_id} deleted.")
        else:
            print(f"No agent found with ID {agent_id}.")

    def get_agent_by_id_flow(self):
        agent_id = Manager.input_int("Enter agent ID to fetch: ")
        agent = self.manager.get_agent_by_id(agent_id)
        if agent:
            print(f"ID: {agent.id}")
            print(f"Code Name: {agent.codeName}")
            print(f"Real Name: {agent.realName}")
            print(f"Location: {agent.location}")
            print(f"Status: {agent.status}")
            print(f"Missions Completed: {agent.missionsCompleted}")
        else:
            print("Agent not found.")

    def list_all_agents_flow(self):
        agents = self.manager.get_all_agents()
        if not agents:
            print("No agents found.")
        else:
            for a in agents:
                print(
                    f"{a.agent_id}: {a.code_name} ({a.real_name}), {a.status} at {a.location}, Missions: {a.missionsCompleted}")