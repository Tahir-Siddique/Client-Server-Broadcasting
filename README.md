# Client Server Broadcasting

Client server broadcasting script is created to broadcast from one PI to multiple PI's within same network.

## Installation
Make Sure PYTHON 3 is Installed already
1. You need install pyaudio
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pyaudio.

```bash
pip install pyaudio
```

[1] You can create virtual environment and then install pyaudio

2. Activate environment if not and run `server.py`. To run type

```bash
> python server.py


IP: 192.168.0.101
PORT: 5000

```

## To use listen on other PI's
To use listen on other PI's you need to do the same for one step. But for 2nd step you need to run `client.py`

```bash
python client.py IP PORT
```
Before running this script you should replace IP and Port that was generated in previous command while executing `python server.py`.