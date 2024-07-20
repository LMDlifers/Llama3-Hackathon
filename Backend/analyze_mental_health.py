# analyze_mental_health.py
def analyze_mental_health(index, query):
    response = index.query(query)
    return response
