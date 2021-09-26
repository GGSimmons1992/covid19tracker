import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
plt.style.use('ggplot')

import plotly
from urllib.request import urlopen
import json
import plotly.express as px
import plotly.graph_objects as go

def makeChoropleth(df,valueColumn,title,colorRange = [0,0]):
    nonNanDF = df[df[valueColumn] != np.nan]
    
    if colorRange[1] == 0:
        colorRange[1] = max(nonNanDF[valueColumn])

    fig = px.choropleth(
        nonNanDF,
        locations = 'Country/Territory',
        locationmode = 'country names',
        color = valueColumn,
        range_color = colorRange,
        color_continuous_scale='RdYlGn'
    )
    
    fig.layout.coloraxis.colorbar.title = ""

    fig.update_layout(title_text=title)
    imgTitle = title.replace(" ","")
    fig.write_image(f'../images/{imgTitle}.png')
    return fig