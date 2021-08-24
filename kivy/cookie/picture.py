import math

from kivy.graphics import Line, InstructionGroup
from kivy.graphics.context_instructions import Color
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.scatter import Scatter


class Picture(Scatter):
    source = StringProperty()
    draw_mode = StringProperty() #zmienna typu STRINGPROPERTY która przechowuje wartość nazwy tego przycisku (line, circle...)
    last_drawing = ObjectProperty()

    def on_touch_down(self, touch):
        if touch.button == "scrolldown":
            self.scale *= 1.25
        elif touch.button == "scrollup":
            self.scale *= 0.8
        elif not self.draw_mode:
            super(Picture, self).on_touch_down(touch)

        self.scale_touch(touch)
        touch.ud['group'] = InstructionGroup()
        with self.canvas:
            Color(1, 1, 0)
            touch.ud['group'].add(Color(1,1,0))
            touch.ud['line'] = Line(points=(touch.x, touch.y))
            touch.ud['line'].points += [touch.x, touch.y]
            if self.draw_mode == "freeform":
                touch.ud['line'].close = True

    def on_touch_up(self, touch):
        if not self.draw_mode or touch.button == "scrolldown" or touch.button == "scrolup":
            return super(Picture, self).on_touch_up(touch)

        self.scale_touch(touch)

        if self.canvas.indexof(touch.ud['line']) != -1:
            self.canvas.remove(touch.ud['line'])

        if self.draw_mode == "circle":
            self.circle(touch)
        elif self.draw_mode == "rectangle":
            self.rectangle(touch)

        if self.canvas.indexof(touch.ud['group']) != -1:
            self.canvas.remove(touch.ud['group'])
        else:
            touch.ud['group'].add(touch.ud['line'])
            self.canvas.add(touch.ud['group'])

        self.last_drawing = touch.ud['group']

    def on_touch_move(self, touch):
        self.scale_touch(touch)
        if not self.draw_mode:
            return super(Picture, self).on_touch_move(touch)
        if self.draw_mode != "freeform":
            del touch.ud['line'].points[-2:]
        touch.ud['line'].points += [touch.x, touch.y]

    def scale_touch(self, touch):
        touch.x /= self.scale
        touch.y /= self.scale

    def circle(self, touch): # przekazujemy touch ponieważ tam jest zdefinoowana informacjia o zmiennych lini
        point = touch.ud['line'].points
        touch.ud['line'] = Line(circle=(
            (point[0] + point[2])/2,(point[1] + point[3])/2, math.dist([point[0], point[1]],[point[2], point[3]])/2))

    def rectangle(self, touch):
        point = touch.ud['line'].points
        touch.ud['line'] = Line(rectangle=(
            min(point[0], point[2]), min(point[1], point[3]),
            max(point[0], point[2])- min(point[0], point[2]),
            max(point[1], point[3]) - min(point[1], point[3])))

'''       with self.canvas:
            Color(1, 1, 0)
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_up(self, touch):
        pass

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y] rysuje linie z punktów tak jak się np. pisze maluje !!!
'''