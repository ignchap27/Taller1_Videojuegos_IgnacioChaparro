import pygame

class GameEngine:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600), pygame.SCALED)
        self.clock = pygame.time.Clock()
        self.lock_cuad = pygame.Rect(100, 100, 640, 380)
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
        self.pos_cuad = pygame.Vector2(-25, 200)
        self.vel_cuad = pygame.Vector2(200, 200)
        size_cuad = pygame.Vector2(50, 70)
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
        
        # test_rect = pygame.Rect(100, 100, 640, 380)  replaced by self.lock_cuad
        screen_rect = self.screen.get_rect()
        cuad_rect = self.surf_cuad.get_rect(topleft=self.pos_cuad)
        
        if cuad_rect.left < self.lock_cuad.left or cuad_rect.right > self.lock_cuad.right:
            self.vel_cuad.x *= -1
            cuad_rect.clamp_ip(self.lock_cuad)
            self.pos_cuad.x = cuad_rect.x
            
        if cuad_rect.top < self.lock_cuad.top or cuad_rect.bottom > self.lock_cuad.bottom:
            self.vel_cuad.y *= -1
            cuad_rect.clamp_ip(self.lock_cuad)
            self.pos_cuad.y = cuad_rect.y

    def _draw(self):
        self.screen.fill((0, 100, 200))

        # Draw test_rect with a border (red color)
        pygame.draw.rect(self.screen, (255, 0, 0), self.lock_cuad, 2)

        self.screen.blit(self.surf_cuad, self.pos_cuad)

        pygame.display.flip()

    def _clean(self):
        pygame.quit()
