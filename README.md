# gitly: Showing plotly graphs in github

This is a home made lib to help you plot your fency graphs from plotly in github while using Google Colab notebook.

## Nbviewer from Github is static!

The problem is that all fency engines that you use on notebooks doesn't run in static viewers, of course there's a lot of ways to generate static images in this libraries. But I use Google Colab by a lot in my classes and I would like to have a easy way to switch betweern dinamic plots and statics plots (to commit and share nice plots in github). So I implement this very simple implementation.

## Easy switch between colab and git "renderers"

Just change from dinamic to static using:

```python
from plotly_in_github import gitly_show, setup_gitly

setup_gitly('github')
```

Now just pass the figure from plotly to ```python gitly_show() ``` and it's done!!!

```python
gitly_show('github')
```
Now you can commit all your fency plots in github! Congratz!

## Can I use both at the same time? Sure u can!

Just use ```python setup_gitly('colab') ``` to switch back in the cell and renderer with default plot from Plotly.

## Check the example here!

<to do>


## License
[MIT](https://choosealicense.com/licenses/mit/)

Created without pretensions by Tiago Sanches da Silva.
