FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy only necessary files
COPY requirements.txt ./
COPY generate_eda.py ./
COPY dashboard ./dashboard
COPY data ./data
COPY sql ./sql
COPY notebooks ./notebooks
COPY charts ./charts
COPY *.md ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose any ports the dashboard might use (assume Flask on 5000)
EXPOSE 8050

# Run the dashboard app when container starts
CMD ["sh", "-c", "python generate_eda.py && python dashboard/app.py"]
