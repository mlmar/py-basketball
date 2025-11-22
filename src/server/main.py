from lib.stats.stats import get_all, get_averages, get_totals

days = int(input('Last N Days (Excluding today): '))
get_all(days)
get_averages(days)
get_totals(days)