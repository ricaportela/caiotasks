#!/bin/sh

repo_name=$1
test -z $repo_name && echo "Repo name required." 1>&2 && exit 1

curl -u 'ricaportela@gmail.com' https://api.github.com/user/repos -d "{\"name\":\"$repo_name\"}"

# echo "# caiotasks" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git remote add origin https://github.com/ricaportela/caiotasks.git
# git push -u origin master
