from time import time
from typing import Callable, List, Sequence, Union, overload

import pygame

pygame.font.init()

if __name__ == "__main__":
    print("This is a module and should not be run directly")
    quit()


def center(ow: int, oh: int, iw: int, ih: int) -> List[int]:
    return [ow // 2 - iw // 2, oh // 2 - ih // 2]


def lerp(a, b, t): return a * (1 - t) + b * t


def lighter(color: pygame.Color, amount: float) -> pygame.Color:
    r, g, b = color.r, color.g, color.b
    return pygame.Color(int(lerp(r, 255, amount)), int(lerp(g, 255, amount)), int(lerp(b, 255, amount)))


def darker(color: pygame.Color, amount: float) -> pygame.Color:
    r, g, b = color.r, color.g, color.b
    return pygame.Color(int(lerp(0, r, amount)), int(lerp(0, g, amount)), int(lerp(0, b, amount)))


def get_color(color: Union[pygame.Color, int, str], default: int) -> pygame.Color:
    if isinstance(color, (list, tuple)) and len(color) in (3, 4):
        return pygame.Color(*color)
    elif isinstance(color, int):
        try:
            return pygame.Color(color << 8 | 255)
        except ValueError:
            return pygame.Color(color)
    elif isinstance(color, str):
        try:
            return pygame.Color(color)
        except ValueError or UnicodeEncodeError:
            return pygame.Color(default)
    elif isinstance(color, pygame.Color):
        return color
    else:
        return pygame.Color(default)


def get_font(font: Union[pygame.font.Font, str]):
    if isinstance(font, pygame.font.Font):
        return font
    elif isinstance(font, str) and "_" in font and font.count("_") == 1:
        name, rest = font.split("_")
        size = "".join((i for i in rest if i.isdecimal()))
        bold = "b" in rest
        italic = "i" in rest
        return pygame.font.SysFont(name, int(size), bold, italic)
    elif isinstance(font, (tuple, list)) and isinstance(font[0], str) and isinstance(font[1], int) and font[1]:
        if len(font) == 2:
            return pygame.font.SysFont(font[0], abs(font[1]))
        elif len(font) == 3 and isinstance(font[2], (str, list, tuple)):
            bold = "b" in font[2]
            italic = "i" in font[2]
            return pygame.font.SysFont(font[0], abs(font[1], bold, italic))

def draw_widgets(surface: pygame.Surface):
    Widget.group.draw(surface)


class Widget(pygame.sprite.Sprite):
    group = pygame.sprite.Group()

    def __init__(self, rect: pygame.Rect, text: str):
        pygame.sprite.Sprite.__init__(self)
        if isinstance(rect, pygame.Rect):
            self.rect = rect
        else:
            self.rect = pygame.Rect(rect)
        self.text = text
        self.image = pygame.Surface(self.rect.size)
        Widget.group.add(self)

    def config(self, **kwargs):
        if kwargs:
            for k, v in kwargs.items():
                if k == "color":
                    setattr(self, k, get_color(v, 0xf0f0f0))
                elif k == "textcolor":
                    setattr(self, k, get_color(v, 0x000000))
                elif k == "font":
                    setattr(self, k, get_font(v))
                elif k == "rect":
                    if isinstance(v, pygame.Rect):
                        setattr(self, k, v)
                    else:
                        setattr(self, k, pygame.Rect(v))
                else:
                    setattr(self, k, v)
            self.render()
            return self
        else:
            return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}


