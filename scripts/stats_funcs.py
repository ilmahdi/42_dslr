import math


def count(values):
    return len(values)


def mean(values):
    n = len(values)
    return sum(values) / n if n else None


def std(values, ddof=1):
    n = len(values)
    avg = mean(values)
    if n <= ddof or avg is None:
        return None
    return math.sqrt(sum((x - avg) ** 2 for x in values) / (n - ddof))


def minimum(values):
    return min(values) if values else None


def maximum(values):
    return max(values) if values else None


def quantile(values, q):
    if not values:
        return None
    sorted_vals = sorted(values)
    pos = q * (len(sorted_vals) - 1)
    lower = int(math.floor(pos))
    upper = int(math.ceil(pos))
    if lower == upper:
        return sorted_vals[int(pos)]
    return sorted_vals[lower] * (upper - pos) + sorted_vals[upper] * (pos - lower)


def median(values):
    return quantile(values, 0.5)
