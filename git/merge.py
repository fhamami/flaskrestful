from subprocess import call

call('git checkout master', shell=True)
print('checkout to master')
call('git pull origin master', shell=True)
print('please type branch name')
branchname = raw_input('')
call('git merge "' + branchname + '"', shell=True)
print('please type branch name to merge')
branch = raw_input('')
call('git push origin ' + branch, shell=True)

# https://stackoverflow.com/questions/5601931/best-and-safest-way-to-merge-a-git-branch-into-master
