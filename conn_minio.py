from minio import Minio
from minio.error import S3Error
import io
import pyarrow as pa
import pyarrow.parquet as pq

def connect_minio():

    minio_client = Minio(
        "localhost:9000",
        access_key="qdjqh5hPZe8X7y6alCkJ",
        secret_key="gGYkMcb5L0fn3GqukfxmayHJ3X8Ms8x6OC2zkGAk",
        secure=False
    )

    return minio_client
