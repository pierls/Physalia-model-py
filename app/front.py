import dearpygui.dearpygui as dpg
from model import compute






class Front(object):
    def __init__(self):
        self.values = {}
        self.values["a"]     = 0
        self.values["b"]      = 0
        self.values["Sp"]     = 0
        self.values["d"]      = 0
        self.values["Q"]      = 0
        self.values["Sm"]     = 0
        self.values["F"]      = 0
        self.values["α"]      = 0
        self.values["PO"]     = 0

    def render(self):
        dpg.create_context()
        def print_value(sender):
            a = dpg.get_value(sender)
            label = dpg.get_item_label(sender)
            print(label + " : "+str(a))
            self.values["label"] = a

        dpg.create_viewport(title='Modelisation Population Physalia interactif', width=600, height=600)
        dpg.setup_dearpygui()


        with dpg.window(label="Primary Window"):
            with dpg.table(header_row=False):

                # use add_table_column to add columns to the table,
                # table columns use child slot 0
                dpg.add_table_column()
                

                with dpg.table_row():
                    #function display here
                    dpg.add_text(f"Function should be \ndisplayed here")
                
                with dpg.table_row():
                    dpg.add_slider_float(label="a",default_value=0,callback=print_value, max_value=1)

                with dpg.table_row():
                    dpg.add_slider_float(label="b",default_value=0,callback=print_value, max_value=1)

                with dpg.table_row():
                    dpg.add_slider_float(label="Sp",default_value=0,callback=print_value, max_value=1)
                
                with dpg.table_row():
                    dpg.add_slider_float(label="d",default_value=0,callback=print_value, max_value=1)
                
                with dpg.table_row():
                    dpg.add_slider_float(label="Sm",default_value=0,callback=print_value, max_value=1)
                
                with dpg.table_row():
                    dpg.add_slider_float(label="F",default_value=0,callback=print_value, max_value=1)
                
                with dpg.table_row():
                    dpg.add_slider_float(label="α",default_value=0,callback=print_value, max_value=1)
                
                


                column_2 = dpg.add_table_column()

        
        #dpg.set_primary_window("Primary Window", True)
            


        return dpg

