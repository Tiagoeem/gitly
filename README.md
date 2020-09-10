# gitly: Showing plotly graphs in github

This is a home made lib to help you plot your fency graphs from plotly in github while using Google Colab notebook.

## Nbviewer from Github is static!

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

## Can I use both at the same time? Sure you can, at any time!

Just use ```gitly.switch_renderer('colab') ``` to switch back in the cell and renderer with default plot from Plotly.

## Check the example here!

<to do>

# Instalation

This lib is intended to be used only on Google Colab notebooks.

Open a cell and run the following code:

```!pip install -i https://test.pypi.org/simple/ gitly==0.0.2 ```


## License
[MIT](https://choosealicense.com/licenses/mit/)

Created without pretensions by Tiago Sanches da Silva.
