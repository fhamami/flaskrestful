from subprocess import call

call('git add .', shell=True)
call('git status', shell=True)
print('please input an commit message bellow')
committext = raw_input('')
call('git commit -m "' + committext + '"', shell=True)
print('please input branch name bellow')
branch = raw_input('')
call('git push -u origin ' + branch, shell=True)
