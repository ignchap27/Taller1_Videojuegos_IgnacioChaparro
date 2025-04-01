import pygame
import random
import esper
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.c_enemy_spawner import CEnemySpawner

def system_enemy_spawner(world: esper.World, delta_time: float, enemies_cfg: dict):
    spawner_components = world.get_component(CEnemySpawner)

    for entity, spawner in spawner_components:
        spawner.current_time += delta_time

        for event in spawner.spawn_events:
            if not event["spawned"] and spawner.current_time >= event["time"]:
                enemy_def = enemies_cfg[event["enemy_type"]]

                size = pygame.Vector2(enemy_def["size"]["x"], enemy_def["size"]["y"])
                color = pygame.Color(enemy_def["color"]["r"],
                                     enemy_def["color"]["g"],
                                     enemy_def["color"]["b"])
                speed = random.uniform(enemy_def["velocity_min"], enemy_def["velocity_max"])

                velocity = pygame.Vector2(
                    random.choice([-1, 1]) * speed,
                    random.choice([-1, 1]) * speed
                )

                entity = world.create_entity()
                world.add_component(entity, CSurface(size, color))
                world.add_component(entity, CTransform(pygame.Vector2(event["position"]["x"], event["position"]["y"])))
                world.add_component(entity, CVelocity(velocity))

                event["spawned"] = True
