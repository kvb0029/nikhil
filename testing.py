import unittest
from main import OrganManagementSystem  # Import the main system

class TestOrganManagementSystem(unittest.TestCase):
    def setUp(self):
        """Set up a fresh instance of the system before each test."""
        self.system = OrganManagementSystem()

    def test_add_donor(self):
        """Test adding a donor."""
        donor = {"name": "John Doe", "age": 35, "organ": "Kidney", "blood_group": "A+"}
        self.system.donors.append(donor)
        self.assertEqual(len(self.system.donors), 1)
        self.assertEqual(self.system.donors[0], donor)

    def test_add_recipient(self):
        """Test adding a recipient."""
        recipient = {
            "name": "Alice Smith",
            "age": 28,
            "organ": "Liver",
            "blood_group": "O+",
            "urgency": 4,
        }
        self.system.recipients.append(recipient)
        self.assertEqual(len(self.system.recipients), 1)
        self.assertEqual(self.system.recipients[0], recipient)

    def test_match_organ_success(self):
        """Test a successful organ match."""
        self.system.donors = [
            {"name": "John Doe", "age": 35, "organ": "Kidney", "blood_group": "A+"}
        ]
        self.system.recipients = [
            {"name": "Alice Smith", "age": 30, "organ": "Kidney", "blood_group": "A+", "urgency": 5}
        ]
        self.system.match_organ()
        self.assertEqual(len(self.system.matches), 1)
        self.assertEqual(self.system.matches[0]["donor"]["name"], "John Doe")
        self.assertEqual(self.system.matches[0]["recipient"]["name"], "Alice Smith")

    def test_match_organ_failure(self):
        """Test an unsuccessful organ match."""
        self.system.donors = [
            {"name": "John Doe", "age": 35, "organ": "Kidney", "blood_group": "A+"}
        ]
        self.system.recipients = [
            {"name": "Alice Smith", "age": 30, "organ": "Liver", "blood_group": "O+", "urgency": 5}
        ]
        self.system.match_organ()
        self.assertEqual(len(self.system.matches), 0)

    def test_backup_and_restore(self):
        """Test backup and restore functionality."""
        self.system.donors = [
            {"name": "John Doe", "age": 35, "organ": "Kidney", "blood_group": "A+"}
        ]
        self.system.recipients = [
            {"name": "Alice Smith", "age": 28, "organ": "Liver", "blood_group": "O+", "urgency": 4}
        ]
        self.system.matches = [
            {
                "donor": self.system.donors[0],
                "recipient": self.system.recipients[0],
            }
        ]
        self.system.backup_data()

        # Clear all data
        self.system.donors = []
        self.system.recipients = []
        self.system.matches = []

        # Restore from backup
        self.system.restore_data()
        self.assertEqual(len(self.system.donors), 1)
        self.assertEqual(len(self.system.recipients), 1)
        self.assertEqual(len(self.system.matches), 1)

    def track_organ_demand(self):
        demand = {}
        for recipient in self.recipients:
            organ = recipient['organ']
            demand[organ] = demand.get(organ, 0) + 1
    
        print("Organ Demand Tracker:")
        for organ, count in demand.items():
            print(f"Organ: {organ}, Recipients Waiting: {count}")
        return demand  # Ensure the demand dictionary is returned


if __name__ == "__main__":
    unittest.main()
