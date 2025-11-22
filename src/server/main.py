from lib.stats.stats import get_all, get_averages, get_totals
from lib.ai.gemini import get_analysis

days = int(input('Last N Days (Excluding today, max of 10): '))
days = min(days, 10)

# get_all(days)
averages = get_averages(days)
# get_totals(days)
print('------')

get_analysis(averages, 'averages', days)