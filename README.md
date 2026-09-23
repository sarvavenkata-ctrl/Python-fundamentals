# Example Project

A public GitHub portfolio project demonstrating Python fundamentals, data processing, and visualisation skills for AI/ML and software engineering roles.

## Project Overview
This project contains a simple but practical **Marks/Grade Predictor** application that:
- takes student marks as input
- validates the values
- calculates the average score
- assigns a grade based on performance
- presents the results using a small data-driven visualisation

The project is designed to showcase skills in:
- Python programming
- input validation and conditional logic
- NumPy for numerical calculations
- Pandas for structured data handling
- Matplotlib for charts and visualisation
- Git and GitHub portfolio management

## Features
- User-friendly command-line interface
- Marks validation to prevent invalid inputs
- Grade prediction based on average score
- Visual summary using matplotlib
- Clean, beginner-friendly code suitable for a portfolio

## Technologies Used
- Python
- NumPy
- Pandas
- Matplotlib
- Git
- GitHub

## Repository Purpose
This repository is intended to be a public project visible to recruiters and hiring teams, especially on platforms such as AWS job portals and GitHub portfolio reviews.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/sarvavenkata-ctrl/Example-Project.git
   cd Example-Project
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the project:
```bash
python marks_grade_predictor.py
```

Follow the prompts to enter marks for each subject. The script will:
- validate the input
- calculate the average
- display the predicted grade
- generate a bar chart

## Example Output
```text
Enter the number of subjects: 5
Enter marks for Subject 1: 85
Enter marks for Subject 2: 90
Enter marks for Subject 3: 78
Enter marks for Subject 4: 88
Enter marks for Subject 5: 92

Average Mark: 86.60
Predicted Grade: A
Performance: Distinction
```

## Project Structure
```text
Example-Project/
├── README.md
├── .gitignore
├── requirements.txt
├── marks_grade_predictor.py
└── .venv/  # created locally when using a virtual environment
```

## License
This project is open for educational and portfolio use.

## Author
Sarva Venkata
