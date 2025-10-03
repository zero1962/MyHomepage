#!/usr/bin/perl

require 'jcode.pl';

print "Content-type: text/html; charset=EUC-JP \n\n";
print '<body background="kabe2.gif">';
print "<head>";
print "<title>エクサの勉強部屋</title>";
print "</head>";
print '<font color="#ffffff" size="3">';


#///////////////////////会話入力///////////////////////////
read(STDIN, $str, $ENV{"CONTENT_LENGTH"});
$str =~ tr/+/ /;
$str =~ s/%([0-9a-fA-F][0-9a-fA-F])/pack("C", hex($1))/eg;
jcode::convert(*str,'euc');
($str2,$str3,$str4,$str5,$str6)=split(/&/,$str);

($ky,$ky2)=split(/=/,$str2);
($hennji,$hennji2)=split(/=/,$str3);
($suki,$suki2)=split(/=/,$str4);
($kao,$kao2)=split(/=/,$str5);
($kokoro1,$kokoro2)=split(/=/,$str6);


#//////////////////半角カタカナを全角にします//////////////
jcode::h2z_euc(\$ky2);


####全角英数を半角英数にします###############
$from = "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"
       . "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"
       . "０１２３４５６７８９＊．／＾＿＄"
       . "!\"#%&'()+,:;<=>?\@[\\]`{|}~-";

$to = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
         . "0123456789*./^_\$"
         . "！”＃％＆’（）＋，：；＜＝＞？＠[￥]‘｛｜｝〜−";

jcode::tr(\$ky2,$from, $to); 


#//////////////////小文字を大文字へ////////////////////////
$from = "abcdefghijklmnopqrstuvwxyz";
$to = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
jcode::tr(\$ky2,$from, $to); 


#*******************************人工無脳エクサ　マッチングエンジン（$jump）***************************************

#---入力ないと書き込まないぞ---
if($hennji2 ne ""){
if($kokoro2 == 0){
if($ky2 ne ""){
open(ai,">>./dat/ai.dat");
print ai"\n$ky2,";
print ai"$hennji2,";
print ai"$suki2,";
print ai"$kao2";
close(ai);
}

} elsif ($kokoro2 == 1){
open(futuu,">>./dat/futuu.dat");
print futuu"\n$hennji2,";
print futuu"$suki2,";
print futuu"$kao2";
close(futuu);

} elsif ($kokoro2 == 2){
open(suki,">>./dat/suki.dat");
print suki"\n$hennji2,";
print suki"$suki2,";
print suki"$kao2";
close(suki);

} elsif ($kokoro2 == 3){
open(kirai,">>./dat/kirai.dat");
print kirai"\n$hennji2,";
print kirai"$suki2,";
print kirai"$kao2";
close(kirai);

} elsif ($kokoro2 == 4){
if($ky2 ne ""){
open(event,">>./dat/event.dat");
print event"\n$ky2,";
print event"$hennji2,";
print event"$suki2,";
print event"$kao2";
close(event);
}
} elsif ($kokoro2 == 5){
if($ky2 ne ""){
open(joukyou,">>./dat/joukyou.dat");
print joukyou"\n$ky2,";
print joukyou"$hennji2,";
print joukyou"$suki2,";
print joukyou"$kao2";
close(joukyou);
}
}
}

#//////////////////////入力窓展開//////////////////////////


print '<FORM ACTION="gakushuu.cgi" METHOD="POST">';
print '単語をいれてね  φ(￣∇￣o)<BR><BR>';
print 'キーワード<INPUT TYPE="TEXT" NAME="name" SIZE="20"><BR>';
print '返事<INPUT TYPE="TEXT" NAME="name" SIZE="100"><BR>';
print "こころパラメーター";
print "<BR>";
print '<input type="radio" name="kokoro"value="0" CHECKED>0_ふつう<BR>';
print '<INPUT TYPE="radio" name="kokoro"value="1">1_すき<BR>';
print '<input type="radio" name="kokoro"value="2">2_きらい<BR>';
print "<BR>";
print "気持ち";
print "<BR>";
print '<input type="radio" name=" kimoti"value="0" CHECKED>0_ふつう<BR>';
print '<input type="radio" name=" kimoti"value="1">1_楽しい<BR>';
print '<input type="radio" name=" kimoti"value="2">2_あきれ<BR>';
print '<input type="radio" name=" kimoti"value="3">3_悲しい<BR>';
print '<input type="radio" name=" kimoti"value="4">4_怒り<BR>';
print '<input type="radio" name=" kimoti"value="5">5_テレ<BR>';
print '<input type="radio" name=" kimoti"value="6">6_笑い<BR>';
print '<input type="radio" name=" kimoti"value="7">7_驚き<BR>';
print '<input type="radio" name=" kimoti"value="9">9_哀愁<BR>';
print '<input type="radio" name=" kimoti"value="11">11_いじわる<BR>';
print '<input type="radio" name=" kimoti"value="12">12_笑顔<BR>';
print "<BR>";
print "辞書";
print "<BR>";
print '<input type="radio" name=" DATA"value="0" CHECKED>0_会話<BR>';
print '<input type="radio" name=" DATA"value="1">1_普通<BR>';
print '<input type="radio" name=" DATA"value="2">2_好き<BR>';
print '<input type="radio" name=" DATA"value="3">3_嫌い<BR>';
print '<input type="radio" name=" DATA"value="4">4_イベント<BR>';
print '<input type="radio" name=" DATA"value="5">5_状況<BR>';
print '<INPUT TYPE="SUBMIT" VALUE="送信"><BR>';
print "<BR>";


#///////////////////////説明///////////////////////////////
print '---記入方法---<BR>';
print '・カタカナは全角でね<BR>';
print '・キーワードの間に「_」を入れると2キーワード<BR>・キーワードの最初に「EE」と入れるとエクサのこと「MM」と入れるとあなたの事になります。<BR>';
print '・返事に「user」と入力すると名前「nen」と入力すると年「jikan」と入力すると時間「niti」と入力すると日「youbi」と入力すると曜日が入ります。<BR>';
print '・キーワードに「__」の後、前回のエクサの返事、返事に次に言う言葉で語りモードに入ります。<BR>';
print '<BR>・正規表現の許可（注意：正規表現のみの入力は出来ません）<BR>';
print '・キーワードの前に「^」で先頭マッチ、キーワードの後ろに「$」で語尾マッチ、途中に「.*」で前後の言葉マッチ<BR>';
print "<BR>";

#////////////////////////プレビュー////////////////////////
print "<BR>";
print "キーワード$str2";
print "<BR>";
print "返事$str3";
print "<BR>";
print "こころ$str4";
print "<BR>";
print "気持ち$str5";
print "<BR>";
print "辞書$str6";
print "<BR>";
print '</font>';

exit;