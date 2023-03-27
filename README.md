# ProjectPiBot

git push 시 [remote: fatal error in commit_refs] 에러 해결법 

1. cmd창에 git fsck (데이터베이스의 Integrity를 검사)
2. 두번째로 git gc (저장소에 필요없는 파일을 삭제하고 남은 파일을 압축하는 “Garbage Collection”)
