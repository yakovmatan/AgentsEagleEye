from Manager import Manager


def menu():
    manager = Manager()
    while True:
        print("\n===== Eagle Eye Agent Manager =====")
        print("1. Add new agent")
        print("2. Update agent")
        print("3. Delete agent")
        print("4. Get agent by ID")
        print("5. List all agents")
        print("6. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            manager.add_agent_flow()
        elif choice == "2":
            manager.update_agent_flow()
        elif choice == "3":
            manager.delete_agent_flow()
        elif choice == "4":
            manager.get_agent_by_id_flow()
        elif choice == "5":
            manager.list_all_agents_flow()
        elif choice == "6":
            print("Existing...")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == '__main__':
    menu()