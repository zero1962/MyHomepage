//
//   日付時刻メッセージ・スクリプト
//
// 日よって文字を変える
m = (new Date()).getMonth() + 1;
d = (new Date()).getDate();
if     ((m ==  1) && (d ==  1)) document.write("元日です<br>");
else if((m ==  1) && (d == 13)) document.write("成人の日です<br>");
else if((m ==  2) && (d == 11)) document.write("建国記念日です<br>");
else if((m ==  3) && (d == 21)) document.write("春分の日です<br>");
else if((m ==  4) && (d == 29)) document.write("みどりの日です<br>");
else if((m ==  5) && (d ==  3)) document.write("憲法記念日です<br>");
else if((m ==  5) && (d ==  5)) document.write("こどもの日です<br>");
else if((m ==  7) && (d == 21)) document.write("海の日です<br>");
else if((m ==  9) && (d == 15)) document.write("敬老の日です<br>");
else if((m ==  9) && (d == 23)) document.write("秋分の日です<br>");
else if((m == 10) && (d == 13)) document.write("体育の日です<br>");
else if((m == 11) && (d ==  3)) document.write("文化の日です<br>");
else if((m == 12) && (d == 23)) document.write("勤労感謝の日です");
else if((m == 12) && (d == 23)) document.write("天皇誕生日です<br>");
//else document.write("今日は特に何もありません");

if((m ==  1) && (d >= 1)&&(d <=  7)) document.write("明けましておめでうございます<br>");
if((m == 12) && (d >= 1)&&(d <= 31)) document.write("寒中師走でございます<br>");

if((m == 12) && (d == 24)) document.write("メリークリスマス！  <br>");
if((m == 12) && (d == 25)) document.write("メリークリスマス！  <br>");
if((m ==  6) && (d == 15)) document.write("おめでたい日ですね！<br>");
if((m ==  8) && (d == 17)) document.write("おめでたい日ですね！<br>");
if((m ==  4) && (d == 17)) document.write("おめでたい日ですね！<br>");
if((m ==  5) && (d == 23)) document.write("おめでたい日ですね！<br>");
if((m == 10) && (d ==  2)) document.write("おめでたい日ですね！<br>");


//
//  終わり
//



        //配列関数定義
        function MakeArray(n){
                this.length=n;
        }

        var today=new Date();
        var m=today.getMonth();
        var d=today.getDate();
        var w=today.getDay();
        var mm=new MakeArray(55);
        var dd=new MakeArray(55);
        var cc=new MakeArray(55);
        var ww=new MakeArray(7);
        var hh=new MakeArray(7);
        var kr = new kyureki(today.getJD());

        ww[1]="日";ww[2]="月";ww[3]="火";ww[4]="水";ww[5]="木";ww[6]="金";ww[7]="土";
        hh[1]="幸運な日です" ;hh[2]="酒でも飲もう" ;hh[3]="悲しい事もあるさ" ;
        hh[4]="友に感謝" ;hh[5]="食べ過ぎは禁物" ;hh[6]="許せ他人の失敗";hh[7]="昨日の次の日" ;

        mm[1]=1;mm[2]=1 ;mm[3]=2 ;mm[4]=3 ;mm[5]=4 ;mm[6]=5 ;mm[7]=5;mm[8]=9 ;
        dd[1]=1;dd[2]=15;dd[3]=11;dd[4]=21;dd[5]=29;dd[6]=3 ;dd[7]=5;dd[8]=15;
        mm[9]=9 ;mm[10]=10;mm[11]=11;mm[12]=11;mm[13]=12;
        dd[9]=23;dd[10]=10;dd[11]=3 ;dd[12]=23;dd[13]=23;
        cc[1]="元日";cc[2]="成人の日";cc[3]="建国記念日";cc[4]="春分の日";cc[5]="みどりの日";
        cc[6]="憲法記念日";cc[7]="こどもの日";cc[8]="敬老の日";cc[9]="秋分の日";cc[10]="体育の日";
        cc[11]="文化の日";cc[12]="勤労感謝の日";cc[13]="天皇誕生日";

        mm[14]=1 ;mm[15]=2 ;mm[16]=3 ;mm[17]=3 ;mm[18]=4 ;mm[19]=4;mm[20]=5 ;mm[21]=5;
        dd[14]=16;dd[15]=3 ;dd[16]=3 ;dd[17]=18;dd[18]=1 ;dd[19]=8;dd[20]=1 ;dd[21]=2;
        mm[22]=5 ;mm[23]=6 ;mm[24]=6 ;mm[25]=7 ;mm[26]=7 ;mm[27]=7;mm[28]=9;mm[29]=9;
        dd[22]=5 ;dd[23]=10;dd[24]=11;dd[25]=7;dd[26]=15;dd[27]=23;dd[28]=1;dd[29]=20;
        mm[30]=11 ;mm[31]=12;mm[32]=12;
        dd[30]=15 ;dd[31]=25;dd[32]=31;
        cc[14]="薮入";cc[15]="節分";cc[16]="ひな祭";cc[17]="彼岸入り";cc[18]="万遇節";
        cc[19]="灌仏";cc[20]="メーデー";cc[21]="八十八夜";cc[22]="端午の節句";cc[23]="時の記念日";
        cc[24]="入梅";cc[25]="七夕祭";cc[26]="ふみの日";cc[27]="二百十日";cc[28]="震災記念日";
        cc[29]="彼岸入り";cc[30]="七五三";cc[31]="クリスマス";cc[32]="大祓";

        mm[33]=1 ;mm[34]=1 ;mm[35]=2 ;mm[36]=2 ;mm[37]=3 ;mm[38]=3;mm[39]=4 ;mm[40]=4 ;
        dd[33]=5 ;dd[34]=20;dd[35]=4 ;dd[36]=19;dd[37]=6;dd[38]=21;dd[39]=5 ;dd[40]=20;
        mm[41]=5 ;mm[42]=5 ;mm[43]=6 ;mm[44]=6 ;mm[45]=7 ;mm[46]=7;mm[47]=8 ;mm[48]=8 ;
        dd[41]=6 ;dd[42]=21;dd[43]=6 ;dd[44]=21;dd[45]=7;dd[46]=23;dd[47]=8 ;dd[48]=23;
        mm[49]=9 ;mm[50]=9;mm[51]=10;mm[52]=10;mm[53]=11;mm[54]=11;mm[55]=12;mm[56]=12;
        dd[49]=8 ;dd[50]=23;dd[51]=8 ;dd[52]=24;dd[53]=8;dd[54]=22;dd[55]=7 ;dd[56]=22;
        cc[33]="小寒";cc[34]="大寒";cc[35]="立春";cc[36]="雨水";cc[37]="啓蟄";
        cc[38]="春分";cc[39]="清明";cc[40]="穀雨";cc[41]="立夏";cc[42]="小満";
        cc[43]="芒種";cc[44]="夏至";cc[45]="小暑";cc[46]="大暑";cc[47]="立秋";
        cc[48]="処暑";cc[49]="白露";cc[50]="秋分";cc[51]="寒露";cc[52]="霜降";
        cc[53]="立冬";cc[54]="小雪";cc[55]="大雪";cc[56]="冬至";
        flg=0;
