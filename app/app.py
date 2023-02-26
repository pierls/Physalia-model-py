from front import Front



def __init__():
    print("hello world")
    app = Front().render()

    app.show_viewport()
    app.start_dearpygui()
    app.destroy_context()


__init__()