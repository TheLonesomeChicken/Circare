# setup
to go your repos folder
`git clone https://github.com/TheLonesomeChicken/Circare`
`cd Circare`
`source venv/bin/activate`

## to start api
for localhost:
`fastapi dev searchAPI.py`
for network:
`fastapi dev searchAPI.py --host 0.0.0.0`

## test the api
`http://127.0.0.1:8000search?q=google`

`q=google` in this case we are looking for `google` because thats what `q` is set to
