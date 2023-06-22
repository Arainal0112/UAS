import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.stats import kstest, norm

print('------------------- UAS STATISTIK KOMPUTASI -------------------')
print('Arainal Aldiansyah(05) - TI-2G - 2141720042')

data = pd.read_csv('walmart.csv')

# store_Code = 4
# data_penjualan = data.loc[data['Store'] == store_Code]
# print('---------------------------------------------------------------')

#1 
#a
# #1. B
# print('---------------------------------------------------------------')
# data_penjualan = data[data['Store'] == store_Code]
    
# weekly_Sales = data_penjualan['Weekly_Sales'].describe()
# holiday_flag = data_penjualan['Holiday_Flag'].describe()
# temperature = data_penjualan['Temperature'].describe()
# fuel_price = data_penjualan['Fuel_Price'].describe()
# customer_price_index = data_penjualan['CPI'].describe()
# unemployment = data_penjualan['Unemployment'].describe()
    
# print("1. B - Nilai Statistik Untuk STORE 4")
# print('---------------------------------------------------------------')
# print("Weekly Sale:")
# print(weekly_Sales)
# print('---------------------------------------------------------------')
# print("Holiday Flag:")
# print(holiday_flag)
# print('---------------------------------------------------------------')
# print("Temperature:")
# print(temperature)
# print('---------------------------------------------------------------')
# print("Fuel Price:")
# print(fuel_price)
# print('---------------------------------------------------------------')
# print("Customer Price Index:")
# print(customer_price_index)
# print('---------------------------------------------------------------')
# print("Unemployment:")
# print(unemployment)
# print('---------------------------------------------------------------')

# print("1. C - Nilai Q1,Q2,Q3 dan IQR untuk Fuel_Price, CPI, dan Unemployemnt pada Store 4")
# print('---------------------------------------------------------------')
# f_p_q1 = data_penjualan['Fuel_Price'].quantile(0.25)
# f_p_q2 = data_penjualan['Fuel_Price'].quantile(0.50)
# f_p_q3 = data_penjualan['Fuel_Price'].quantile(0.75)
# f_p_iqr = f_p_q3 - f_p_q1

# cpi_q1 = data_penjualan['CPI'].quantile(0.25)
# cpi_q2 = data_penjualan['CPI'].quantile(0.50)
# cpi_q3 = data_penjualan['CPI'].quantile(0.75)
# cpi_iqr = cpi_q3 - cpi_q1

# unemployment_q1 = data_penjualan['Unemployment'].quantile(0.25)
# unemployment_q2 = data_penjualan['Unemployment'].quantile(0.50)
# unemployment_q3 = data_penjualan['Unemployment'].quantile(0.75)
# unemployment_iqr = unemployment_q3 - unemployment_q1
    

# print("Fuel Price :")
# print("Nilai Q1 :", f_p_q1)
# print("Nilai Q2 :", f_p_q2)
# print("Nilai Q3 :", f_p_q3)
# print("Nilai IQR:", f_p_iqr)
# print('---------------------------------------------------------------')
# print("Customer Price :")
# print("Nilai Q1 :", cpi_q1)
# print("Nilai Q2 :", cpi_q2)
# print("Nilai Q3 :", cpi_q3)
# print("Nilai IQR:", cpi_iqr)
# print('---------------------------------------------------------------')
# print("Unemployment :")
# print("Nilai Q1 :", unemployment_q1)
# print("Nilai Q2 :", unemployment_q2)
# print("Nilai Q3 :", unemployment_q3)
# print("Nilai IQR:", unemployment_iqr)

# print("1. D Variansi dari 1 - holiday week dan 0 - non holiday week")
# print('---------------------------------------------------------------')
# data_holiday_week = data.groupby('Holiday_Flag')['Weekly_Sales'].var()
# for flag, variance in data_holiday_week.items():
#             if flag == 1:
#                         print(" Variansi Holiday Week : ")
#             else:
#                         print(" Variansi Non-Holiday Week : ")
#             print(variance)

