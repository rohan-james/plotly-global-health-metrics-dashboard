from app_instance import app
import dash_mantine_components as dmc

from index import layout

import callbacks.header_callbacks
import callbacks.gender_callbacks
import callbacks.globe_callbacks
import callbacks.heatmap_callbacks
import callbacks.bubble_chart_callbacks
import callbacks.chart_toggle_callback
import callbacks.sankey_diagram_callback
import callbacks.histplot_callback
import callbacks.hero_section_callbacks

app.layout = dmc.MantineProvider(children=[layout])

server = app.server

if __name__ == "__main__":
    try:
        app.run(
            debug=True,
            port=8000,
            dev_tools_ui=False,
            dev_tools_props_check=False,
            dev_tools_hot_reload=False,
        )
    except Exception as e:
        print(e)
