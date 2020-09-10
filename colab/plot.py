# Created by Tiago Sanches da Silva: tiago.eem@gmail.com :)
import os

try:
    import sys
    from IPython import get_ipython

    if not('google.colab' in str(get_ipython())):
        print('This script was made to run only on Google Colab notebooks')
        sys.exit()      
except:
    print('This script was made to run only on Google Colab notebooks')
    sys.exit()

print('There are few libs and modules that should be installed in Colab in order to generate static plots from Plotly.' )
print('Summary: Install Orca, update plotly and update apt-get')
print('')
print('apt-get update')
os.system('apt-get update')
print('pip install plotly>=4.0.0')
os.system('pip install plotly>=4.0.0')
print('wget https://github.com/plotly/orca/releases/download/v1.2.1/orca-1.2.1-x86_64.AppImage -O /usr/local/bin/orca')
os.system('wget https://github.com/plotly/orca/releases/download/v1.2.1/orca-1.2.1-x86_64.AppImage -O /usr/local/bin/orca')
print('chmod +x /usr/local/bin/orca')
os.system('chmod +x /usr/local/bin/orca')
print('apt-get install xvfb libgtk2.0-0 libgconf-2-4')
os.system('apt-get install xvfb libgtk2.0-0 libgconf-2-4')
print('Done. Have fun! :)')


class GitlyPlotter:

    static = True
    default_H = 500
    default_W = 1000
    default_S = 1

    def __init__ (self, renderer = 'git'):

        if (renderer.lower() == 'git') or (renderer.lower() == 'github'):
            self.static = True
        else:
            self.static = False

            self.default_H = 500
            self.default_W = 1000
            self.default_S = 1

    def config_render(self, renderer = 'colab', default_height = None, default_width = None, default_scale = None):
        if (renderer == 'colab'):
            self.static = False
        else:
            self.static = True

        if not(default_height == None):
            self.default_H = default_height
        if not(default_width == None):
            self.default_W = default_width
        if not(default_scale == None):
            self.default_S = default_scale

    def show(self, figure = None, **kwargs ):
        from IPython.display import Image, HTML, display

        if figure == None :
            return display(HTML('<h1>Where is my figure?</h1><br><p>You should pass me the figure from plotly, like: gitly.show( fig )<br>Check this easy example: https://github.com/Tiagoeem/gitly/blob/master/examples/Using_Gitly_Example.ipynb'))

        try:
            if self.static:
                if 'width' in kwargs:
                    w = kwargs.get("width")
                else: 
                    w = self.default_W

                if 'height' in kwargs:
                    h = kwargs.get("height")
                else: 
                    h = self.default_H

                if 'scale' in kwargs:
                    s = kwargs.get("scale")
                else: 
                    s = self.default_S

                if 'format' in kwargs:
                    f = kwargs.get("format")
                else: 
                    f = 'png'

                img_bytes = figure.to_image(format=f, width=w, height=h, scale=s)
                return Image(img_bytes)
            else:
                return figure.show()

        except:
            print('Error: Are you sure that you send me a valid plotly figure?')
            print('Please refer: https://github.com/Tiagoeem/gitly')
