import gzip
import delegator


def run():
    database = 'local'

    with gzip.open('bkp_'+database+'.zip', 'wb') as f:
        c = delegator.run('pg_dump -h localhost -U postgres postgres')
        print(c.out)
        f.write(c.out.encode('utf-8'))

if __name__ == '__main__':
    run()