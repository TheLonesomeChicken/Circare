# Modded version of https://github.com/TheLonesomeChicken/Circare

# setup
to go your repos folder
```bash
git clone https://github.com/rapsacclion/Circare
cd Circare
source venv/bin/activate
```

## to start api
for localhost:
`fastapi dev searchAPI.py`
for network:
`fastapi dev searchAPI.py --host 0.0.0.0`

## test the api
`http://127.0.0.1:8000/search?q=value`

`q=value` would be searching for `value` in the above link
