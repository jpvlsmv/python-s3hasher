#!/usr/bin/env python3

import hashlib
import sys
from io import BytesIO

import boto3
import click

assert sys.version_info >= (3, 6)


@click.command()
@click.option('--limit',  '-l', default=50,   help='Limit number of files checked')
@click.option('--bucket', '-b', default=None, help='bucket name')
def main(limit, bucket):
    s3 = boto3.resource('s3')
    if bucket is None:
        bucketlist = s3.buckets.all()
    else:
        bucketlist = [s3.Bucket(bucket)]
    for bucket in bucketlist:
        print(bucket.name)
        for obj in bucket.objects.all().limit(limit):
            if obj.key.endswith('/'):
                print(f'\tDirectory {obj.key}')
            else:
                resp = obj.get()
                h = hashlib.sha256()
                for f in BytesIO(resp["Body"].read()):
                    h.update(f)
                click.echo(f'\t\t{h.hexdigest()}  {obj.key}\n')


if __name__ == '__main__':
    main()
