import argparse
import json

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

data_file = './vectors/documents_1580776041981.jsonl'

def load_dataset():
	with open(data_file) as f:
		return [json.loads(line) for line in f]


def main():
    client = Elasticsearch()
    docs = load_dataset()
    bulk(client, docs)


if __name__ == '__main__':
    main()