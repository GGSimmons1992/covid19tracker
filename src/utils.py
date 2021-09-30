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

import seaborn as sns
from statsmodels.graphics.gofplots import qqplot

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
    fig.write_image(f'../images/choropleths/{imgTitle}.png')
    return fig

def checkNormality(df,valueColumn):
    fig,axs = plt.subplots(2,1)
    sns.histplot(df[valueColumn],kde=True,ax=axs[0])
    qqplot(df[valueColumn],line='s',ax=axs[1])
    figTitle = f'Normal Check for {valueColumn}'
    fig.suptitle(figTitle)
    plt.savefig(f'../images/normalChecks/{figTitle.replace(" ","")}.png')
    plt.show()

def spearmanCorrelate(df,xCol,yCol,title):
    nonNanDF = df[[xCol,yCol]].dropna()
    
    ax = sns.regplot(x = nonNanDF[xCol], y = nonNanDF[yCol], scatter_kws = {'s':8},fit_reg = False)
    sns.regplot(x = nonNanDF[xCol], y = nonNanDF[yCol], scatter=False, ci=95, fit_reg = True,
    color = 'orange', lowess = True)
    ax.set(xlabel = xCol, ylabel = yCol)
    rValue,pValue = stats.spearmanr(nonNanDF)
    ax.set(title = f'{title} R={rValue:.2f}, p={pValue:.5f}')
    plt.savefig(f'../images/correlations/{title.replace(" ","")}.png')
    plt.show()