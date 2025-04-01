import pygame
import esper
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity

def system_bounce(world:esper.world, screen:pygame.Surface, lock_cuad:pygame.Rect):
    components = world.get_components(CTransform, CVelocity, CSurface)
    
    c_t:CTransform
    c_v:CVelocity
    c_s:CSurface
    
    for entity, (c_t, c_v, c_s) in components:
        cuad_rect = c_s.surf.get_rect(topleft=c_t.pos)
        
        if cuad_rect.left < lock_cuad.left or cuad_rect.right > lock_cuad.right:
            c_v.vel.x *= -1
            cuad_rect.clamp_ip(lock_cuad)
            c_v.vel.x = cuad_rect.x
            
        if cuad_rect.top < lock_cuad.top or cuad_rect.bottom > lock_cuad.bottom:
            c_v.vel.y *= -1
            cuad_rect.clamp_ip(lock_cuad)
            c_t.pos.y = cuad_rect.y
