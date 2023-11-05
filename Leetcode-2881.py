import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees.insert(loc = 2,
          column = 'bonus',
          value = employees['salary'] * 2)
    return employees