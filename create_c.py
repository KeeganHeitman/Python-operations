import subprocess
def create(f,n):
  subprocess.run(gcc -o(n) (f))
  subprocess.run(rm(f))
  pass
create(input(),input())

#raises error "Traceback (most recent call last):
  File "/home/ghaspingghasp/create.py", line 6, in <module>
    create(input(),input())
  File "/home/ghaspingghasp/create.py", line 3, in create
    subprocess.run(gcc -o (newname) (filename))
NameError: name 'gcc' is not defined"
