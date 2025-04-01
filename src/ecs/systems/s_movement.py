import esper
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity


def system_movements(world:esper.World, delta_time:float):
    components = world.get_components(CVelocity, CTransform)
    
    c_t:CTransform
    c_v:CVelocity
    
    for entity, (c_t, c_v) in components:
        c_t.pos.x += c_v.vel.x * delta_time
        c_t.pos.y += c_v.vel.y * delta_time