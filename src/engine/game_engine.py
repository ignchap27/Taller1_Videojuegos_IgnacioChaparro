import pygame
import esper
import json
from src.ecs.components.c_enemy_spawner import CEnemySpawner
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.systems.s_bounce import system_bounce
from src.ecs.systems.s_enemy_spawner import system_enemy_spawner
from src.ecs.systems.s_movement import system_movement
from src.ecs.systems.s_rendering import system_rendering

class GameEngine:
    def __init__(self) -> None:
        pygame.init()
        
        #Indicar que cfg usar
        cfg = "cfg_00"
        
        #Cargar configuracion de window de cfg
        with open(f"verificacion/{cfg}/window.json") as f:
            window_cfg = json.load(f)
        
        #Cargar config enemies de cfg
        with open(f"verificacion/{cfg}/enemies.json") as f:
            self.enemies_cfg = json.load(f)
            
        #Cargar config level de cfg
        with open(f"verificacion/{cfg}/level_01.json") as f:
            self.level_cfg = json.load(f)
        
        self.screen = pygame.display.set_mode(
            (window_cfg["size"]["w"], window_cfg["size"]["h"]), pygame.SCALED)
        pygame.display.set_caption(window_cfg["title"])
        self.bg_color = (
            window_cfg["bg_color"]["r"],
            window_cfg["bg_color"]["g"],
            window_cfg["bg_color"]["b"],
        )
        
        self.clock = pygame.time.Clock()
        self.is_running = False
        self.frame_rate = window_cfg["framerate"]
        self.delta_time = 0
        
        self.ecs_world = esper.World()
        

    def run(self) -> None:
        self._create()
        self.is_running = True
        while self.is_running:
            self._calculate_time()
            self._process_events()
            self._update()
            self._draw()
        self._clean()

    def _create(self):
        spawner_entity = self.ecs_world.create_entity()
        self.ecs_world.add_component(spawner_entity, CEnemySpawner(self.level_cfg["enemy_spawn_events"]))

    def _calculate_time(self):
        self.clock.tick(self.frame_rate)
        self.delta_time = self.clock.get_time() / 1000.0

    def _process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def _update(self):
        system_movement(self.ecs_world, self.delta_time)
        system_bounce(self.ecs_world, self.screen)
        system_enemy_spawner(self.ecs_world, self.delta_time, self.enemies_cfg)

    def _draw(self):
        self.screen.fill((0, 100, 200))
        
        system_rendering(self.ecs_world, self.screen)

        pygame.display.flip()

    def _clean(self):
        pygame.quit()
