FROM python:3.7

# Upgrade pip and setuptools
RUN pip install --upgrade pip setuptools

# Set the working directory inside the container
WORKDIR /src

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code to the container
COPY . .

# Run the Streamlit app
CMD ["streamlit", "run", "main.py"]
