#!/bin/bash

echo "문제 제목을 입력해주세요: "

read title

echo '제목 : $title'

git add .

git status

# git commit -m '문제 : $title 추가
git commit -m '$title 추가'

git push