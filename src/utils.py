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

def createBarCharts(df,valueColumn,title):
    nonNanDF = df[~df[valueColumn].isnull()]
    valuesDF = nonNanDF[['Country/Territory',valueColumn]]
    valuesDF = valuesDF.sort_values(by=valueColumn).set_index('Country/Territory')
    
    top5 = valuesDF.tail(5)
    bottom5 = valuesDF.head(5)

    createBarChart(top5,valueColumn,title,'Top 5')
    createBarChart(bottom5,valueColumn,title,'Bottom 5') 

def createBarChart(df,valueColumn,title,suffix):
    ax = df.plot(kind='barh',legend=False)
    ax.set_title(f'{title} {suffix}')
    ax.set_xlabel(valueColumn)
    plt.savefig(f'../images/barCharts/{title.replace(" ","")}{suffix.replace(" ","")}')

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