//        document.write(" ",m+1,"月",d,"日（",ww[w+1],"）")

document.write(" ",m+1,"月",d,"日（",ww[w+1],"）")
//     kr.year     : 旧暦年（数値）
//     kr.uruu     : 平月／閏月 flag （ブール値 平月:false 閏月:true）
//     kr.month    : 旧暦月（数値）
//     kr.day      : 旧暦日（数値）
//     kr.rokuyo   : 六曜名（文字列）
//     kr.mage     : リアルタイム月齢（数値）
//     kr.magenoon : 正午月齢（数値）
//     kr.illumi   : 輝面比（数値 ％）
//     kr.mphase   : 月相（整数値:0..27）
document.write(" ",kr.rokuyo);


//      var a = Math.floor(Math.random() * 100);

//      if ( a <= 19 ) { kiti=1; }
//      else if ( a <= 39 ) { kiti=2; }
//      else if ( a <= 59 ) { kiti=3; }
//      else if ( a <= 69 ) { kiti=4; }
//      else if ( a <= 79 ) { kiti=5; }
//      else if ( a <= 94 ) { kiti=6; }
//      else { kiti=7; };

//      if ( kiti == 1 ) { moji = '大吉'; color = 'FF0000'; }
//      if ( kiti == 2 ) { moji = '中吉'; color = 'FF8000'; }
//      if ( kiti == 3 ) { moji = '小吉'; color = 'FF00FF'; }
//      if ( kiti == 4 ) { moji = '吉'; color = '00FF00'; }
//      if ( kiti == 5 ) { moji = '末吉'; color = '0000FF'; }
//      if ( kiti == 6 ) { moji = '凶'; color = '800000'; }
//      if ( kiti == 7 ) { moji = '大凶'; color = '800080'; };

//      document.write ( '<br>あなたの今の運勢は <FONT SIZE="2" COLOR="#');
//      document.write ( color + '"><B>' + moji + '</B></FONT> です。' );


        for(i=1; i<=13; i++) {
                if(m+1 == mm[i] && d == dd[i]) {
                        document.write("<br>祝日：",cc[i]);
                        flg=1;
                }
        }
        for(i=14; i<=32; i++) {
                if(m+1 == mm[i] && d == dd[i]) {
                        document.write("<br>年中行事：",cc[i]);
                        flg=1;
                }
        }
        for(i=33; i<=56; i++) {
                if(m+1 == mm[i] && d == dd[i]) {
                        document.write("<br>24節気：",cc[i]);
                        flg=1;
                }
        }
        if(flg == 0) {
                pp = (m+1) + d * 3;
//                flg = pp - 10 * Math.floor(pp/10);
                flg = Math.floor(Math.random() * 11);
                if(flg >= 1 && flg <= 7)
                        document.write("<br>",hh[flg]);
                if(flg >= 8 && flg<=11 || flg == 0)
                        document.write("<br>普通の日");
        }


// 現在時刻に合わせて文字を変える
h = (new Date()).getHours();
document.write("<br>");
if     ((h >=  0) && (h <  3)) document.write("午前０時を回りました   ご安全に！");
else if((h >=  3) && (h <  6)) document.write("もうすぐ夜が明けますね ご安全に！");
else if((h >=  6) && (h <  9)) document.write("おはようございます！   ご安全に！");
else if((h >=  9) && (h < 11)) document.write("お昼ごはんは何にしましょう？");
else if((h >= 11) && (h < 12)) document.write("もうすぐお昼ごはんですね！！");
else if((h >= 12) && (h < 13)) document.write("お昼休みです！");
else if((h >= 13) && (h < 15)) document.write("眠くなってくる頃ですね ご安全に！");
else if((h >= 15) && (h < 18)) document.write("お仕事頑張ってますか？ ご安全に！");
else if((h >= 18) && (h < 21)) document.write("こんばんは！           ご安全に！");
else if((h >= 21) && (h < 24)) document.write("もうすぐ寝る時間ですね ご安全に！");
//
//
//
