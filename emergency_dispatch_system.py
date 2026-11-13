import heapq
import time

class IncidentIntakeQueue:
    def __init__(self):
        self.heap = []
        self.arrivalCounter = 0
        self.priorityMap = {"CRITICAL": 1, "ROUTINE": 2}

    def append(self, urgency, description):
        if urgency is None or str(urgency).strip().upper() not in self.priorityMap:
            print("Incident was not added. Please enter CRITICAL or ROUTINE urgency.")
            return

        urgency = str(urgency).strip().upper()
        self.arrivalCounter += 1
        heapq.heappush(self.heap, (self.priorityMap[urgency], self.arrivalCounter, description))
        print(f"{self.arrivalCounter}. {description} has been added to the queue. ({urgency})")

    def dispatch(self):
        if not self.heap:
            print("No incidents are waiting to be dispatched.")
            return None

        priority, number, description = heapq.heappop(self.heap)
        print(f"{number}. {description} has been dispatched.")
        return description

# incident intake
intake = IncidentIntakeQueue()

intake.append("Routine", "Minor fender-bender on Main Rd")
intake.append("Routine", "Noise complaint in Oak Suburb")
intake.append("Critical", "Cardiac arrest at Civic Centre")
intake.append("Critical", "Structure fire with trapped occupants on 4th Ave")

print()
# dispatch queue
print("Dispatch queue")
while intake.heap:
    intake.dispatch()

print()
print("--empty queue test--")
intake.dispatch()

print()
print("--invalid urgency tests--")
intake.append(None, "Incident with no urgency")
intake.append("Urgent", "Incident with an invalid urgency")


# Vehicle and crew lookup (Hash table)
class VehicleRegistry:
    def __init__(self):
        self.fleet = {}

    def register_vehicle(self, regNumber, unitType, crewLead, status):
        self.fleet[regNumber] = {
            "unitType": unitType,
            "crewLead": crewLead,
            "status": status
        }
        print(f"(REGISTERED) {regNumber} ({unitType}) - Status: {status}")

    def lookup_vehicle(self, reg_number):
        if reg_number in self.fleet:
            details = self.fleet[reg_number]
            print(f"Registration: {reg_number}")
            print(f"Type: {details['unitType']}")
            print(f"Crew: {details['crewLead']}")
            print(f"Status: {details['status']}")
            return details
        print(f"Vehicle {reg_number} was not found.")
        return None

print()
registry = VehicleRegistry()

registry.register_vehicle("AMB-101", "Ambulance", "Paramedic Dlamini", "Available")
registry.register_vehicle("FIRE-204", "Fire Engine", "Capt. Botha", "On Call - 4th Ave")
registry.register_vehicle("TRF-309", "Traffic Unit", "Officer Jacobs", "Patrolling")

print()
print("--lookup test--")
registry.lookup_vehicle("FIRE-204")

print()
print("--unknown vehicle test--")
registry.lookup_vehicle("UNKNOWN-000")



# This function compares how fast a dictionary lookup is against a list search.
def compare_lookup_performance(size):
    registry = VehicleRegistry()
    vehicles = []

    # Create a dictionary and a list with the same vehicle records.
    for i in range(size):
        reg_number = f"VEH-{i}"
        vehicle = {
            "reg": reg_number,
            "unitType": "Ambulance",
            "crewLead": "Crew",
            "status": "Available"
        }
        registry.fleet[reg_number] = vehicle
        vehicles.append(vehicle)

    # We test the last item because it is the worst case for a list search.
    target = f"VEH-{size - 1}"

    # Measure dictionary lookup time.
    start = time.perf_counter()
    registry.fleet.get(target)
    hash_time = (time.perf_counter() - start) * 1000

    # Measure list search time.
    start = time.perf_counter()
    for vehicle in vehicles:
        if vehicle["reg"] == target:
            break
    list_time = (time.perf_counter() - start) * 1000

    return hash_time, list_time

print("\n--- 2.5 Lookup Performance Comparison ---")
print("Dataset Size | Hash Table (ms) | List Search (ms)")
print("-------------------------------------------")

for dataset_size in [5000, 50000]:
    hash_time, list_time = compare_lookup_performance(dataset_size)
    print(f"{dataset_size:<12} | {hash_time:<15.6f} | {list_time:<15.6f}")

    