source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
reflex init
reflex export --frontend-only
rm -rf public
unzip frontend.zip -d public
rm -f frontend.zip
source deactivate
