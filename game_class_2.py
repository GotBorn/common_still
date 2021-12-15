import pygame
import random
import os
import random

font_name = pygame.font.match_font('arial')
def draw_text(text, size, x, y, mode = "midtop"):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect()
    if mode == "midtop":
        text_rect.midtop = (x, y)
    elif mode == "topleft":
        text_rect.topleft = (x, y)
    elif mode == "center":
        text_rect.center = (x, y)
    return text_surface, text_rect


class InputBox:
    COLOR_INACTIVE = (0, 0, 0)
    COLOR_ACTIVE = (255, 0, 0)
    def __init__(self, x, y, w, h, text='', font_name = pygame.font.match_font('arial')):
        self.FONT = pygame.font.Font(font_name, 15)
        self.rect = pygame.Rect(x, y, w, h)
        self.color = self.COLOR_INACTIVE
        self.w = w
        self.h = h
        self.text = text
        self.txt_surface = self.FONT.render(text, True, self.color)
        self.active = False
        self.visible =True

def handle_event(self, event):
        if not self.visible:
            return
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = self.COLOR_ACTIVE if self.active else self.COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.FONT.render(self.text, True, self.color)


        def update(self):
            self.txt_surface = self.FONT.render(self.text, True, self.color)
            pass

        def draw(self, screen):
            if not self.visible:
                return
            # Blit the text.
            screen.blit(self.txt_surface, (self.rect.x+self.w // 2, self.rect.y+self.h // 3))
            # Blit the rect.
            pygame.draw.rect(screen, self.color, self.rect, 2)

class RoundIter():
    def __init__(self, cnt = 1):
        self.filePath = os.path.join(os.path.dirname(__file__), 'video')
        self.videoPath = []
        random.seed()
        for i in range(cnt):
            numRound =  random.randint(1, 3)
            video, timeCode = os.path.join(self.filePath, "round" + str(numRound) + '.mov'), os.path.join(self.filePath, "round" + str(numRound) + '.txt')
            while (video, timeCode) in self.videoPath:
                numRound =  random.randint(1, cnt)
                video, timeCode = os.path.join(self.filePath, "round" + str(numRound) + '.mov'), os.path.join(self.filePath, "round" + str(numRound) + '.txt')
            self.videoPath.append((video, timeCode))
        self._start = 0
        self._end = cnt  -1

    def __iter__(self):
        return self
