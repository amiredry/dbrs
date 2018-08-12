from sodapy import Socrata
import csv
import sys

socrata_domain = 'data.cityofnewyork.us'
socrata_dataset_identifier = 'fhrw-4uyv'


def get_data():
    client = Socrata(socrata_domain, 'ohJoNJOw8qez7ABLZhzGUja4n')
    lmt = 1000000
    start_at = 0
    all_complaints = []

    while True:

        complaints = client.get(socrata_dataset_identifier,
                                limit=lmt,
                                offset=start_at,
                                order="created_date ASC",
                                select="created_date, borough, complaint_type, incident_zip",
                                where="created_date between '2017-01-01T00:00:00' and '2017-12-31T23:59:59'")

        all_complaints.extend(complaints)
        start_at += lmt

        if len(complaints) < lmt:
            break

    headers = ['created_date', 'borough', 'complaint_type', 'incident_zip']

    with open('complaint.csv', 'w') as f:

        csvwriter = csv.DictWriter(f, headers)
        csvwriter.writeheader()
        csvwriter.writerows(all_complaints)

    print('SUCCESS. Number of complaints downloaded: {}'.format(len(all_complaints)))
    print('Saved to {} file'.format('complaint.csv'))


def main():

    try:
        get_data()

    except:
        print("Unexpected error:", sys.exc_info()[0])


if __name__ == '__main__':
    main()
