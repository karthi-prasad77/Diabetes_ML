FROM python:3.7

# Upgrade pip and setuptools
RUN pip install --upgrade pip setuptools

# Set the working directory inside the container
WORKDIR /app

# Copy the source code to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the Streamlit app
CMD ["streamlit", "run", "main.py"]
