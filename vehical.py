class Vehicle:
    def __init__(self, vehicle_id, owner_name, owner_contact):
        self.vehicle_id = vehicle_id
        self.owner_name = owner_name
        self.owner_contact = owner_contact


class StolenVehicleRecord:
    def __init__(self, vehicle, date_reported):
        self.vehicle = vehicle
        self.date_reported = date_reported


class StolenVehicleTracker:
    def __init__(self):
        self.records = {}

    def record_stolen_vehicle(self, vehicle, date_reported):
        if vehicle.vehicle_id in self.records:
           return False  # Duplicate entry
        self.records[vehicle.vehicle_id] = StolenVehicleRecord(vehicle, date_reported)
        return True
    
    def retrieve_record(self, vehicle_id):
        return self.records.get(vehicle_id)
    
    def update_record(self, vehicle_id, new_date_reported):
        if vehicle_id in self.records:
            self.records[vehicle_id].date_reported = new_date_reported
            return True
        return False

    
    def delete_record(self, vehicle_id):
        if vehicle_id in self.records:
              del self.records[vehicle_id]
              return True
        return False
        

    
    def notify_owners(self, vehicle_id):
        if vehicle_id in self.records:
            record = self.retrieve_record(vehicle_id)
            vehicle = record.vehicle
            return f"Contacting {vehicle.owner_name} at {vehicle.owner_contact}: Notification: Your vehicle {vehicle.vehicle_id} has been reported stolen."
        return None


import unittest

class TestStolenVehicleTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = StolenVehicleTracker()
        self.vehicle1 = Vehicle("VH001", "John Doe", "555-0101")
        self.vehicle2 = Vehicle("VH002", "Jane Smith", "555-0202")

    def test_record_stolen_vehicle(self):
        self.assertTrue(self.tracker.record_stolen_vehicle(self.vehicle1, "2023-01-01"))
        self.assertFalse(self.tracker.record_stolen_vehicle(self.vehicle1, "2023-01-01"))  # Duplicate entry

    def test_retrieve_record(self):
        self.tracker.record_stolen_vehicle(self.vehicle1, "2023-01-01")
        record = self.tracker.retrieve_record("VH001")
        self.assertEqual(record.vehicle, self.vehicle1)

    def test_update_record(self):
        self.tracker.record_stolen_vehicle(self.vehicle1, "2023-01-01")
        self.assertTrue(self.tracker.update_record("VH001", "2023-01-02"))
        self.assertEqual(self.tracker.retrieve_record("VH001").date_reported, "2023-01-02")

    def test_delete_record(self):
        self.tracker.record_stolen_vehicle(self.vehicle1, "2023-01-01")
        self.assertTrue(self.tracker.delete_record("VH001"))
        self.assertIsNone(self.tracker.retrieve_record("VH001"))

    def test_notify_owners(self):
        self.tracker.record_stolen_vehicle(self.vehicle1, "2023-01-01")
        notification = self.tracker.notify_owners("VH001")
        expected_message = "Contacting John Doe at 555-0101: Notification: Your vehicle VH001 has been reported stolen."
        self.assertEqual(notification, expected_message)

if __name__ == "__main__":
    unittest.main()
   
    
