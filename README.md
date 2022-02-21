# sfademo_chiba
千葉県のJA、自治体情報をFlaskapp上で見れるツール

システム概要<br>
・Google Firebaseに保存された自治体やJAの問い合わせ窓口や住所などをFlask上で表示するツール<br>
・現在はFlaskのdebugモードで作成しており、http://127.0.0.1:5000/にアクセスすることで起動できます。<br>
・動作している画面はこちらhttps://drive.google.com/file/d/1h1sfwdCBSaBJSq7mc4uPm8zuRmCl9Ls6/view?usp=sharing<br>

起動に必要なもの<br>
・Firebaseのアクセス用json<br>

今後追加したい機能<br>
【ツール統合】
・JA千葉の店舗データをスクレイピングコードをFlask上から使えるようにしたい<br>
・Firebaseに読み書きするコードをFlask上から使えるようにしたい<br>
・iOS標準カレンダーにイベントを追加するコードをFlask上から使えるようにしたい<br>
【完全未実装で盛り込みたいもの】<br>
・データ一覧画面でソートなどの機能<br>
・経路案内ページにて、DB上のデータからGoogle_Directional_APIと連携したiOS用イベント作成機能<br>
