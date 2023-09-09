__version__ = "0.0.0"

import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title=f'MedConsultant v{__version__}', width=800, height=600)

with dpg.window(
    label="Example Window",
    min_size=(800, 600),
    no_collapse=True, no_close=True, no_move=True
):
    # with dpg.window(height=500, width=600, no_scrollbar=True):
    with dpg.table(header_row=False, resizable=True):
        dpg.add_table_column(width_fixed=True, init_width_or_weight=200)
        dpg.add_table_column()
        with dpg.table_row():
            with dpg.child_window(autosize_y=True):
                with dpg.tree_node(label="Heart deseases"):
                    dpg.add_checkbox(label="Heart attack 1")
                    dpg.add_checkbox(label="Heart attack 2")

                with dpg.tree_node(label="Oporno dvigatel deseases"):
                    for i in range(100):
                        dpg.add_checkbox(label=f"Heart attack {i}")

                dpg.add_button(label="Result", callback=lambda: print("ok"))

            with dpg.group():
                with dpg.child_window(autosize_y=True):
                    with dpg.table(label="Excercises"):
                        dpg.add_table_column(label="Name")
                        dpg.add_table_column(label="Description")
                        with dpg.table_row():
                            dpg.add_text("Bob")
                            dpg.add_text("He is a man")


if __name__ == "__main__":
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
