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

    def __init__ (self, renderer = 'git'):

        if (renderer.lower() == 'git') or (renderer.lower() == 'github'):
            self.static = True
        else:
            self.static = False

    def switch_renderer(self, renderer = 'colab'):
        if (renderer == 'colab'):
            self.static = False
        else:
            self.static = True

    def show(self, figure = None ):
        from IPython.display import Image, HTML, display

        if figure == None :
            return display(HTML('<h1>Where is my figure?</h1><br><p>You should pass me the figure from plotly, like: gplt.show( fig )<br>Check <a href="https://github.com/Tiagoeem/gitly/blob/master/examples/Using_Gitly_Example.ipynb"> this easy example</a>'))

        try:
            if self.static:
                img_bytes = figure.to_image('png')
                return Image(img_bytes)
            else:
                return figure.show()

        except:
            print('Error: Are you sure that you send me a valid plotly figure?')
            print('Please refer: https://github.com/Tiagoeem/gitly')
