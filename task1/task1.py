import pandas as pd
import matplotlib.pyplot as plt

def exercise_0(file): # Load the data
    df = pd.read_csv(file)
    return df

def exercise_1(df): # Get the columns
    columns = df.columns
    return list(columns)

def exercise_2(df, k): # Get the first k rows
    return df.head(k)

def exercise_3(df, k): # Get the random k rows
    return df.sample(k)

def exercise_4(df): # Get the unique rows
    return df.drop_duplicates()
    
def exercise_5(df): # top 10 transactions destinations with frequency
    return df['nameDest'].value_counts().head(10)

def exercise_6(df): # all rows with fraud = 1
    return df[df['isFraud'] == 1]

def exercise_7(df): # Frequency of distinct destinations which each source interacts with in descending order
    return df.groupby('nameOrig')['nameDest'].nunique().sort_values(ascending=False)

def visual_1(df):
    def transaction_counts(df): # Transaction types
        # TODO
        return df['type'].value_counts()
    def transaction_counts_split_by_fraud(df): # Transaction types split by fraud
        # TODO
        return df.groupby(['type', 'isFraud']).size().unstack().fillna(0)

    fig, axs = plt.subplots(2, figsize=(6,10))
    transaction_counts(df).plot(ax=axs[0], kind='bar')
    axs[0].set_title('Transaction types')
    axs[0].set_xlabel('Transaction type')
    axs[0].set_ylabel('Frequency')
    transaction_counts_split_by_fraud(df).plot(ax=axs[1], kind='bar')
    axs[1].set_title('Transaction types split by fraud')
    axs[1].set_xlabel('Transaction type')
    axs[1].set_ylabel('Frequency')
    fig.suptitle('Visual Representation of the required Exercise', fontsize=16)
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    for ax in axs:
      for p in ax.patches:
          ax.annotate(p.get_height(), (p.get_x(), p.get_height()))
    return fig

def visual_2(df):
    def query(df):
        return df[(df['type'] == 'CASH_OUT') & (df['isFraud'] == 1)]
        
    plot = query(df).plot.scatter(x='oldbalanceOrg', y='newbalanceOrig', c='oldbalanceDest')
    plot.set_title('Origin account balance delta v.')
    plot.set_xlim(left=-1e3, right=1e3)
    plot.set_ylim(bottom=-1e3, top=1e3)
    return plot

def exercise_custom(df): # function to get the differences between the old and new balances of the origin accounts for fraudulent transactions
    return df[df['isFraud'] == 1]['newbalanceOrig'] - df[df['isFraud'] == 1]['oldbalanceOrg']
    
def visual_custom(df): # Use the custom function to plot a scatter plot
    plot = df.plot.scatter(x='oldbalanceOrg', y='newbalanceOrig')
    plot.set_title('newbalanceOrig v. oldbalanceOrg')
    plot.set_xlim(left=-1e3, right=1e3)
    plot.set_ylim(bottom=-1e3, top=1e3)
    return plot