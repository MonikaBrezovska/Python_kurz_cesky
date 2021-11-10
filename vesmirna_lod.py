import pyglet
batch = pyglet.graphics.Batch()
sprite1 = pyglet.sprite.Sprite(obrazek, batch=batch)
sprite2 = pyglet.sprite.Sprite(obrazek, batch=batch)

# a potom můžeš vykreslit všechny najednou:
batch.draw()