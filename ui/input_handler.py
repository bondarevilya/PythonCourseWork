class InputHandler:
    def __init__(self, controller):
        self.controller = controller

    def handle_click(self, pos):
        self.controller.process_click(pos)