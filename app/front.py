import dearpygui.dearpygui as dpg






class Front(object):


    def render(self):
        dpg.create_context()
        dpg.create_viewport()
        dpg.setup_dearpygui()

        with dpg.window(label="Example Window"):
            dpg.add_text("Hello world")
            dpg.add_button(label="Save")
            dpg.add_input_text(label="string")
            dpg.add_slider_float(label="float")

        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()



temp = Front()
temp.render()