# 1 E
# rata_rata_weekly_sales = data.groupby('Store')['Weekly_Sales'].mean()
# print(rata_rata_weekly_sales)

#1 F
# print("1. F -  Dari setiap toko, CPI yang Lebih tinggi")
# max_cpi_by_store = data.groupby('Store')['CPI'].max()
# higher_cpi_by_store = max_cpi_by_store.idxmax()
# higher_cpi_value = max_cpi_by_store.max()
    
# print(f"CPI Tertinggi adalah {higher_cpi_value} dari Store {higher_cpi_by_store}")
# # for store_id in max_cpi_by_store.index:
# #             cpi_value = max_cpi_by_store.loc[store_id]
# #             print(f"Store ID: {store_id} CPI : {cpi_value}")
        
# print('1. G - CPI mana yang lebih tinggi, holiday week atau non')
# rata_holiday = data[data['Holiday_Flag'] == 1]['CPI'].mean()
# rata_non_holiday = data[data['Holiday_Flag'] == 0]['CPI'].mean()
# print("Rata-rata CPI pada holiday week", rata_holiday)
# print("Rata-rata CPI pada Non holiday week", rata_non_holiday)

# alpha = 0.05
# ks_statistic_weekly_sales, p_value_weekly_sales = stats.kstest(data['Weekly_Sales'], 'norm')
# is_weekly_sales_normal = p_value_weekly_sales > alpha
    
# ks_statistic_fuel_price, p_value_fuel_price = stats.kstest(data['Fuel_Price'], 'norm')
# is_fuel_price_normal = p_value_fuel_price > alpha
    
# print("Hasil analisis uji normalitas:")
# print("Kolom 'Weekly_Sales':")
# print("KS statistic:", ks_statistic_weekly_sales)
# print("P-value:", p_value_weekly_sales)
# if is_weekly_sales_normal:
#             print("Data Weekly_Sales' berasal dari distribusi normal.")
# else:
#             print("Data 'Weekly_Sales' tidak berasal dari distribusi normal.")
# print("Kolom 'Fuel_Price':")
# print("KS statistic:", ks_statistic_fuel_price)
# print("P-value:", p_value_fuel_price)
# if is_fuel_price_normal:
#             print("Data 'Fuel_Price' berasal dari distribusi normal.")
# else:
#             print("Data 'Fuel_Price' tidak berasal dari distribusi normal.")

# # 3.A
# correlation = data[['Holiday_Flag', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment', 'Weekly_Sales']].corr()
# print("3 a. Korelasi antar variabel independen ")
# print(correlation['Weekly_Sales'])

# # 3.B
# correlation = data[['Holiday_Flag', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment', 'Weekly_Sales']].corr()
# negative_correlations = correlation[correlation['Weekly_Sales'] < 0]
# negative_correlations = negative_correlations['Weekly_Sales'].drop('Weekly_Sales', errors='ignore')
# if negative_correlations.empty:
#             print("Tidak ada pasangan variabel independen dan dependen dengan korelasi negatif.")
# else:
#             print("Pasangan variabel independen dan dependen dengan korelasi negatif:")
#             print(negative_correlations)

# 4
class Nomor4() :
    print()
    print('Nomer 4')
    data = data[['Fuel_Price', 'Weekly_Sales']]

    X = data[['Fuel_Price']]
    y = data['Weekly_Sales']

    model = LinearRegression()
    model.fit(X, y)

    a = model.intercept_
    b = model.coef_[0]

    print("Model regresi: y = {} + {}x".format(a, b))
    data = data[['Fuel_Price', 'Weekly_Sales']]

    X = data[['Fuel_Price']]
    y = data['Weekly_Sales']

    model = LinearRegression()

    model.fit(X, y)
    y_pred = model.predict(X)
    plt.scatter(X, y, color='blue', label='Data')
    plt.plot(X, y_pred, color='red', linewidth=2, label='Regression Line')

    plt.xlabel('Fuel_Price')
    plt.ylabel('Weekly_Sales')
    plt.title('Linear Regression')

    plt.legend()

    plt.show()