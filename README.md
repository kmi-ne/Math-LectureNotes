# Math-LectureNotes

数学の講義ノート．

## ディレクトリ構造

```
Math-LectureNotes
├─ pdf [pdf 置き場]
│  └─ lect-<講義の識別子>
│     ├─ lect-<講義の識別子>.pdf [メイン文書]
│     └─ lect-<講義の識別子>-<サブ文書識別子>.pdf [サブ文書]
├─ tex [tex ソース置き場]
│  ├─ _cfg-global [全講義に共通の文書設定]
│  │  ├─ cfg.sty [メイン設定 (以下3つのいずれかを呼び出し)]
│  │  ├─ cfg-draft.sty [とりあえずコンパイルしたいときの設定]
│  │  ├─ cfg-full.sty [完成品用の設定]
│  │  └─ cfg-light.sty [下書き用の設定]
│  ├─ _pkg [自作パッケージ置き場]
│  │  ├─ <パッケージ名>.sty
│  │  └─ ...
│  └─ lect-<講義の識別子>
│     ├─ _cfg-local [講義ごとの文書設定]
│     │  ├─ macro.sty [マクロ集]
│     │  └─ ...
│     ├─ main [メイン文書のソース置き場]
│     │  ├─ sub [サブソース置き場]
│     │  │  ├─ 01 [chapter 1]
│     │  │  │  ├─ 01.tex [section 1]
│     │  │  │  ├─ 02.tex
│     │  │  │  ├─ ...
│     │  │  │  └─ main.tex [各 section のソースをここで統合]
│     │  │  ├─ ...
│     │  │  └─ misc [chapter 以外のサブソース置き場]
│     │  │     └─ <サブソース名>.tex
│     │  ├─ .latexmkrc
│     │  └─ main.tex [メインソース]
│     └─ <サブ文書識別子> [サブ文書のソース置き場]
│        ├─ ...
│        ├─ .latexmkrc
│        └─ main.tex
├─ .gitattributes
├─ .gitignore
├─ LICENSE.md
└─ README.md
```
