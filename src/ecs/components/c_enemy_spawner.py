
class CEnemySpawner:
    def __init__(self, spawn_events: list):
        self.spawn_events = spawn_events
        for event in self.spawn_events:
            event["spawned"] = False
        self.current_time = 0.0
