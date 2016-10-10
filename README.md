# tick

A simple library to compute revenue from [Tock](https://github.com/18F/tock).

## Installation

```sh
git clone git@github.com:vzvenyach/tick.git
cd tick
pyvenv env
source env/bin/activate
mv .env.example .env
pip install requirements.txt
```

Then, edit `.env` to add your Tock API Key.

## Usage

To use `tick`, you must pass three arguments:

1. Start Date
2. Project ID
3. The Profit and Loss associated with the project ("Acq", "PIF", "18F")

```sh
python run.py 2016-10-02 415 Acq
# {'start_date': '2016-10-02', 'project_id': '415', 'hours': 28.75, 'project_name': 'TTS Acq / Consulting / Department of Transportation FHWA Data', 'revenue': 7853.75}
```

## License

CC0-1.0
