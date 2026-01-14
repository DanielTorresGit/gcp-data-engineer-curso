import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions


def run():
    #Configurar las opciones del pipeline
    options = PipelineOptions(
        runner='DataflowRunner',  # Cambiar "DirectRunner" a 'DataflowRunner' para ejecutar en Google Cloud Dataflow
        project='gcp-data-engineer-curso-480819',
        zone='us-west1-b', # me lo pidio crear cuando no habia servidores disponibles en la region
        worker_machine_type='e2-micro',     
        num_workers=1,
        temp_location='gs://gcs-bucket_curso/temp',
        region='us-west1'
    )

    with beam.Pipeline(options=options) as p:
        (
            p
            | "leer archivo" >> beam.io.ReadFromText('gs://dataflow-samples-local/ReyLear.txt')
            | "dividir en palabras" >> beam.FlatMap(lambda linea: linea.split())
            | "contar palabras" >> beam.combiners.Count.PerElement()
            | "escribir resultados" >> beam.io.WriteToText('gs://gcs-bucket_curso/output/wordcount')
        )

if __name__ == '__main__':
    run()