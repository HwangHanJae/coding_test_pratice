#!/bin/bash

TITLE=${1}

echo '제목 : ${TITLE}'

git add .

git status

# git commit -m '문제 : ${TITLE} 추가
git commit -m "${TITLE} 추가"

echo "> ${TITLE} commit 완료"

git push

echo "> push 완료"