class Button(Widget):
    group = pygame.sprite.Group()

    def __init__(self, rect: pygame.Rect, text: str = "", color: pygame.Color = 0xf0f0f0,
                 command: Callable[[], None] = None, active: bool = True,
                 textcolor: pygame.Color = 0x000000, font: pygame.font.Font = None):
        super().__init__(rect, text)
        Button.group.add(self)
        Widget.group.add(self)
        self.command = command
        self.color = get_color(color, 0xf0f0f0)
        self.textcolor = get_color(textcolor, 0x000000)
        self.active = active
        self.pressed = False
        self.font = get_font(font)
        self.render()

    @overload
    def config(self, rect: pygame.Rect, text: str, color: pygame.Color, command: Callable[[], None],
               active: bool, textcolor: pygame.Color, font: pygame.font.Font) -> Union[dict, None]:
        ...

    def config(self, **kwargs):
        return super().config(**kwargs)

    def render(self):
        if not self.font:
            self.font = pygame.font.Font(None, self.rect.height)
        w, h = self.rect.width, self.rect.height
        s = self.font.size(self.text)
        if self.pressed:
            self.image.fill(lighter(self.color, .6))
            pygame.draw.rect(self.image, darker(
                self.color, .7), (0, 0, w - 1, h - 1))
            pygame.draw.rect(self.image, darker(
                self.color, .9), (1, 1, w - 2, h - 2))
            pygame.draw.rect(self.image, darker(
                self.color, .6), (1, 1, w - 3, h - 3))
            pygame.draw.rect(self.image, self.color, (2, 2, w - 4, h - 4))
            self.image.blit(self.font.render(self.text, True,
                            self.textcolor), ((c := center(*self.rect.size, *s))[0] + 1, c[1] + 1))
        else:
            self.image.fill(darker(self.color, .6))
            pygame.draw.rect(self.image, lighter(
                self.color, .6), (0, 0, w - 1, h - 1))
            pygame.draw.rect(self.image, darker(
                self.color, .7), (1, 1, w - 2, h - 2))
            pygame.draw.rect(self.image, darker(
                self.color, .9), (1, 1, w - 3, h - 3))
            pygame.draw.rect(self.image, self.color, (2, 2, w - 4, h - 4))
            color = self.textcolor if self.active else 0x6d6d6dff
            self.image.blit(self.font.render(
                self.text, True, color), center(*self.rect.size, *s))

    def update(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.active and pygame.Rect.collidepoint(self.rect, event.pos):
                self.pressed = True
                self.render()
                if self.command:
                    self.command()
        elif event.type == pygame.MOUSEBUTTONUP and self.pressed:
            self.pressed = False
            self.render()
    
    def __repr__(self):
        return f"Button: {self.text}"


class DropdownMenu(Widget):
    group = pygame.sprite.Group()

    def __init__(self, rect: pygame.Rect, text: str = "", color: pygame.Color = 0xf0f0f0,
                 textcolor: pygame.Color = 0x000000, expansion: int = 200,
                 options: Sequence[str] = None, font: pygame.font.Font = None):
        super().__init__(rect, text)
        DropdownMenu.group.add(self)
        Widget.group.add(self)
        self.color = get_color(color, 0xf0f0f0)
        self.textcolor = get_color(textcolor, 0x000000)
        self.expansion = expansion
        self.options = [] if options is None else list(options)
        self.font = get_font(font)
        self.selected = -1  # Index of selected Element, -1 if None
        self.opened = False
        self.render()

    @overload
    def config(self, rect: pygame.Rect, text: str, color: pygame.Color,
               textcolor: pygame.Color, expansion: int,
               options: Sequence[str], font: pygame.font.Font) -> Union[dict, None]: ...

    def config(self, **kwargs):
        return super().config(**kwargs)

    def render(self):
        if not self.font:
            self.font = pygame.font.Font(None, self.rect.height)
        w, h = self.rect.width, self.rect.height
        if self.opened:
            self.image = pygame.Surface(
                (w, min(h + self.expansion, h * (len(self.options) + 1))))
        else:
            self.image = pygame.Surface(self.rect.size)
        s = self.font.size(self.text)
        self.image.fill(lighter(self.color, .6))
        pygame.draw.rect(self.image, darker(
            self.color, .7), (0, 0, w - 1, h - 1))
        pygame.draw.rect(self.image, darker(
            self.color, .9), (1, 1, w - 2, h - 2))
        pygame.draw.rect(self.image, darker(
            self.color, .6), (1, 1, w - 3, h - 3))
        pygame.draw.rect(self.image, self.color, (2, 2, w - 4, h - 4))
        self.image.blit(self.font.render(self.text, True,
                        self.textcolor), center(*self.rect.size, *s))
        if self.opened:
            pygame.draw.polygon(self.image, self.textcolor, [
                (w - h // 1.15, h // 1.6),
                (w - h // 2.7 + 1, h // 1.6),
                (w - (h // 2.3 + h // 5.2), h // 2.7),
                (w - (h // 2.3 + h // 5.2 + 1), h // 2.7 + 1),
            ])
            for i, x in enumerate(self.options):
                pygame.draw.rect(self.image, self.color,
                                 (0, h * (i + 1), w, h))

        else:
            pygame.draw.polygon(self.image, self.textcolor, [
                (w - h // 1.15, h // 2.7),
                (w - h // 2.7, h // 2.7),
                (w - (h // 2.3 + h // 5.2), h // 1.6)])

    def update(self, event: pygame.event.Event):
        if pygame.Rect.collidepoint(self.rect, event.pos):
            pass
        elif self.opened:
            self.opened = False
            self.render()


class EntryGroup(pygame.sprite.Group):
    def __init__(self, *sprites):
        super().__init__(self, *sprites)
        self.focus_entry = None

    def focused(self):
        return bool(self.focus_entry)



class Entry(Widget):
    group = EntryGroup()

    def __init__(self, rect: pygame.Rect, prompt: str = "",
                 color: pygame.Color = 0xffffff, textcolor: pygame.Color = 0x000000,
                 active: bool = True, font: pygame.font.Font = None):
        Entry.group.add(self)
        Widget.group.add(self)
        super().__init__(rect, "")
        self.prompt = prompt
        self.color = get_color(color, 0xffffff)
        self.textcolor = get_color(textcolor, 0x000000)
        self.active = active
        self.focused = False
        self.font = font
        self.render()

    @overload
    def config(selfrect: pygame.Rect, prompt: str, allow_empty: bool,
               color: pygame.Color, textcolor: pygame.Color,
               active: bool, font: pygame.font.Font = None) -> Union[dict, None]:
        ...

    def config(self, **kwargs):
        return super().config(**kwargs)

    def render(self):
        if not self.font:
            self.font = pygame.font.Font(None, self.rect.height)
        width = self.font.size(self.text)[0]
        x = min(self.rect.width - x - 10, 0)
        

    def draw(self, surface_dest: pygame.Surface):
        super().draw(surface_dest)

    def get(self): return self.text
    __str__ = get

    def focus(self):
        for i in self.groups():
            if isinstance(i, EntryGroup):
                i.focus_entry = self

    def update(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                # delete last character
                self.focus_entry.text = self.focus_entry.text[:-1]
                self.focus_entry.render(True)
            elif event.key == pygame.K_ESCAPE:
                # unfocus entries
                self.focus_entry.focused = False
                self.focus_entry.render(False)
                self.focus_entry = None
            else:
                # add typed character to focused entry
                self.focus_entry.text += event.unicode
                self.focus_entry.render(False)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in self.sprites():
                if pygame.Rect.collidepoint(i.rect, event.pos):
                    self.focus_entry = i
                    i.focused = True
                    i.timerstart = time()
                    break
                elif i.focused:
                    i.focused = False
    
    def __repr__(self):
        return f"Entry: {self.get}"

class Menu:
    def __init__(self, *widgets):
        self.entry_group = EntryGroup()
        self.widget_group = pygame.sprite.Group()
        self.add(*widgets)
    
    def add(self, *widgets):
        for i in widgets:
            if isinstance(i, Entry):
                self.entry_group.add(i)
            elif isinstance(i, Widget):
                self.widget_group.add(i)
    
    def update(self, event):
        self.widget_group.update(event)
        self.entry_group.update(event)
    
    def draw(self, surface):
        self.widget_group.draw(surface)
        self.entry_group.draw(surface)

    def entry_focused(self):
        return bool(self.entry_group.focus_entry)