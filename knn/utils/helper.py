import pandas as pd
from sklearn.preprocessing import LabelEncoder

class HELPER:
    def __init__(self):
        pass

    def encoding (self,df,encode = 'label_encode'):

        if encode == 'label_encode':
            #converting string categorical values to integer for Sequence_Name
            le2 = LabelEncoder()
            df['Sequence_Name'] = le2.fit_transform(df['Sequence_Name' ])
            return df
        elif encode == 'one_hot_encode':
            # use pd.concat to join the new columns with your original dataframe
            df = pd.concat([df,pd.get_dummies(df['Sequence_Name'], prefix='Sequence_Name')],axis=1)

            # now drop the original 'Sequence_Name' column (you don't need it anymore)
            df.drop(['Sequence_Name'],axis=1, inplace=True)

            return df

    def get_data(self,do_it = False):
        print(do_it)
        if do_it == False:
            return
        with open('data/ecoli.txt') as input_file:
           lines = input_file.readlines()
           newLines = []
           for line in lines:
              newLine = line.strip().split()
              newLines.append( newLine )

        with open('data/ecoli.csv', 'w') as test_file:
           file_writer = csv.writer(test_file)
           file_writer.writerows( newLines )
