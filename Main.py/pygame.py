import pygame, math, sys

pygame.init()
s = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
W, H, clock = s.get_width(), s.get_height(), pygame.time.Clock()

# particles: [x, y, old_x, old_y, pinned]
P = [[x*20+W/4, y*20+100, x*20+W/4, y*20+100, y==0] for y in range(30) for x in range(50)]
# springs between neighbors (i,i+1) and (i,i+50)
S = [[i, i+1, 20] for i in range(len(P)) if (i+1)%50] + [[i, i+50, 20] for i in range(len(P)-50)]

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    s.fill((0, 5, 10))
    mx, my = pygame.mouse.get_pos()
    md = pygame.mouse.get_pressed()

    # verlet integration
    for p in P:
        if not p[4]:
            if md[0] and math.hypot(p[0]-mx, p[1]-my) < 30:
                p[0], p[1] = mx, my
            vx = (p[0]-p[2]) * 0.99
            vy = (p[1]-p[3]) * 0.99
            p[2], p[3] = p[0], p[1]
            p[0] += max(-20, min(20, vx))
            p[1] += max(-20, min(20, vy)) + 0.4

    # constraint relaxation
    for _ in range(6):
        for sk in S:
            p1, p2 = P[sk[0]], P[sk[1]]
            dx, dy = p2[0]-p1[0], p2[1]-p1[1]
            d = math.hypot(dx, dy) or 0.1
            target = sk[2]
            diff = (d - target) / d * 0.5
            if not p1[4]:
                p1[0] += dx * diff
                p1[1] += dy * diff
            if not p2[4]:
                p2[0] -= dx * diff
                p2[1] -= dy * diff

    # draw springs and particles
    for sk in S:
        p1, p2 = P[sk[0]], P[sk[1]]
        pygame.draw.aaline(s, (20, 120, 100), (p1[0], p1[1]), (p2[0], p2[1]))
    for p in P:
        color = (200, 50, 50) if p[4] else (240,240,240)
        pygame.draw.circle(s, color, (int(p[0]), int(p[1])), 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
        