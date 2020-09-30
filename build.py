"""
build.py
----------

Run a simple static site generation to build an example shop webpage.
"""

import os
import jinja2
import requests


def get_shop(shopId,
             API_KEY=None,
             API_ROOT=None):
    """
    Get the shop document stored in Kerfed.

    Parameters
    -----------
    shopId : str
      Identifier of shop on Kerfed
    API_KEY : None or str
      Kerfed API key, can be generated at kerfed.com/account
    API_ROOT : None or str
      URL for kerfed API, by default kerfed.com/api/v1

    Returns
    --------
    shop : dict
      Shop document retrieved from API
    """
    if API_KEY is None:
        # your API key
        API_KEY = os.environ['KERFED_API_KEY']
    if API_ROOT is None:
        # the default location of the Kerfed V1 API
        API_ROOT = 'https://kerfed.com/api/v1'
        
    # Create a Kerfed API session using our API key
    with requests.Session() as s:
        s.headers.update({
            'Content-Type': 'application/json',
            'x-api-key': API_KEY})

        # get the shop document, containing name, address, and other info
        shop_response = s.get(f'{API_ROOT}/shops/{shopId}')
        if shop_response.status_code != 200:
            raise ValueError(shop_response.text)

        # get the JSON shop document
        shop = shop_response.json()

    return shop


if __name__ == '__main__':


    # where to write the resulting site
    path_out = 'html'
    # templates to skip rendering
    blacklist = ['base.html']
    
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader('templates'))

    # get the information about the shop we're making a site for
    shop = get_shop(shopId='leland')
        
    for file_name in env.list_templates():
        if file_name in blacklist:
            continue
        if '#' in file_name or '~' in file_name:
            continue
        try:
            # make directories if necessary
            os.makedirs(
                os.path.dirname(
                    os.path.join(path_out, file_name)))
        except BaseException:
            pass
        # pass the name of the template we're rendering
        active = file_name.lower().replace('.html', '')
        # render the jinja2 template with the shop and current page name
        rendered = env.get_template(file_name).render(shop=shop, active=active)

        # write the rendered result
        with open(os.path.join(path_out, file_name), 'w') as f:
            f.write(rendered)
