![](https://cdn.discordapp.com/attachments/1164599259518226574/1293292816725971084/ciii.png?ex=6706d84b&is=670586cb&hm=6390cbe5182a1d669bf424b2f470fc42dff9f7266b2308c9a6ed0c700d13c287&)

<h1 align="center">💉 CacheInject 📂</h1>
<p align="center">CacheInject is a simple way to hide code in the pycache, that anyone shouldn't see. It's not working for cross-versions. The code will execute only if the user that execute the code is on the same version as the user who built the infected code.</p>

## 🔽 Installation
```
git clone https://github.com/Izak57/CacheInject.git
cd CacheInject
pip install .
```

## ❓ Usage
```
py -m cacheinject [-h] codefile module

Inject code to a pycache.

positional arguments:
  codefile    Path to the file that contains the code you want to inject
  module      The module path were the code will be injected

options:
  -h, --help  show this help message and exit
```

## ❓ Usage example
```
py -m cacheinject ./hiddenCode.py ./script/constants.py
```

Now if you run a code were there is `import constants` or `from constants import`,
if will run the code in `hiddenCode.py`.