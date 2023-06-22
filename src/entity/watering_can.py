import pygame

from src.settings import IMAGE_FOLDER_PATH, PLAYER_TEXTURE_SIZE


class WateringCan(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        direction = player.status.split("_")[0]
        print(direction)

        # graphic
        full_path = IMAGE_FOLDER_PATH + f"/watering_cans/{direction}.png"
        self.image = pygame.image.load(full_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, PLAYER_TEXTURE_SIZE)

        # placement
        if direction == "right":
            self.rect = self.image.get_rect(midleft=player.rect.midright)
        elif direction == "left":
            self.rect = self.image.get_rect(midright=player.rect.midleft)
        elif direction == "down":
            self.rect = self.image.get_rect(midtop=player.rect.midbottom)
        else:
            self.rect = self.image.get_rect(midbottom=player.rect.midtop)
