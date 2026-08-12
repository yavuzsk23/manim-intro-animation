from manim import *
from loguru import logger


class FirstAnimation(Scene):
    """A simple introductory Manim scene: a circle is drawn, filled, and labeled."""

    def construct(self):
        logger.info("Preparing the scene...")

        # Create a circle with a cyan outline and a semi-transparent blue fill
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_color(CYAN)

        # Add a label below the circle
        label = Text("Space Station", font_size=40).next_to(circle, DOWN)

        # Animate: draw the circle, then write the label
        logger.info("Rendering circle...")
        self.play(Create(circle))

        logger.info("Rendering label...")
        self.play(Write(label))

        # Briefly transform the circle's color to show a second animation
        logger.info("Rendering color transition...")
        self.play(circle.animate.set_color(YELLOW))

        self.wait(2)
        logger.success("Scene finished rendering.")
