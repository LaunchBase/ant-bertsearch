

from elasticsearch import Elasticsearch
index_name = 'ant-training'
index_file_name = './ant-training-index.json'

def main():
	client = Elasticsearch()
	client.indices.delete(index=index_name, ignore=[404])
	with open(index_file_name) as index_file:
		source = index_file.read().strip()
		client.indices.create(index=index_name, body=source)


if __name__ == '__main__':
    main()