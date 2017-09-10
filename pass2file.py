import os
import subprocess

root = os.path.expanduser('~/.password-store')
dest = os.path.expanduser('/tmp/pass.txt')

with open(dest, 'w') as out:

    for subdir, dirs, files in os.walk(root):
        if '.git' not in subdir:
            for f in files:
                if f.endswith('.gpg'):
                    path = os.path.join(subdir, f)
                    relpath = os.path.relpath(path, root)
                    pass_name = relpath[:-4]
                    p = subprocess.Popen(['pass', pass_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    output = p.communicate()[0]
                    data = output.decode('utf-8')
                    out.write(pass_name)
                    out.write(': ')
                    out.write(data)
                    out.write('\n')
