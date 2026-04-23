 Multi-Dimensional Academic Intelligence System

# Overview
This project analyzes student performance using marks, attendance, and assignment scores. It uses structured data and libraries like Pandas and NumPy to perform analysis and generate insights.
# Features

* Random student data generation
* Data stored using lists, tuples, and dictionary
* Conversion to DataFrame for structured analysis
* Statistical calculations:

  * Mean (manual)
  * Median
  * Standard Deviation
  * Correlation
* Student classification:

  * At Risk
  * Average
  * Good
  * Top Performer
* Normalization using list comprehension
* Pattern detection:

  * Consistency
  * Attendance Risk
  * High Achievement
* Optional visualization using matplotlib
  
# Data Structure

Each student record:
(student_id, marks, attendance_percentage, assignment_score)
All records are stored in a list and converted into a DataFrame.

# Functions Used

* generate_data(n): Generates student data
* classify_students(data): Classifies students into categories
* analyze_data(data): Performs statistical analysis and pattern detection

# Personalization Logic

n = 10 + (digit ** 2)
This ensures a minimum of 10 students and creates a unique dataset for each input.

# Performance Index

Performance Index = sqrt(Marks × Assignment) + (Attendance / 2)
This balances academic performance, assignment consistency, and attendance.

# How to Run

1. Install dependencies:
   pip install pandas numpy matplotlib
2. Run the program:
   python file_name.py
3. Enter the roll number last digit when prompted.

# Output

* DataFrame table
* Categorized dictionary
* Statistical summary
* Tuple (mean, standard deviation, maximum marks)
* Final system insight

# Note

Since the program uses the random module, outputs will vary each time.
To get consistent results, use:
random.seed(42)

# Learning Outcome

This project helped in understanding structured data analysis using Pandas and NumPy, statistical computations, and designing custom performance metrics.

# Declaration

This project is created as part of an academic assignment. All work is original.

