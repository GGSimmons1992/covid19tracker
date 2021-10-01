# covid19tracker

Covid vaccination rates in the U.S. and other industrialized nations tend to be faster than those in third world countries. This project uses a the global covid 19 vaccination tracker data set to answer if population, GDP, and various vaccination numbers (e.g. daily dose rate, vaccines allotted for % of the population, and % of population fully vaccinated) affect each other. The target audience is individuals organizations interested in the progress of vaccination of the world, like the World Health Organization. My main tools are Pandas for data manipulation, scipy.stats for correlation and hypothesis testing calculations, pyplot.matplotlib for figures, and plotly for choropleth maps. For the hypothesis testing I'm mainly going to calculate p using pearson correlations for normalized data and spearman correlations for non-normalized data. First I will present choropleth maps to give a visual of the world data in question. Then I will present bar charts of the top 5 and bottom 5 countries according to vaccination percentage. Finally, I will present the correlation plots near the end with the p-values to then accept or reject my null hypotheses.

## data (not included. Using .gitignore)

Due to data size and standard practice, my datasets are not included in this repo. However, the datasets are easily procurable. GDP and vaccination data are downloadable from the Kaggle dataset, [Global Covid 19 Vaccination Tracker](https://www.kaggle.com/kamal007/global-covid19-vaccination-tracker). Population dataset comes from [The World Bank](https://data.worldbank.org/indicator/SP.POP.TOTL). The specific .csv file from the World Bank used is API_SP.POP.TOTL_DS2_en_csv_v2_2918012.csv. The last 7 digits in the name of the csv file is a timestamp, so that number may change when you download it.

## images

Images are divided into subfolders: barCharts, choropleths, correlations, and normalCheck. The bar charts in barCharts show the top 5 and bottom 5 countries in each of the 5 targetted columns used in this study. The choropleths in choropleths show a choropleth map for the 5 target columns used in this study. Correlation plots in correlations show the Spearman correlations between selected columns. Lastly, the plots in normalCheck are used to determine if the data is normally distributed. Since, the data is not normally distributed, we can justify using Spearman correlation, since using Pearson correlation is not advisable for non-normally distributed data.

## notebooks

dataProcessor.ipynb is my pipeline used to generate all figures. First, ensure all data mentioned in the data section above is in a data folder (which should be at the same level of the other folders). Second, make sure the names and paths of .csv file in the Data Manipulation section match up with the .csv files in the data folder (See last sentence in data section of this readme). Once the data is in the data folder and the paths in the read_csv commands are verified to match the data in the data folder, one can run the whole notebook, to populate the images folders with the correct images.

## src

utils.py is a custom python module that notebooks/dataProcess.ipynb uses.

## License

This work uses a MIT License, granting people to use or reuse this project for their own purposes.