# Base image: Choose a Python version suitable for your project
FROM python:3.8

# Working directory: Set a clear working directory
WORKDIR /app

# Copy project files: Copy entire project structure
COPY . /app

# Install Python dependencies: Use a virtual environment for better isolation
RUN apt-get update && apt-get install -y python3
RUN pip install -r requirements.txt

# Optional: Set environment variables for sensitive data or configurations
# ENV MY_SECRET_KEY=my_secret_value

# Entrypoint: Define the default command to execute when the container starts
#CMD ["python3", "Level-3\TABLE-4_CAST_COST_performance.py"]  # Replace "main.py" with your main script

CMD python TABLE-4_CAST_COST_performance.py && python TABLE-2_BIT_STRING_Performance.py && python Table-7_Transient_cast.py && python Table-5_Neighbors_preformance.py && python Figure-7_NumberofTyped_VS_Runtime.py && python Figure-9_NumberofTyped_VS_RunTime_transient.py && python Barchart.py
