class Marksheet:
    def __init__(self, name: str, scores: dict):
        self.name = name
        self.scores = scores
    def generate(self):
        total = sum(self.scores.values())
        print(f"Marksheet for {self.name}")
        for sub, score in self.scores.items():
            print(f"{sub}: {score}")
        print(f"Total: {total}")

if __name__ == "__main__":
    m = Marksheet("Alice", {"Math": 95, "Science": 88})
    m.generate()
