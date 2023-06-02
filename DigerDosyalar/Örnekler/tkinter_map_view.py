import tkinter
from tkintermapview import TkinterMapView
root_tk = tkinter.Tk()
root_tk.title("map_view_simple_example.py")
root_tk.geometry(f"{600}x{400}")
widgetmap_widget = TkinterMapView(root_tk, width=600, height=400, corner_radius=0)
widgetmap_widget.pack(fill="both", expand=True)
widgetmap_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
# widgetmap_widget.set_address("Kiz kulesi", marker=True)
widgetmap_widget.set_position(39.744957, 39.482981, marker=True)
root_tk.mainloop()