init -1500 python:
    class DraggedItem(Tooltip, renpy.Displayable):
        """A Tooltip whose x/y position follows the mouse's."""
        action = Action

        def __init__(self, item, padding={"x": -32, "y": -32}, *args, **kwargs):
            super(renpy.Displayable, self).__init__(*args, **kwargs)
            
            if item is None:
                self.image = Null()
            else:
                self.image = Image(item.image % "idle")
            
            self.padding = padding or {}
            self.pad_x = self.padding.get('x', 0)
            self.pad_y = self.padding.get('y', 0)

            self.x = -100
            self.y = -100

            self._redraw = item is not None

        @property
        def redraw(self):
            return self._redraw

        @redraw.setter
        def redraw(self, new_value):
            self._redraw = new_value
            renpy.redraw(self, 0)

        def render(self, width, height, st, at):
            child_render = renpy.render(self.image, width, height, st, at)
            w, h = child_render.get_size()

            render = renpy.Render(w, h)
            render.place(self.image, x=self.x + self.pad_x, y=self.y + self.pad_y)
            return render

        def event(self, ev, x, y, st):
            self.x = x
            self.y = y

            if self.redraw:
                renpy.redraw(self, 0)

            # Pass the event to our child
            return self.image.event(ev, x, y, st)
