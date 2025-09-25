import csv


def merge_csv(file1_path, file2_path, result_path, key):
    with open(file1_path, newline='', encoding='utf-8') as f1, \
            open(file2_path, newline='', encoding='utf-8') as f2, \
            open(result_path, 'w', newline='', encoding='utf-8') as out:

        r1 = list(csv.DictReader(f1))
        r2 = list(csv.DictReader(f2))

        h1 = list(r1[0].keys())
        h2 = list(r2[0].keys())
        header = [key] + [c for c in h1 if c != key] + [c for c in h2 if c != key]

        w = csv.DictWriter(out, fieldnames=header)
        w.writeheader()

        idx1 = {row[key]: row for row in r1}
        idx2 = {row[key]: row for row in r2}

        common_keys = set(idx1.keys()) | set(idx2.keys())

        for k in common_keys:
            row1 = idx1[k]
            row2 = idx2[k]
            out_row = {key: k}

            for c in h1:
                if c != key:
                    out_row[c] = row1.get(c, '')

            for c in h2:
                if c != key:
                    out_row[c] = row2.get(c, '')

            w.writerow(out_row)
