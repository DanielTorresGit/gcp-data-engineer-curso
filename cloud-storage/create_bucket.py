import argparse
from google.cloud import storage


def main():
    # Crear el parser de argumentos
    parser = argparse.ArgumentParser(
        description="Create a GCP bucket."
    )

    # Argumentos por línea de comandos
    parser.add_argument(
        "bucket_name",
        type=str,
        help="Name of the bucket to create"
    )

    args = parser.parse_args()

    bucket_name = args.bucket_name

    # Crear cliente de Storage
    storage_client = storage.Client()

    # Crear el bucket
    bucket = storage_client.create_bucket(bucket_name)

    # Configurar la clase de almacenamiento
    bucket.storage_class = "STANDARD"

    print(
        f"Bucket {bucket.name} created in {bucket.location} "
        f"with class {bucket.storage_class}"
    )


if __name__ == "__main__":
    main()
