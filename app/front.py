

import dearpygui.dearpygui as dpg
from numpy import max
from model import compute

"""
This module can be assmilated as the core of this application. Not only it does the
front-UI aspect, but it also use the model from model.py.
"""




# Création dictionnaire de valeurs 
class Front(object):
    """
    Front
    =====
    Description
    -----------
    Front is an object that does not get any parameters , and had a single configuration possible.
    It is the one that return a dearpygui object fully setup. But be careful, it does not show any windows.
    This need to be done after that.
    The right way to manipulate it is:
        - To create it in a fist place.
        - To call its ``render()`` function.
    
    After that, it can be displayed by using its .show_viewport() internal function.

    Requirements
    ------------
    This class rely on three libraries to run:
        - numpy (can be downloaded via ``pip install numpy``.)
        - dearpygui (can be downloaded via ``pip install dearpygui``.)
        - model (internal class of this application.)
    """ 
    # Création du dictionnaire de valeur, clés valeurs sous forme de tableau pour 
    def __init__(self):                     
        self.values = {}
        self.values["Taux de rencontre méduse / prédateur"]             = 0.5
        self.values["Taux de formation des supra-organismes"]           = 0.02
        self.values["Taux de survie polype"]                            = 0.7
        self.values["Taux de scissiparité par polype"]                  = 0.4
        self.values["Quantité de prédateur initial"]                    = 5
        self.values["Taux de survie par méduse"]                        = 0.55
        self.values["Taux de fécondation par méduse"]                   = 0.6
        self.values["Taux d'impact compétition intra-spécifique"]       = 0.01
        self.values["Quantité de polype initial"]                       = 10
        self.values["Période prévisionelle (années)"]                   = 40
        self.values["results"]                                          = [0]

# Création du plot la boucle d'itération permet d'ajouter +1 aux abscisse pour chaque itération de modèle 
    def plot(self):
        """Function that act like a factory for the plot object of the UI.
        """
        with dpg.plot(label="", height=400, width=400):
            valeurs = []
            for i in range(self.values["Période prévisionelle (années)"]):
                valeurs.append(i)
            # optionally create legend
            dpg.add_plot_legend()

            # REQUIRED: create x and y axes
            dpg.add_plot_axis(dpg.mvXAxis, label="Période prévisionelle (années)", tag="x_axis")
            dpg.add_plot_axis(dpg.mvYAxis, label="population", tag="y_axis")

            # series belong to a y axis
            dpg.add_line_series(valeurs, self.values["results"], label="Estimation de la population", parent="y_axis",tag="series")

# Actualisation axe y et x respectivement en fonction du nombre d'individus calculés et de la période prévisionelle grâce a Numpy (trouve la valeur max d'un tableau de valeur)
    def update_plot(self):
        """This function updates the previously created plot comùponent of the UI, based on
        the new parameters that the user have chosen. It calls the model's ``compute()`` function in order to display proper data.
        """
        annees = [0]
        for i in range(self.values["Période prévisionelle (années)"]):
            annees.append(i+1)

        print(str(self.values))
        print("results : " +str(self.values["results"]))
        dpg.set_value('series', [annees, self.values["results"]])
        dpg.set_axis_limits(axis = "y_axis",ymax=max(self.values["results"])+10, ymin=0)
        dpg.set_axis_limits(axis = "x_axis", ymax=self.values["Période prévisionelle (années)"], ymin = 0)

    def render(self):
        """Contrary to what its name might suggest, the ``render()`` function does not display anything, it only creates a viewport (in the DearPygui's way).
        It is left to the user of this class to render this object afterward.
        """
        dpg.create_context()
        dpg.create_viewport(title='Modelisation Population Physalia interactif', width=600, height=600)
        dpg.setup_dearpygui()

# Création du lien dictionnaire de valeur / front
        def print_value(sender): #bouton touché --> a, a = self.values(label) --> dit au dictionnaire qu'une valeur a bougé
            """"This function  oraiginally print a dump of all values for debugging, but it becomes an update on the values dict by recognizing the last button/slider updated by the user.
            """
            a = dpg.get_value(sender)
            label = dpg.get_item_label(sender)
            print(label + " : "+str(a)) # affichage des valeurs dans le terminal pour debuguer
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
                                             years= self.values["Période prévisionelle (années)"]
                                             )
            self.update_plot()


# Création de l'interface sliders/input

        with dpg.window(tag="Primary Window"):          
            with dpg.table(header_row=False):
             dpg.add_table_column()
             with dpg.table_row():
                with dpg.table_cell(tag="Sliders"):
                    dpg.add_text("Modèle sous forme d'équation différentiel non linéaire")
                    dpg.add_slider_float(label="Taux de rencontre méduse / prédateur",default_value=self.values["Taux de rencontre méduse / prédateur"],callback=print_value, max_value=1)
                    dpg.add_slider_float(label="Taux de formation des supra-organismes",default_value=self.values["Taux de formation des supra-organismes"],callback=print_value, max_value=1)
                    dpg.add_slider_float(label="Taux de survie polype",default_value=self.values["Taux de survie polype"],callback=print_value, max_value=1)
                    dpg.add_slider_float(label="Taux de scissiparité par polype",default_value=self.values["Taux de scissiparité par polype"],callback=print_value, max_value=1)
                    dpg.add_slider_float(label="Taux de survie par méduse",default_value=self.values["Taux de survie par méduse"],callback=print_value, max_value=1)
                    dpg.add_slider_float(label="Taux de fécondation par méduse",default_value=self.values["Taux de fécondation par méduse"],callback=print_value, max_value=1)
                    dpg.add_slider_float(label="Taux d'impact compétition intra-spécifique",default_value=self.values["Taux d'impact compétition intra-spécifique"],callback=print_value, max_value=1)
                    dpg.add_input_int(label="Quantité de prédateur initial",default_value=self.values["Quantité de prédateur initial"],callback=print_value)
                    dpg.add_input_int(label="Quantité de polype initial",default_value=self.values["Quantité de polype initial"],callback=print_value)
                    dpg.add_input_int(label="Période prévisionelle (années)",default_value=self.values["Période prévisionelle (années)"],callback=print_value)
                    self.plot()

               


        
            dpg.set_primary_window("Primary Window", True)
            


        return dpg

