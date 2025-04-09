import heapq
import itertools

class Patient:
    def __init__(self,name,urgency_level):
        self.name = name
        self.urgency = urgency_level
    def __repr__(self):
        return f"Name: {self.name}, Urgency: {self.urgency}"

class Emergencyroom:
    def __init__(self):
        self.heap = []
        self.entryfinder = {}
        self.counter = itertools.count()
        self.REMOVED = "<removed>" # the built-in heapq does not support removing arbitrary elements efficiently

    # add patients
    def add_patient(self,name,urgency_level):
        if name in self.entryfinder:
            self.remove_patient(name)
        patient = Patient(name,urgency_level)
        count = next(self.counter)
        entry = [-urgency_level,count,patient] 
        self.entryfinder[name] = entry
        heapq.heappush(self.heap, entry)

    # remove patients
    def remove_patient(self,name):
        entry = self.entryfinder.pop(name)
        entry[-1] = self.REMOVED

    # see the most urgent patient
    def see_most_urgent(self):
        while self.heap:
            urgency_level, count, patient = self.heap[0]
            if patient is not self.REMOVED:
                return patient
            heapq.heappop(self.heap)
        return None
    
    # call the most urgent patient
    def call_most_urgent(self):
        while self.heap:
            urgency_level, count, patient = heapq.heappop(self.heap)
            if patient is not self.REMOVED:
                del self.entryfinder[patient.name]
                return patient
        return None
    
    # update patients' urgency level
    def update_urgency(self,name,new_urgency_level):
        if name in self.entryfinder:
            self.remove_patient(name)
        self.add_patient(name, new_urgency_level)
    

    # see top 10 most urgent patients
    def top_10_patients(self):
        temp = []
        result = []

        while self.heap and len(result) < 10:
            urgency, count, patient = heapq.heappop(self.heap)
            if patient != self.REMOVED:
                result.append(patient)
                temp.append([urgency, count, patient])

        for entry in temp:
            heapq.heappush(self.heap, entry)

        return result


def main():
        er = Emergencyroom()
        er.add_patient("Alice", 75)
        er.add_patient("Bob", 90)
        er.add_patient("Charlie", 90)
        er.add_patient("Diana", 60)

        print("Most urgent:", er.see_most_urgent())
        print("Top 10:", er.top_10_patients())

        er.update_urgency("Alice", 95)
        print("Most urgent after update:", er.see_most_urgent())

        print("Calling:", er.call_most_urgent())
        print("Calling next:", er.call_most_urgent())


if __name__ == "__main__":
    main()