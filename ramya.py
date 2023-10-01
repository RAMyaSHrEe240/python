
import pandas as pd
import matplotlib.pyplot as plt


plt.rcParams['figure.figsize'] = [13,6] 
plt.style.use('ggplot')

dec2018 = pd.read_csv("coinmarketcap.csv")

print(dec2018)

m_capital = dec2018[['id','market_cap_usd']].query('market_cap_usd > 0')

print(m_capital.count())


chart_title = 'Top 10 crypto in terms of market capitalization in 2018'
chart_y_label = '% of total market capitalization'
m_cap10 = m_capital.head(10).set_index(m_capital.id[:10])
m_cap10 = m_cap10.assign(market_cap_perc = lambda x: (x.market_cap_usd/m_capital.market_cap_usd.sum())*100)
ax = m_cap10.plot.bar(x='id', y='market_cap_perc', title=chart_title)
ax.set_ylabel(chart_y_label)
plt.xticks(rotation=45) 
plt.show()