import pygame

class GameEngine:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((640, 360), pygame.SCALED)
        self.clock = pygame.time.Clock()
        self.is_running = False
        self.frame_rate = 60
        self.delta_time = 0

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
        self.pos_cuad = pygame.Vector2(50, 200)
        self.vel_cuad = pygame.Vector2(20, 50)
        size_cuad = pygame.Vector2(50, 50)
        col_cuad = pygame.Color(0, 0, 0)

        self.surf_cuad = pygame.Surface(size_cuad)
        self.surf_cuad.fill(col_cuad)

    def _calculate_time(self):
        self.clock.tick(self.frame_rate)
        self.delta_time = self.clock.get_time() / 1000.0

    def _process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def _update(self):
        # Pixeles por segundo
        self.pos_cuad.x += self.vel_cuad.x * self.delta_time
        self.pos_cuad.y += self.vel_cuad.y * self.delta_time

    def _draw(self):
        self.screen.fill((0, 100, 200))

        self.screen.blit(self.surf_cuad, self.pos_cuad)

        pygame.display.flip()

    def _clean(self):
        pygame.quit()
