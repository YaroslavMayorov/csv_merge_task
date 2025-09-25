import csv


def merge_csv(file1_path, file2_path, result_path, key):
    with open(file2_path, newline="", encoding="utf-8") as f2:
        r2 = csv.DictReader(f2)
        file2_fields = [c for c in r2.fieldnames if c != key]
        index2 = {}
        for row in r2:
            k = row.get(key)
            if k is not None:
                index2[k] = row

    with open(file1_path, newline="", encoding="utf-8") as f1, \
            open(result_path, "w", newline="", encoding="utf-8") as out:
        r1 = csv.DictReader(f1)
        file1_fields = [c for c in r1.fieldnames if c != key]

        header = [key] + file1_fields + file2_fields
        w = csv.DictWriter(out, fieldnames=header)
        w.writeheader()

        for row1 in r1:
            k = row1.get(key)
            if not k:
                continue
            row2 = index2.get(k)
            if row2 is None:
                continue

            combined = {h: "" for h in header}
            combined[key] = k
            for c in file1_fields:
                combined[c] = row1.get(c, "")
            for c in file2_fields:
                combined[c] = row2.get(c, "")
            w.writerow(combined)
