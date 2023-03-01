import dearpygui.dearpygui as dpg
from numpy import max
from model import compute






class Front(object):
    def __init__(self):
        self.values = {}
        self.values["a"]      = 0
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
        with dpg.plot(label="", height=400, width=400):
            temp = []
            for i in range(self.values["years"]):
                temp.append(i)
            # optionally create legend
            dpg.add_plot_legend()

            # REQUIRED: create x and y axes
            dpg.add_plot_axis(dpg.mvXAxis, label="years", tag="x_axis")
            dpg.add_plot_axis(dpg.mvYAxis, label="population", tag="y_axis")

            # series belong to a y axis
            dpg.add_line_series(temp, self.values["results"], label="population by years", parent="y_axis",tag="series")

    def update_plot(self):
        temp = [0]
        for i in range(self.values["years"]):
            temp.append(i+1)

        print(str(self.values))
        print("results : " +str(self.values["results"]))
        dpg.set_value('series', [temp, self.values["results"]])
        dpg.set_axis_limits(axis = "y_axis",ymax=max(self.values["results"])+10, ymin=0)
        dpg.set_axis_limits(axis = "x_axis", ymax=self.values["years"], ymin = 0)

    def render(self):
        dpg.create_context()
        def print_value(sender):
            a = dpg.get_value(sender)
            label = dpg.get_item_label(sender)
            print(label + " : "+str(a))
            self.values[label] = a

            self.values["results"] = compute(PO =   self.values["PO"],
                                             a=     self.values["a"],
                                             b=     self.values["b"],
                                             d=     self.values["d"],
                                             Sp=    self.values["Sp"],
                                             Q=     self.values["Q"],
                                             Sm=    self.values["Sm"],
                                             f=     self.values["f"],
                                             α=     self.values["α"],
                                             years= self.values["years"]
                                             )
            self.update_plot()

        dpg.create_viewport(title='Modelisation Population Physalia interactif', width=600, height=600)
        dpg.setup_dearpygui()


        with dpg.window(tag="Primary Window"):          
            with dpg.table(header_row=False):
             dpg.add_table_column()
             with dpg.table_row():
                with dpg.window(tag="Sliders"):
                    dpg.add_text(f"Function should be \ndisplayed here")
                    dpg.add_slider_float(label="a",default_value=0,callback=print_value, max_value=1)
                    dpg.add_slider_float(label="b",default_value=0,callback=print_value, max_value=1)
                    dpg.add_slider_float(label="Sp",default_value=0,callback=print_value, max_value=1)
                    dpg.add_slider_float(label="d",default_value=0,callback=print_value, max_value=1)
                    dpg.add_slider_float(label="Sm",default_value=0,callback=print_value, max_value=1)
                    dpg.add_slider_float(label="f",default_value=0,callback=print_value, max_value=1)
                    dpg.add_slider_float(label="α",default_value=0,callback=print_value, max_value=1)
                    dpg.add_input_int(label="Q",callback=print_value)
                    dpg.add_input_int(label="PO",callback=print_value)
                    dpg.add_input_int(label="years",callback=print_value)
                self.plot()

               


        
        dpg.set_primary_window("Primary Window", True)
            


        return dpg

