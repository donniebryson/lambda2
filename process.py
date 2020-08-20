import io
from io import StringIO
import pandas as pd
from fbprophet import Prophet
client = boto3.client('s3')
obj = client.get_object(Bucket='donniebrysonplaybucket', Key='input/example_retail_sales.csv')
df = pd.read_csv(io.BytesIO(obj['Body'].read()))
#df = pd.read_csv('input.csv', sep='\t')

df.head()
# Python
m = Prophet()
m.fit(df)
# Python
future = m.make_future_dataframe(periods=365)
future.tail()
# Python
forecast = m.predict(future)
output = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
output.to_csv('donnie.csv')
s3 = boto3.resource('s3')
s3.Object('donniebrysonplaybucket','output/donnie.csv').upload_file(Filename='donnie.csv')
#
