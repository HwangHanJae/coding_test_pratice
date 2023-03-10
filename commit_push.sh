#!/bin/bash

echo "문제를 입력하세요:"

read TITLE

echo "문제 : ${TITLE}"

git add .

echo "> git add 완료"

git commit -m "문제 : ${TITLE} 추가"

echo "> ${TITLE} commit 완료"

git push

echo "> push 완료"