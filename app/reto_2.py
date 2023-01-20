import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item :item['Continent']== 'South America', data))

  countries = list(map(lambda x: x["Country/Territory"], data))
  percentages = list(map(lambda x: x["World Population Percentage"], data))

  charts.generate_pie_chart(countries, percentages)
'''
def run (): # otra solucion con comprehensions definido en utils.py
  data = read_csv.read_csv('./app/data.csv')
  countries, percentages = utils.get_world_percentages(data)
  charts.generate_pie_chart(countries, percentages)
'''
if __name__ == '__main__': 
  run()