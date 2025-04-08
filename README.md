# Medical Diagnosis System (MDS)

This project is a Medical Diagnosis System (MDS) that predicts diseases based on symptoms provided by the user. It uses machine learning models and a MySQL database to store user information and predictions.

## Features
- User authentication and information storage.
- Disease prediction based on symptoms.
- Interactive web interface.

## Prerequisites

1. **Python**: Ensure Python 3.10 or later is installed.
2. **MySQL**: Install and configure MySQL server.
3. **Docker** (optional): For containerized deployment.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/kevilgs/MedDiagSys.git
   cd MDS
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the MySQL database:
   - Create a database named `mds`.
   - Update the `DB_HOST`, `DB_USER`, `DB_PASSWORD`, and `DB_NAME` environment variables in your system or modify the `create_connection` function in `database.py` with your MySQL credentials.

4. Initialize the database:
   ```bash
   python app.py
   ```
   This will create the necessary tables in the database.

5. Train the model (if needed):
   ```bash
   python train_model.py
   ```

## Running the Application

1. Start the application:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to `http://localhost:5000` to access the web interface.

## Docker Deployment (Optional)

1. Build the Docker image:
   ```bash
   docker build -t mds-app .
   ```

2. Start the application using Docker Compose:
   ```bash
   docker-compose up
   ```

3. Access the application at `http://localhost:5000`.

## Testing

Run the test suite to ensure everything is working correctly:
```bash
python test.py
```

## File Structure
- `app.py`: Main application file.
- `database.py`: Handles database connections and operations.
- `train_model.py`: Script for training the machine learning model.
- `data/`: Contains datasets used for training and testing.
- `model/`: Stores trained models and encoders.
- `templates/`: HTML templates for the web interface.
- `static/`: Static files like CSS.

## Troubleshooting

1. **Database Connection Error**:
   - Ensure MySQL is running and the credentials in `database.py` are correct.

2. **Model Accuracy**:
   - Use the `evaluate_model` function in `train_model.py` to check the accuracy of your models.

3. **Port Conflicts**:
   - Ensure port `5000` is not in use by another application.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- Contributors: Kevil and team.
- Libraries: Scikit-learn, Pandas, MySQL Connector, Flask.