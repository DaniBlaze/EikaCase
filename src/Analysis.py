import pandas as pd
import plotly.express as px

#pd.set_option('display.max_rows', None)
# Read csv file
df = pd.read_csv("/Users/Dani/workspace/EikaCase/resources/loan.csv")

# Get insight on the different loan statuses.
print('\n Grouped by loan status \n')
df_loan_status_grouped = df.groupby(['loan_status'])
print(df_loan_status_grouped.size().sort_values(ascending=False))

# Seperating good loans from bad loans
print('Number of nan rows:', df['loan_status'].isnull().sum().sum())
bad_loan = ['Charged Off', 'Late (31-120 days)', 'In Grace Period', 'Late (16-30 days)', 'Default', 'Does not meet the credit policy. Status:Charged Off']
current_loan = ['Current']

def loan_condition (status):
    if status in bad_loan:
        return 'Dårlig lån'
    elif status in current_loan:
        return 'Nøytralt lån'
    else:
        return 'Bra lån'

df['loan_condition'] = df['loan_status'].apply(loan_condition)

good_vs_bad_loans = df['loan_condition'].value_counts().rename_axis('loan_type').reset_index(name='counts')
print(good_vs_bad_loans)

# Pie chart
fig = px.pie(good_vs_bad_loans, values='counts', names='loan_type')
fig.show()


# Get insight on the different loan statuses combined with grade.
print('\n Grouped by loan status and grade \n')
df_loan_status_and_grade_grouped = df.groupby(['loan_status', 'grade'])
print(df_loan_status_and_grade_grouped.size())

# Get insight on the different employee experience.
print('\n Grouped by employee experience \n')
df_emp_length_grouped = df.groupby(['emp_length'])
print(df_emp_length_grouped.size().sort_values(ascending=False))

# Compare monthly debt/income ratio (dti) for each state
print('\n Grouped by state and mean dti')
df_mean_dti_state_grouped = df.groupby('addr_state', as_index=False)['dti'].mean()
print(df_mean_dti_state_grouped.sort_values('dti'))

fig_bar = px.bar(df_mean_dti_state_grouped.sort_values('dti'), x='addr_state', y='dti')
fig_bar.show()

