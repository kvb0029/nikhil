import csv
import json
from datetime import datetime


class OrganManagementSystem:
    def __init__(self):
        self.donors = []
        self.recipients = []
        self.matches = []
        self.logs = []

    def log_action(self, action):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.logs.append(f"{timestamp} - {action}")

    def add_donor(self):
        name = input("Enter donor name: ")
        age = int(input("Enter donor age: "))
        organ = input("Enter organ to donate: ")
        blood_group = input("Enter donor blood group: ")

        for donor in self.donors:
            if donor['name'].lower() == name.lower() and donor['organ'].lower() == organ.lower():
                print("Duplicate donor detected! Donor already exists.")
                return

        self.donors.append({"name": name, "age": age, "organ": organ, "blood_group": blood_group})
        print("Donor added successfully!")
        self.log_action(f"Added donor: {name}, Age: {age}, Organ: {organ}, Blood Group: {blood_group}")

    def add_recipient(self):
        name = input("Enter recipient name: ")
        age = int(input("Enter recipient age: "))
        organ = input("Enter organ needed: ")
        blood_group = input("Enter recipient blood group: ")

        for recipient in self.recipients:
            if recipient['name'].lower() == name.lower() and recipient['organ'].lower() == organ.lower():
                print("Duplicate recipient detected! Recipient already exists.")
                return

        urgency = int(input("Enter urgency level (1 to 5, where 5 is most urgent): "))
        self.recipients.append({"name": name, "age": age, "organ": organ, "blood_group": blood_group, "urgency": urgency})
        print("Recipient added successfully!")
        self.log_action(f"Added recipient: {name}, Age: {age}, Organ: {organ}, Blood Group: {blood_group}, Urgency: {urgency}")

    def update_donor(self):
        name = input("Enter donor name to update: ")
        for donor in self.donors:
            if donor['name'].lower() == name.lower():
                print(f"Current details: {donor}")
                donor['name'] = input("Enter new name (or press Enter to keep current): ") or donor['name']
                donor['age'] = int(input("Enter new age (or press Enter to keep current): ") or donor['age'])
                donor['organ'] = input("Enter new organ (or press Enter to keep current): ") or donor['organ']
                donor['blood_group'] = input("Enter new blood group (or press Enter to keep current): ") or donor['blood_group']
                print("Donor details updated!")
                self.log_action(f"Updated donor: {donor}")
                return
        print("Donor not found.")

    def update_recipient(self):
        name = input("Enter recipient name to update: ")
        for recipient in self.recipients:
            if recipient['name'].lower() == name.lower():
                print(f"Current details: {recipient}")
                recipient['name'] = input("Enter new name (or press Enter to keep current): ") or recipient['name']
                recipient['age'] = int(input("Enter new age (or press Enter to keep current): ") or recipient['age'])
                recipient['organ'] = input("Enter new organ (or press Enter to keep current): ") or recipient['organ']
                recipient['blood_group'] = input("Enter new blood group (or press Enter to keep current): ") or recipient['blood_group']
                recipient['urgency'] = int(input("Enter new urgency level (1 to 5): ") or recipient['urgency'])
                print("Recipient details updated!")
                self.log_action(f"Updated recipient: {recipient}")
                return
        print("Recipient not found.")

    def match_organ(self):
        if not self.donors or not self.recipients:
            print("No donors or recipients available for matching.")
            return

        for recipient in sorted(self.recipients, key=lambda x: (-x['urgency'], x['age'])):
            matched_donor = next(
                (donor for donor in self.donors
                 if donor['organ'] == recipient['organ']
                 and donor['blood_group'] == recipient['blood_group']
                 and abs(donor['age'] - recipient['age']) <= 10),
                None
            )
            if matched_donor:
                print(f"Match found! Donor {matched_donor['name']} can donate {matched_donor['organ']} to Recipient {recipient['name']}.")
                self.matches.append({"donor": matched_donor, "recipient": recipient})
                self.log_action(f"Matched donor {matched_donor['name']} with recipient {recipient['name']}.")
            else:
                print(f"No match found for Recipient {recipient['name']}.")

    def view_donors(self):
        print("List of Donors:")
        for donor in self.donors:
            print(f"Name: {donor['name']}, Age: {donor['age']}, Organ: {donor['organ']}, Blood Group: {donor['blood_group']}")
        self.log_action("Viewed donors list.")

    def view_recipients(self):
        print("List of Recipients:")
        for recipient in self.recipients:
            print(f"Name: {recipient['name']}, Age: {recipient['age']}, Organ: {recipient['organ']}, Blood Group: {recipient['blood_group']}, Urgency: {recipient['urgency']}")
        self.log_action("Viewed recipients list.")

    def view_matches(self):
        print("List of Matches:")
        if self.matches:
            for match in self.matches:
                print(f"Donor: {match['donor']['name']} -> Recipient: {match['recipient']['name']}")
        else:
            print("No matches available.")
        self.log_action("Viewed matches list.")

    def track_organ_demand(self):
        demand = {}
        for recipient in self.recipients:
            organ = recipient['organ']
            demand[organ] = demand.get(organ, 0) + 1

        print("Organ Demand Tracker:")
        for organ, count in demand.items():
            print(f"Organ: {organ}, Recipients Waiting: {count}")
        self.log_action("Tracked organ demand.")

    def backup_data(self):
        data = {
            "donors": self.donors,
            "recipients": self.recipients,
            "matches": self.matches,
            "logs": self.logs
        }
        with open("backup.json", "w") as file:
            json.dump(data, file, indent=4)
        print("System data backed up successfully!")
        self.log_action("System data backed up.")

    def restore_data(self):
        try:
            with open("backup.json", "r") as file:
                data = json.load(file)
                self.donors = data.get("donors", [])
                self.recipients = data.get("recipients", [])
                self.matches = data.get("matches", [])
                self.logs = data.get("logs", [])
            print("System data restored successfully!")
            self.log_action("System data restored.")
        except FileNotFoundError:
            print("No backup file found.")

    def view_logs(self):
        print("Activity Logs:")
        if self.logs:
            for log in self.logs:
                print(log)
        else:
            print("No logs available.")

    def main_menu(self):
        while True:
            print("\nOrgan Management System")
            print("1. Add Donor")
            print("2. Add Recipient")
            print("3. Update Donor")
            print("4. Update Recipient")
            print("5. Match Organ")
            print("6. View Donors")
            print("7. View Recipients")
            print("8. View Matches")
            print("9. Track Organ Demand")
            print("10. Backup Data")
            print("11. Restore Data")
            print("12. View Logs")
            print("13. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_donor()
            elif choice == '2':
                self.add_recipient()
            elif choice == '3':
                self.update_donor()
            elif choice == '4':
                self.update_recipient()
            elif choice == '5':
                self.match_organ()
            elif choice == '6':
                self.view_donors()
            elif choice == '7':
                self.view_recipients()
            elif choice == '8':
                self.view_matches()
            elif choice == '9':
                self.track_organ_demand()
            elif choice == '10':
                self.backup_data()
            elif choice == '11':
                self.restore_data()
            elif choice == '12':
                self.view_logs()
            elif choice == '13':
                print("Exiting Organ Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    system = OrganManagementSystem()
    system.main_menu()
