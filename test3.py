import pandas as pd

'''Exemplos
data = pd.DataFrame({
    'Days':['Monday','Tuesday','Wednesday'], 'Months':['Jan','Feb','March']
})
print(data)
'''

d={
    "name":pd.Series(["Braund", "Cummings", "Heikkinem", "Allen"],index=["a",'b','c','d']),
    "age":pd.Series([22,38,26,35],index=["a",'b','c','d']),
    "fare":pd.Series([7.25,71.83,8.05],index=["a","b","d"]),
    "survived?":pd.Series([False,True,True,False],index=["a",'b','c','d'])
}

df = pd.DataFrame(d)
print(df)

