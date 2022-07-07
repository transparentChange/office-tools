import shutil
import sys
from io import StringIO

start_pg = 4
prev_break = '<hr style="page-break-before:always;display:none;"/>'
insert_str = lambda pg_num : '    <p class="pg">' + str(pg_num) + '</p>\n    <p style="page-break-before:always;"></p>\n'

def insert(filename, new_filename):
    file = open(filename, 'r', encoding="utf8")
    lines = file.readlines()
    new_file = StringIO()
    print(prev_break)
    cnt = 0
    for l in lines:
        new_file.write(l)
        if (l.strip() == prev_break):
            cnt += 1
            if (cnt >= start_pg):
                new_file.write(insert_str(cnt - start_pg + 1))

    with open(new_filename, 'w', encoding="utf8") as f:
        new_file.seek(0)
        shutil.copyfileobj(new_file, f)


print(sys.argv)
insert(sys.argv[1], sys.argv[2])