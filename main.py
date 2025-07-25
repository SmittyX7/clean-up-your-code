def on_button_pressed_a():
    for index in range(4):
        images.create_big_image("""
            . . . . . . . . . .
            . . . . . . # # # .
            . . # . . . # . # .
            . . . . . . # # # .
            . . . . . . . . . .
            """).scroll_image(5, 300)
        images.create_big_image("""
            # # # # # . . . . .
            # . . . # . . . . .
            # . . . # . . . . .
            # . . . # . . . . .
            # # # # # . . . . .
            """).scroll_image(5, 300)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)
