#!/usr/bin/env python3
import csv
from collections import Counter

CSV_FILE = 'tickets.csv'

def read_tickets(path):
    with open(path, newline='') as f:
        return list(csv.DictReader(f))

def summary(tickets):
    total = len(tickets)
    by_priority = Counter(t['priority'] for t in tickets)
    by_status = Counter(t['status'] for t in tickets)
    return total, by_priority, by_status

if __name__ == '__main__':
    tickets = read_tickets(CSV_FILE)
    total, by_priority, by_status = summary(tickets)
    print(f"Total tickets: {total}")
    print('By priority:')
    for k,v in by_priority.items():
        print(f'  {k}: {v}')
    print('By status:')
    for k,v in by_status.items():
        print(f'  {k}: {v}')

    with open('summary.txt', 'w') as out:
        out.write(f"Total tickets: {total}\n")
        out.write('By priority:\n')
        for k,v in by_priority.items():
            out.write(f"  {k}: {v}\n")
        out.write('By status:\n')
        for k,v in by_status.items():
            out.write(f"  {k}: {v}\n")
    print('\nsummary.txt created')
