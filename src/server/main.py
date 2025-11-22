from lib.stats.stats import get_all, get_averages, get_totals
from lib.ai.gemini import test_gemini

days = int(input('Last N Days (Excluding today): '))
# get_all(days)
averages = get_averages(days)
# get_totals(days)

test_gemini(averages)