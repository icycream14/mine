# 깊은산 채굴기

공통 소스: https://github.com/icycream14/mine

운영 사이트: https://deepmine-mobile-gamnamu.super-soldier.chatgpt.site

## 작업과 배포

main 브랜치가 공통 작업 원본입니다. 다른 대화에서도 최신 main을 읽고 수정합니다. 작업 기준은 AGENTS.md에 있습니다.

실제 게임 파일은 dist/game.js, dist/style.css, dist/index.html입니다. 기존 저장 키 deepmine_site_v4를 유지합니다.

수정 후 실행합니다.

```bash
python scripts/prepare-assets.py
node check-game.cjs
node check-progression.cjs
node check-items.cjs
```

GitHub에 수정본을 저장한 뒤 기존 Sites 프로젝트에 같은 dist 파일을 배포합니다. .openai/hosting.json이 기존 프로젝트를 식별합니다. GitHub 푸시만으로 사이트가 자동 발행되는 구성은 아닙니다. GitHub Actions를 사용하지 않습니다.

## 로컬 실행

```bash
python -m http.server 8080 --directory dist
```

http://localhost:8080 에서 실행합니다.
