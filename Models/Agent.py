class Agent:

    def __init__(self,code_name,real_name,location,status,missions_completed,agent_id=None):
        self.id = agent_id
        self.code_name = code_name
        self.real_name = real_name
        self.location = location
        self.status = status
        self.missions_completed = missions_completed

    def __str__(self):
        return (f"\nID: {self.id}, \nCode Name: {self.code_name}, \nReal Name: {self.real_name}, "
                f"Location: {self.location}, \nStatus: {self.status}, \nMissions Completed: {self.missions_completed}")

