import dearpygui.dearpygui as dpg
from numpy import max
from model import compute






class Front(object):
    def __init__(self):
        self.values = {}
        self.values["Taux de rencontre méduse / prédateur"]             = 0
        self.values["Taux de formation des supra-organismes"]           = 0
        self.values["Taux de survie polype"]                            = 0
        self.values["Taux de scissiparité par polype"]                  = 0
        self.values["Quantité de prédateur initial"]                    = 0
        self.values["Taux de survie par méduse"]                        = 0
        self.values["Taux de fécondation par méduse"]                   = 0
        self.values["Taux d'impact compétition intra-spécifique"]       = 0
        self.values["Quantité de polype initial"]                       = 0
        self.values["Période prévisionelle"]                            = 1
        self.values["results"]                                          = [0]

    def plot(self):
        with dpg.plot(label="", height=400, width=400):
            valeurs = []
            for i in range(self.values["Période prévisionelle"]):
                valeurs.append(i)
            # optionally create legend
            dpg.add_plot_legend()

            # REQUIRED: create x and y axes
            dpg.add_plot_axis(dpg.mvXAxis, label="Période prévisionelle", tag="x_axis")
            dpg.add_plot_axis(dpg.mvYAxis, label="population", tag="y_axis")

            # series belong to a y axis
            dpg.add_line_series(valeurs, self.values["results"], label="Estimation de la population", parent="y_axis",tag="series")

    def update_plot(self):
        annees = [0]
        for i in range(self.values["Période prévisionelle"]):
            annees.append(i+1)

        print(str(self.values))
        print("results : " +str(self.values["results"]))
        dpg.set_value('series', [annees, self.values["results"]])
        dpg.set_axis_limits(axis = "y_axis",ymax=max(self.values["results"])+10, ymin=0)
        dpg.set_axis_limits(axis = "x_axis", ymax=self.values["Période prévisionelle"], ymin = 0)

    def render(self):
        dpg.create_context()
        dpg.create_viewport(title='Modelisation Population Physalia interactif', width=600, height=600)
        dpg.setup_dearpygui()


        def print_value(sender):
            a = dpg.get_value(sender)
            label = dpg.get_item_label(sender)
            print(label + " : "+str(a))
            self.values[label] = a

            self.values["results"] = compute(PO =   self.values["Quantité de polype initial"],
                                             a=     self.values["Taux de rencontre méduse / prédateur"],
                                             b=     self.values["Taux de formation des supra-organismes"],
                                             d=     self.values["Taux de scissiparité par polype"],
                                             Sp=    self.values["Taux de survie polype"],
                                             Q=     self.values["Quantité de prédateur initial"],
                                             Sm=    self.values["Taux de survie par méduse"],
                                             f=     self.values["Taux de fécondation par méduse"],
                                             α=     self.values["Taux d'impact compétition intra-spécifique"],
                                             years= self.values["Période prévisionelle"]
                                             )
            self.update_plot()


        # Test

        with dpg.window(tag="Primary Window"):          
            with dpg.table(header_row=False):
             dpg.add_table_column()
             with dpg.table_row():
                with dpg.table_cell(tag="Sliders"):
                    dpg.add_text(f"Function should be \ndisplayed here")
                    dpg.add_slider_float(label="Taux de rencontre méduse / prédateur",default_value=0,callback=print_value, max_value=1)
                    dpg.add_slider_float(label="Taux de formation des supra-organismes",default_value=0,callback=print_value, max_value=1)
                    dpg.add_slider_float(label="Taux de survie polype",default_value=0,callback=print_value, max_value=1)
                    dpg.add_slider_float(label="Taux de scissiparité par polype",default_value=0,callback=print_value, max_value=1)
                    dpg.add_slider_float(label="Taux de survie par méduse",default_value=0,callback=print_value, max_value=1)
                    dpg.add_slider_float(label="Taux de fécondation par méduse",default_value=0,callback=print_value, max_value=1)
                    dpg.add_slider_float(label="Taux d'impact compétition intra-spécifique",default_value=0,callback=print_value, max_value=1)
                    dpg.add_input_int(label="Quantité de prédateur initial",callback=print_value)
                    dpg.add_input_int(label="Quantité de polype initial",callback=print_value)
                    dpg.add_input_int(label="Période prévisionelle",callback=print_value)
                    self.plot()

               


        
            dpg.set_primary_window("Primary Window", True)
            


        return dpg

