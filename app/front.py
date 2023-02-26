import dearpygui.dearpygui as dpg






class Front(object):


    def render(self):
        dpg.create_context()
        dpg.create_viewport(title='Modelisation Population Physalia interactif', width=600, height=600)
        dpg.setup_dearpygui()


        with dpg.window(label="Primary Window"):
            with dpg.table(header_row=False):

                # use add_table_column to add columns to the table,
                # table columns use child slot 0
                dpg.add_table_column()
                dpg.add_table_column()

        # add_table_next_column will jump to the next row
        # once it reaches the end of the columns
        # table next column use slot 1
                for i in range(0, 2):
                    with dpg.table_row():
                        for j in range(0, 1):
                            dpg.add_text(f"Row{i} Column{j}")

        
        #dpg.set_primary_window("Primary Window", True)
            


        return dpg

