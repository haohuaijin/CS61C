#!/bin/bash
rm -rf ./git
rm -f git.tar
tar -C .. -cf ./git.tar .git
git add ./git.tar
git commit -m "Added the git repo metadata tar to your lab00 folder"
git push origin master
