import pandas as pd
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Math': [85, 92, 78, 90, 88],
    'Science': [91, 89, 85, 93, 90],
    'English': [88, 94, 82, 87, 91]
}

data = pd.DataFrame(data)
print("Original DataFrame:")
print(data)

filter_row = data[data['Science']>=90]
print("\nStudents with Science score above or equal 90:")
print(filter_row)

data['Total'] = data['Math'] + data['Science'] + data['English']
print("\nDataFrame with Total Score column:")
print(data)

print("\n",data.describe())