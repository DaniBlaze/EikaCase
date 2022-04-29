import pandas as pd

pd.set_option('display.max_rows', None)
# Read csv file
df = pd.read_csv("/Users/Dani/workspace/EikaCase/resources/loan.csv")

# Get insight on the different loan statuses.
print('\n Grouped by loan status \n')
df_loan_status_grouped = df.groupby(['loan_status'])
print(df_loan_status_grouped.size().sort_values(ascending=False))

# Get insight on the different loan statuses combined with grade.
print('\n Grouped by loan status and grade \n')
df_loan_status_and_grade_grouped = df.groupby(['loan_status', 'grade'])
print(df_loan_status_and_grade_grouped.size())

# Get insight on the different employee experience.
print('\n Grouped by employee experience \n')
df_emp_length_grouped = df.groupby(['emp_length'])
print(df_emp_length_grouped.size().sort_values(ascending=False))