from zeep import Client

client = Client('https://subaggregator.pdslkenya.com:8084/pdslvending/Requests?wsdl')
meter_response = client.service.prepaidMeterQuery('9897', '22119337610')
prepaid=client.service.prepaidVend('9897','22119337610', '200')
postpaid=client.service.postpaidVend('9897', '22119337610', '200', '254741151005')
airtime=client.service.postpaidVend('9897', 'orange_100', '200')


print(meter_response,prepaid, postpaid, airtime)
