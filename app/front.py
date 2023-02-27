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
        self.values["f"]      = 0
        self.values["α"]      = 0
        self.values["PO"]     = 0
        self.values["years"]  = 1
        self.values["results"] = [0]

    def plot(self):
        with dpg.plot(label="Plot", height=400, width=400):
            temp = []
            for i in range(self.values["years"]):
                temp.append(i)
            # optionally create legend
            dpg.add_plot_legend()

            # REQUIRED: create x and y axes
            dpg.add_plot_axis(dpg.mvXAxis, label="years")
            dpg.add_plot_axis(dpg.mvYAxis, label="population", tag="y_axis")

            # series belong to a y axis
            dpg.add_line_series(temp, self.values["results"], label="population by years", parent="y_axis",tag="series")

    def update_plot(self):
        temp = []
        for i in range(self.values["years"]):
            temp.append(i)

        print("temp : "+temp)
        print("results : " +self.values["results"])
        dpg.set_value('series', [temp, self.values["results"]])

    def render(self):
        dpg.create_context()
        def print_value(sender):
            a = dpg.get_value(sender)
            label = dpg.get_item_label(sender)
            print(label + " : "+str(a))
            self.values["label"] = a

            self.values["results"] = compute(PO =   self.values["PO"],
                                             a=     self.values["a"],
                                             b=     self.values["b"],
                                             d=     self.values["d"],
                                             Sp=    self.values["Sp"],
                                             Q=     self.values["Q"],
                                             Sm=    self.values["Sm"],
                                             f=     self.values["f"],
                                             α=     self.values["α"],
                                             )
            print(self.values["results"])
            self.update_plot()

        dpg.create_viewport(title='Modelisation Population Physalia interactif', width=600, height=600)
        dpg.setup_dearpygui()


        with dpg.window(tag="Primary Window"):
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
                    dpg.add_slider_float(label="f",default_value=0,callback=print_value, max_value=1)
                
                with dpg.table_row():
                    dpg.add_slider_float(label="α",default_value=0,callback=print_value, max_value=1)

                with dpg.table_row():
                    dpg.add_input_int(label="Q",callback=print_value)

                with dpg.table_row():
                    dpg.add_input_int(label="PO",callback=print_value)
                
                with dpg.table_row():
                    dpg.add_input_int(label="years",callback=print_value)


                dpg.add_table_column()

                with dpg.table_row():
                    self.plot()


        
        dpg.set_primary_window("Primary Window", True)
            


        return dpg

