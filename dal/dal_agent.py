from Models.Agent import Agent
from dal.dal_CRUD import DalCrud

class DalAgent:

    def __init__(self):
        self.dal = DalCrud(host="localhost", user="root", password="", database="eagleeyedb")

    def add_agent(self,agent: Agent):
        query = """
        INSERT INTO agents (codeName, realName, location, status, missionComplete)
        VALUES (%s, %s, %s, %s, %s)
        """
        params = (agent.code_name, agent.real_name, agent.location, agent.status, agent.missions_completed)
        new_id = self.dal.insert(query,params)
        agent.id = new_id
        return new_id

    def get_agent_by_id(self,agent_id: int):
        query = "SELECT * FROM agents WHERE id=%s"
        params = (agent_id,)
        result = self.dal.select(query,params)
        if result:
            row = result[0]
            return Agent(
                agent_id=row['id'],
                code_name=row['codeName'],
                real_name=row['realName'],
                location=row['location'],
                status=row['status'],
                missions_completed=row['missionsCompleted']
            )
        return None

    def get_all_agents(self):
        query = "SELECT * FROM agents"
        result = self.dal.select(query)
        agents = []
        for row in result:
            agents.append(Agent(
                agent_id=row['id'],
                code_name=row['codeName'],
                real_name=row['realName'],
                location=row['location'],
                status=row['status'],
                missions_completed=row['missionsCompleted']
            ))
        return agents

    def delete_agent(self, agent_id: int):
        query = "DELETE FROM agents WHERE id=%s"
        params = (agent_id,)
        return self.dal.delete(query,params)

    def update_agent(self, agent_id: int, fields_to_update: dict):
        set_clause = ", ".join(f"{field}=%s" for field in fields_to_update.keys())
        params = list(fields_to_update.values())
        params.append(agent_id)

        query = f"""
        UPDATE agents
        SET {set_clause}
        WHERE id=%s
        """
        return self.dal.delete(query, params)