# 깊은산 채굴기 작업 기준

깊은산 채굴기의 공통 작업 원본은 https://github.com/icycream14/mine 의 main 브랜치입니다. 다른 대화에서도 먼저 이 저장소의 최신 main을 읽고 작업합니다. Sites 저장소는 기존 사이트 발행에 사용하는 배포 대상입니다.

- Sites project_id: appgprj_6ad8d5164e44819181d90339c18c4c0e
- 운영 주소: https://deepmine-mobile-gamnamu.super-soldier.chatgpt.site
- 소스: https://git.chatgpt-team.site/2f5f1b72-e159-455e-878c-342e37e5bd12/appgprj_6ad8d5164e44819181d90339c18c4c0e.git
- 브랜치: main
- 정적 배포 폴더: dist

수정 전에 GitHub main의 최신 소스와 로컬 변경을 확인합니다. 배포 전에는 Sites 스킬의 source helper로 기존 프로젝트를 열어 배포 대상의 최신 변경도 비교합니다. GitHub 변경을 반영하지 않은 Sites 소스를 새 원본으로 덮어쓰지 않습니다. 다른 대화의 로컬 파일이 자동으로 공유된다고 가정하지 않습니다. 큐브 살아남기와 왕의기사 저장소를 이 게임의 원본으로 사용하지 않습니다.

실제 편집 파일은 dist/game.js, dist/style.css, dist/index.html입니다. 배포 HTML은 내용 해시가 포함된 JS와 CSS 파일을 참조합니다. JS 또는 CSS 수정 후 해시 파일을 재생성하고 index.html 참조를 갱신해야 합니다. 이전 해시 파일을 그대로 참조하면 새 패치가 실행되지 않습니다.

기존 저장 키 deepmine_site_v4와 기존 진행 기록을 보존합니다. 필요한 검사 후 source helper로 커밋 및 푸시합니다. 배포 요청 시 기존 Sites 프로젝트에 동일 커밋의 정적 산출물을 배포합니다. 배포한 버전과 커밋을 구분해 보고하며 다른 대화의 패치까지 비교하지 않았다면 모두 반영됐다고 말하지 않습니다.

GitHub main에 게임 소스와 검사 파일을 저장한 후 같은 파일을 기존 Sites 프로젝트에 반영합니다. scripts/prepare-assets.py 실행 후 check-game.cjs, check-progression.cjs, check-items.cjs를 실행합니다. 두 저장소의 dist 파일 SHA256이 같은지 확인합니다. GitHub 푸시만으로 Sites가 자동 배포된다고 설명하지 않습니다. 배포는 Sites 도구로 완료하고 성공 결과를 확인해야 합니다. GitHub Actions는 추가하지 않습니다.
