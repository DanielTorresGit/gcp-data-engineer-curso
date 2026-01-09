from google.cloud import bigquery


def query_public_dataset    ():
    client = bigquery.Client()

    query = """
        SELECT * FROM `bigquery-public-data.america_health_rankings.ahr` LIMIT 1000
    """

    query_job = client.query(query)
#results = query_job.result() --se cambia para que quede en formato data frame
    results = query_job.to_dataframe() [:5]


#se comentareo para que imprimiera todo el data frame porque ya no esta en formato de filas
#    for row in results:
#        print(row) 
    print(results)

if __name__ == "__main__":
    query_public_dataset()