![Image of gitly](https://raw.githubusercontent.com/Tiagoeem/gitly/master/doc/ico.PNG)
   
# gitly: Showing plotly graphs in github

This is a home made lib to help you plot your fency graphs from plotly in github while using Google Colab notebook.

## The problem: Nbviewer from Github is static!

The problem is that all fency engines that you use on notebooks doesn't run in static viewers, of course there's a lot of ways to generate static images in this libraries. But I use Google Colab by a lot in my classes and I would like to have a easy way to switch betweern dinamic plots and statics plots (to commit and share nice plots in github). So I implement this very simple implementation.

## Easy switch between colab and git "renderers"

Just change from dinamic to static using:

```python
from gitly.colab.plot import GitlyPlotter

# Instantiate the object using 'github' or 'git' for static plots
# or 'colab' for default dinamic Plotly plots
gitly = GitlyPlotter('github')
```

Now just pass the figure from plotly to ```gitly.show( fig ) ``` and it's done!!!

```python
import plotly.express as px

fig = px.scatter_3d( df, title="Random data")
gitly.show( fig )
```
Now you can commit all your fency plots in github! Congratz!

## Can I use both in the same Colab notebook? Sure you can!

Just use ```gitly.config_render('colab') ``` to switch back in the cell and renderer with default plot from Plotly.

## Check the example here!

You can check that some plots you can see (used "github" view) and others that is used the standard Plotly Engine you only can see if you run this notebook in Google colab.

[Simple Example](https://github.com/Tiagoeem/gitly/blob/master/examples/Using_Gitly_Example.ipynb)

# Instalation

This lib is intended to be used only on Google Colab notebooks.

Open a cell and run the following code:

```!pip install -i https://test.pypi.org/simple/ gitly ```

# Features

This features are only for static plots.
## Change the defaults
You are able to set a default values for **hight**, **width** and **scale** for all your plots.

```python
gitly.config_render('git', default_height = 600, default_width = 1000) # set default values for all gitly.show()

fig = px.scatter_3d( df, title="Random data")
gitly.show( fig )
```

Change the **scale** where ever you want, and all plots after will scale up or down:

```python
gitly.config_render('git', scale = 0.5) # set default scale for all gitly.show()

fig = px.scatter_3d( df, title="Random data")
gitly.show( fig )
```
## Apply change for a specific plot
Or apply an specific change only to one plot while calling ```.show()``` with more arguments:

```python
fig = px.scatter_3d( df, title="Random data")
gitly.show( fig, height = 333, width = 777, scale = 1.5 ) # this change will be applied only for this plot
```
For more, check this [example](https://github.com/Tiagoeem/gitly/blob/master/examples/Using_Gitly_Example.ipynb)

## License
[MIT](https://choosealicense.com/licenses/mit/)

Created without pretensions by Tiago Sanches da Silva.
