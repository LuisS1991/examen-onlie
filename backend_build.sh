pip install --upgrade pip && \
pip install --no-cache-dir -r requirements.txt && \
reflex db makemigrations --message "something changed" && \
reflex db migrate
